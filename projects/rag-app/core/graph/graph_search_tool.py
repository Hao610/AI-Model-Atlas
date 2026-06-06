from core.tools.base import BaseTool
from core.graph.graph_retriever import GraphRetriever

class GraphSearchTool(BaseTool):
    """Retrieves 1-hop graph relationship context for complex relational queries."""
    
    def __init__(self, retriever: GraphRetriever):
        self.retriever = retriever

    @property
    def name(self) -> str:
        return "Graph Search"

    @property
    def description(self) -> str:
        return "Explores 1-hop knowledge graph relationships to provide supplementary context for relational queries."

    def run(self, query: str) -> str:
        return self.retriever.retrieve(query)
