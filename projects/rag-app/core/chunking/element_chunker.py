from typing import List, Dict, Any
from core.parsing.models import ParsedElement
from core.chunking import recursive_character_chunking

class ElementChunker:
    """Intelligently chunks elements depending on their semantic type."""
    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 100):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk(self, elements: List[ParsedElement]) -> List[Dict[str, Any]]:
        final_chunks = []
        
        for el in elements:
            base_meta = {
                "type": el.element_type,
                "page": el.page,
                "source": el.source,
                "section": el.section,
                "element_id": el.element_id
            }
            # Combine core element metadata
            for k, v in el.metadata.items():
                base_meta[k] = str(v)  # ChromaDB metadata must be str/int/float
                
            if el.element_type == "text":
                text_chunks = recursive_character_chunking(
                    el.content, 
                    chunk_size=self.chunk_size, 
                    chunk_overlap=self.chunk_overlap
                )
                for i, txt in enumerate(text_chunks):
                    meta = base_meta.copy()
                    meta["chunk_index"] = i
                    final_chunks.append({
                        "content": txt,
                        "metadata": meta
                    })
            
            elif el.element_type in ["table", "image"]:
                # Atomic chunking - never split tables or images to preserve context
                meta = base_meta.copy()
                meta["chunk_index"] = 0
                final_chunks.append({
                    "content": el.content,
                    "metadata": meta
                })
                
        return final_chunks
