import os
import base64
import logging
import pdfplumber
import fitz  # PyMuPDF
import pandas as pd
from typing import List

from core.parsing.models import ParsedElement
from config.settings import settings

logger = logging.getLogger(__name__)

class PDFParser:
    def __init__(self, llm_router=None):
        self.llm_router = llm_router

    def parse(self, file_path: str) -> List[ParsedElement]:
        elements: List[ParsedElement] = []
        source_name = os.path.basename(file_path)
        
        logger.info(f"Starting structural parsing for {source_name}")
        
        # 1. Parse text and tables using pdfplumber
        with pdfplumber.open(file_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                page_idx = page_num + 1
                
                # A. Extract Tables
                tables = page.find_tables()
                table_bboxes = []
                for t_idx, table in enumerate(tables):
                    table_bboxes.append(table.bbox)
                    extracted_data = table.extract()
                    
                    if extracted_data and len(extracted_data) > 1:
                        # Convert tabular data to Markdown
                        # Handle potential None values in headers or data
                        headers = [str(h) if h is not None else "" for h in extracted_data[0]]
                        data = [[str(cell) if cell is not None else "" for cell in row] for row in extracted_data[1:]]
                        
                        try:
                            df = pd.DataFrame(data, columns=headers)
                            md_content = df.to_markdown(index=False)
                            
                            element_id = f"table_{page_idx}_{t_idx+1:02d}"
                            
                            elements.append(ParsedElement(
                                element_type="table",
                                content=md_content,
                                page=page_idx,
                                source=source_name,
                                element_id=element_id,
                                metadata={"rows": len(df), "columns": len(df.columns)}
                            ))
                        except Exception as e:
                            logger.warning(f"Failed to parse table on page {page_idx}: {e}")
                
                # B. Extract Text (excluding table regions)
                def not_within_bboxes(obj):
                    # obj contains x0, top, x1, bottom
                    # table_bbox is (x0, top, x1, bottom)
                    for bbox in table_bboxes:
                        if (obj.get("x0", 0) < bbox[2] and obj.get("x1", 0) > bbox[0] and
                            obj.get("top", 0) < bbox[3] and obj.get("bottom", 0) > bbox[1]):
                            return False
                    return True
                
                clean_page = page.filter(not_within_bboxes)
                text = clean_page.extract_text()
                if text and text.strip():
                    element_id = f"text_{page_idx}_01"
                    elements.append(ParsedElement(
                        element_type="text",
                        content=text.strip(),
                        page=page_idx,
                        source=source_name,
                        element_id=element_id,
                        metadata={}
                    ))
        
        # 2. Extract Images using PyMuPDF (fitz)
        if settings.ENABLE_IMAGE_CAPTIONING and self.llm_router:
            logger.info("Image captioning is ENABLED. Processing images...")
            try:
                doc = fitz.open(file_path)
                for page_num in range(len(doc)):
                    page_idx = page_num + 1
                    page = doc[page_num]
                    image_list = page.get_images(full=True)
                    
                    for img_index, img in enumerate(image_list):
                        xref = img[0]
                        base_image = doc.extract_image(xref)
                        image_bytes = base_image["image"]
                        width = base_image["width"]
                        height = base_image["height"]
                        
                        # Filter out small noise images (logos, icons)
                        if width < 200 or height < 200:
                            continue
                            
                        # Here we would normally send the image bytes to GPT-4o / Qwen-VL.
                        # For the current MVP, we simulate the caption generation as requested by Tech Lead
                        # to avoid heavy Multimodal API setups in this specific pull request.
                        caption = "[Image Caption]: Visual chart or diagram detailing specific metrics."
                        
                        element_id = f"image_{page_idx}_{img_index+1:02d}"
                        elements.append(ParsedElement(
                            element_type="image",
                            content=caption,
                            page=page_idx,
                            source=source_name,
                            element_id=element_id,
                            metadata={"width": width, "height": height}
                        ))
                doc.close()
            except Exception as e:
                logger.error(f"Failed to extract images with PyMuPDF: {e}")
                
        return elements
