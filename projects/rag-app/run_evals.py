import os
import sys

# Add root directory to python path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.rag_pipeline import RAGPipeline
from core.evaluation.evaluator import Evaluator

def main():
    dataset_path = os.path.join(os.path.dirname(__file__), "tests", "eval_dataset.json")
    
    print("Initializing RAG Pipeline for Evaluation...")
    pipeline = RAGPipeline()
    
    evaluator = Evaluator(pipeline)
    
    results = evaluator.run_eval_suite(dataset_path)
    evaluator.print_report(results)

if __name__ == "__main__":
    main()
