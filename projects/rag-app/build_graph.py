import os
import sys
import logging

from core.vectorstore import VectorStoreManager
from core.embeddings import EmbeddingsManager
from core.llm_router import LLMRouter
from core.graph.graph_extractor import GraphExtractor
from core.graph.graph_store import GraphStore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def build_graph():
    logger.info("Initializing Graph Building Pipeline...")
    embeddings = EmbeddingsManager()
    vectorstore = VectorStoreManager(embeddings)
    router = LLMRouter()
    extractor = GraphExtractor(router)
    graph_store = GraphStore()
    
    collection_name = "default_rag"
    
    # 1. Fetch chunks from VectorDB
    logger.info(f"Fetching chunks from ChromaDB collection: {collection_name}")
    try:
        collection = vectorstore.client.get_collection(collection_name)
        data = collection.get()
    except Exception as e:
        logger.error(f"Failed to fetch collection {collection_name}. Did you run ingestion first? Error: {e}")
        return
        
    ids = data.get("ids", [])
    documents = data.get("documents", [])
    metadatas = data.get("metadatas", [])
    
    if not ids:
        logger.info("No documents found in VectorDB. Please run ingestion first.")
        return
        
    logger.info(f"Found {len(ids)} chunks. Starting Two-Stage Graph Extraction...")
    
    # 2. Extract Entities and Relations
    for idx, doc_text in enumerate(documents):
        chunk_id = ids[idx]
        meta = metadatas[idx] or {}
        source_doc = meta.get("source", "Unknown")
        
        logger.info(f"Processing chunk {idx+1}/{len(ids)}: {chunk_id}")
        
        # We only want to process Text chunks (ignore Tables and Images for relation extraction)
        if meta.get("type", "text") != "text":
            logger.info("Skipping non-text chunk to save LLM tokens.")
            continue
            
        result = extractor.extract(doc_text)
        entities = result.get("entities", [])
        relations = result.get("relations", [])
        
        logger.info(f"Extracted {len(entities)} entities and {len(relations)} relations.")
        
        # 3. Add to GraphStore
        for ent in entities:
            graph_store.add_node(ent.get("entity", ""), ent.get("type", "Unknown"))
            
        for rel in relations:
            graph_store.add_edge(
                source=rel.get("source", ""),
                target=rel.get("target", ""),
                relation=rel.get("relation", ""),
                source_doc=source_doc,
                chunk_id=chunk_id
            )
            
    # 4. Save Graph
    graph_store.save()
    logger.info(f"Graph construction complete. Saved to {graph_store.db_path}.")

if __name__ == "__main__":
    build_graph()
