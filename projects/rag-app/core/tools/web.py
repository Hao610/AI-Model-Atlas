from core.tools.base import BaseTool

class WebSearchTool(BaseTool):
    """Simulates a web search engine."""
    
    @property
    def name(self) -> str:
        return "web_search"
        
    @property
    def description(self) -> str:
        return "Searches the live internet for recent information."

    def run(self, query: str) -> str:
        # In a real application, this would call Serper, Tavily, or DuckDuckGo API
        return f"[Simulated Web Search]: Currently offline. Pretending to search for '{query}'..."
