import os
import json
import networkx as nx
from typing import List, Dict, Any, Optional

class GraphStore:
    def __init__(self, db_path: str = "./data/knowledge_graph.json"):
        self.db_path = db_path
        self.graph = nx.DiGraph()
        self.load()

    def add_node(self, entity_name: str, entity_type: str):
        """Adds a node to the graph if it doesn't exist."""
        if not self.graph.has_node(entity_name):
            self.graph.add_node(entity_name, type=entity_type)

    def add_edge(self, source: str, target: str, relation: str, source_doc: str, chunk_id: str):
        """Adds a directed edge with evidence metadata."""
        # Ensure nodes exist (fail-safe)
        if not self.graph.has_node(source):
            self.add_node(source, "Unknown")
        if not self.graph.has_node(target):
            self.add_node(target, "Unknown")
            
        self.graph.add_edge(
            source, 
            target, 
            relation=relation, 
            source_doc=source_doc, 
            chunk_id=chunk_id
        )

    def get_neighbors(self, entity_name: str) -> List[Dict[str, Any]]:
        """1-Hop Traversal: Returns immediate outgoing and incoming relations."""
        neighbors = []
        if not self.graph.has_node(entity_name):
            return neighbors
            
        # Outgoing edges
        for successor in self.graph.successors(entity_name):
            edge_data = self.graph.get_edge_data(entity_name, successor)
            neighbors.append({
                "direction": "outgoing",
                "source": entity_name,
                "target": successor,
                "relation": edge_data.get("relation", ""),
                "evidence": {
                    "source_doc": edge_data.get("source_doc", ""),
                    "chunk_id": edge_data.get("chunk_id", "")
                }
            })
            
        # Incoming edges
        for predecessor in self.graph.predecessors(entity_name):
            edge_data = self.graph.get_edge_data(predecessor, entity_name)
            neighbors.append({
                "direction": "incoming",
                "source": predecessor,
                "target": entity_name,
                "relation": edge_data.get("relation", ""),
                "evidence": {
                    "source_doc": edge_data.get("source_doc", ""),
                    "chunk_id": edge_data.get("chunk_id", "")
                }
            })
            
        return neighbors

    def save(self):
        """Persists the NetworkX graph to a JSON file."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        data = nx.node_link_data(self.graph)
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self):
        """Loads the graph from JSON if it exists."""
        if os.path.exists(self.db_path):
            try:
                with open(self.db_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.graph = nx.node_link_graph(data)
            except Exception as e:
                print(f"Failed to load graph: {e}")
                self.graph = nx.DiGraph()
