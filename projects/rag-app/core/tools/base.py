from abc import ABC, abstractmethod
from typing import Any

class BaseTool(ABC):
    """Unified interface for all tools in the Orchestration Layer."""
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
        
    @property
    @abstractmethod
    def description(self) -> str:
        pass
        
    @abstractmethod
    def run(self, query: str) -> Any:
        pass
