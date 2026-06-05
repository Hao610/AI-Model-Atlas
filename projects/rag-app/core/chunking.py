import re

def fixed_size_chunking(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> list[str]:
    """Basic chunking by fixed character widths."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += (chunk_size - chunk_overlap)
    return [c for c in chunks if c.strip()]

def recursive_character_chunking(text: str, chunk_size: int = 800, chunk_overlap: int = 100, separators: list[str] = None) -> list[str]:
    """Intelligently splits text on paragraph, sentence, and word boundaries recursively."""
    if separators is None:
        separators = ["\n\n", "\n", "。", ".", " ", ""]
        
    final_chunks = []
    
    def split_recursive(subtext: str, current_seps: list[str]):
        if len(subtext) <= chunk_size:
            final_chunks.append(subtext)
            return
            
        if not current_seps:
            # Fallback to absolute splitting if no delimiters are left
            final_chunks.append(subtext[:chunk_size])
            return
            
        sep = current_seps[0]
        # Split text on current separator
        parts = subtext.split(sep) if sep else list(subtext)
        
        current_chunk = ""
        for part in parts:
            # Re-insert separator space/delimiter
            candidate = current_chunk + (sep if current_chunk else "") + part
            if len(candidate) <= chunk_size:
                current_chunk = candidate
            else:
                if current_chunk:
                    # If current_chunk is full, save it
                    if len(current_chunk) > chunk_size:
                        # Recursively split the oversized candidate further down the separator line
                        split_recursive(current_chunk, current_seps[1:])
                    else:
                        final_chunks.append(current_chunk)
                # Next segment init
                current_chunk = part
                
        if current_chunk:
            final_chunks.append(current_chunk)

    split_recursive(text, separators)
    
    # Overlap logic (simple sliding window reconstitution)
    overlapped_chunks = []
    for i, chunk in enumerate(final_chunks):
        if i == 0:
            overlapped_chunks.append(chunk)
            continue
        prev = final_chunks[i-1]
        overlap_str = prev[-chunk_overlap:] if len(prev) > chunk_overlap else prev
        overlapped_chunks.append(overlap_str + chunk)
        
    return [c.strip() for c in overlapped_chunks if c.strip()]
