import json
import logging
import os
import time
from typing import List, Dict, Any

from core.rag_pipeline import RAGPipeline
from core.evaluation.metrics import (
    FaithfulnessMetric, 
    AnswerRelevancyMetric, 
    ContextPrecisionMetric, 
    GroundednessMetric
)

logger = logging.getLogger(__name__)

class Evaluator:
    def __init__(self, pipeline: RAGPipeline):
        self.pipeline = pipeline
        self.faithfulness = FaithfulnessMetric(pipeline.router)
        self.relevancy = AnswerRelevancyMetric(pipeline.router)
        self.precision = ContextPrecisionMetric(pipeline.router)
        self.groundedness = GroundednessMetric(pipeline.router)
        
    def run_eval_suite(self, dataset_path: str) -> Dict[str, Any]:
        """Runs the entire evaluation suite over a given JSON dataset."""
        if not os.path.exists(dataset_path):
            raise FileNotFoundError(f"Dataset not found: {dataset_path}")
            
        with open(dataset_path, "r", encoding="utf-8") as f:
            dataset = json.load(f)
            
        print(f"Starting Evaluation on {len(dataset)} examples...")
        
        results = []
        routing_correct = 0
        total_latency = 0.0
        
        # Clear previous pipeline traces
        self.pipeline.traces.clear()
        
        for item in dataset:
            query = item["query"]
            expected_route = item["expected_route"]
            print(f"\n[Evaluating] {item['id']}: {query}")
            
            # Execute Pipeline
            stream, _ = self.pipeline.execute_query(query, cache_active=False)
            # Consume stream to finalize the trace
            for _ in stream:
                pass 
                
            # Grab the trace
            trace = self.pipeline.traces[-1]
            total_latency += trace["latency"]
            
            # 1. Routing Accuracy
            is_correct_route = (trace["route"] == expected_route)
            if is_correct_route:
                routing_correct += 1
                
            # 2. LLM Metrics
            metrics = {
                "faithfulness": 0.0,
                "relevancy": 0.0,
                "precision": 0.0,
                "groundedness": 0.0
            }
            
            # Only evaluate RAG metrics if it actually retrieved context
            if trace["route"] == "vector":
                print("  Calculating Faithfulness...")
                f_res = self.faithfulness.score(query, trace["answer"], trace["context"])
                metrics["faithfulness"] = f_res.get("score", 0.0)
                
                print("  Calculating Context Precision...")
                cp_res = self.precision.score(query, trace["answer"], trace["context"])
                metrics["precision"] = cp_res.get("score", 0.0)
                
                print("  Calculating Groundedness...")
                g_res = self.groundedness.score(query, trace["answer"], trace["context"])
                metrics["groundedness"] = g_res.get("score", 0.0)
            
            # Relevancy applies to all routes
            print("  Calculating Answer Relevancy...")
            ar_res = self.relevancy.score(query, trace["answer"], trace["context"])
            metrics["relevancy"] = ar_res.get("score", 0.0)
            
            # Store full result
            results.append({
                "id": item["id"],
                "query": query,
                "expected_route": expected_route,
                "actual_route": trace["route"],
                "route_correct": is_correct_route,
                "metrics": metrics,
                "latency": trace["latency"],
                "answer": trace["answer"],
                "reason": trace["reason"]
            })
            
        # Aggregate
        total = len(dataset)
        vector_count = sum(1 for r in results if r["expected_route"] == "vector")
        summary = {
            "routing_accuracy": routing_correct / total if total else 0,
            "avg_faithfulness": sum(r["metrics"]["faithfulness"] for r in results) / vector_count if vector_count else 0,
            "avg_relevancy": sum(r["metrics"]["relevancy"] for r in results) / total if total else 0,
            "avg_precision": sum(r["metrics"]["precision"] for r in results) / vector_count if vector_count else 0,
            "avg_groundedness": sum(r["metrics"]["groundedness"] for r in results) / vector_count if vector_count else 0,
            "avg_latency": total_latency / total if total else 0
        }
        
        return {
            "summary": summary,
            "details": results
        }
        
    def print_report(self, eval_results: Dict[str, Any]):
        """Prints a beautifully formatted markdown report."""
        summary = eval_results["summary"]
        details = eval_results["details"]
        
        print("\n" + "="*40)
        print("Evaluation Summary")
        print("="*40)
        print(f"Routing Accuracy:  {summary['routing_accuracy']:.2f}")
        print(f"Faithfulness:      {summary['avg_faithfulness']:.2f}")
        print(f"Answer Relevancy:  {summary['avg_relevancy']:.2f}")
        print(f"Context Precision: {summary['avg_precision']:.2f}")
        print(f"Groundedness:      {summary['avg_groundedness']:.2f}")
        print(f"Average Latency:   {summary['avg_latency']:.2f}s")
        print("="*40)
        
        print("\nWorst Examples")
        
        # Sort by lowest relevancy first
        sorted_details = sorted(details, key=lambda x: x["metrics"]["relevancy"])
        
        for idx, item in enumerate(sorted_details[:3]):
            print(f"\n#{idx+1} {item['id']}")
            print(f"Question:\n{item['query']}")
            print(f"Score (Relevancy): {item['metrics']['relevancy']}")
            print(f"Expected Route: {item['expected_route']} | Actual Route: {item['actual_route']}")
            print(f"Answer Snippet: {item['answer'][:100]}...")
        
        print("\n" + "="*40)
