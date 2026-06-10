from typing import List, Dict, Any
from core.parsing.models import ParsedElement
from core.chunking import recursive_character_chunking

class ElementChunker:
    """Intelligently chunks elements depending on their semantic type using Parent-Child logic."""
    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 100):
        self.parent_size = chunk_size
        self.child_size = max(200, chunk_size // 4)
        self.overlap = chunk_overlap

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
                # Split text into parents
                parent_texts = recursive_character_chunking(
                    el.content, 
                    chunk_size=self.parent_size, 
                    chunk_overlap=self.overlap
                )
                
                chunk_idx = 0
                for p_text in parent_texts:
                    p_meta = base_meta.copy()
                    p_meta["chunk_index"] = chunk_idx
                    p_meta["is_child"] = False
                    p_meta["parent_chunk_index"] = -1
                    final_chunks.append({
                        "content": p_text,
                        "metadata": p_meta
                    })
                    parent_global_idx = chunk_idx
                    chunk_idx += 1
                    
                    # Split this parent text into children
                    child_texts = recursive_character_chunking(
                        p_text, 
                        chunk_size=self.child_size, 
                        chunk_overlap=max(20, self.child_size // 4)
                    )
                    for c_text in child_texts:
                        c_meta = base_meta.copy()
                        c_meta["chunk_index"] = chunk_idx
                        c_meta["is_child"] = True
                        c_meta["parent_chunk_index"] = parent_global_idx
                        final_chunks.append({
                            "content": c_text,
                            "metadata": c_meta
                        })
                        chunk_idx += 1
            
            elif el.element_type in ["table", "image"]:
                # Atomic chunking - never split tables or images to preserve context
                meta = base_meta.copy()
                meta["chunk_index"] = 0
                meta["is_child"] = False
                meta["parent_chunk_index"] = -1
                final_chunks.append({
                    "content": el.content,
                    "metadata": meta
                })
                
        return final_chunks

