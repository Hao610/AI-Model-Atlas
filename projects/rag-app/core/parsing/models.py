from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class ParsedElement:
    element_type: str  # e.g., "text", "table", "image"
    content: str
    page: int
    source: str
    section: str = ""
    element_id: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)
