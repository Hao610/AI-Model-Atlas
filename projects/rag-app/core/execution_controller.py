import time
import requests
from config.settings import settings
from core.prompt_templates import PromptTemplates

class ExecutionController:
    def __init__(self, llm_router):
        self.router = llm_router
        self.logs = []

    def log(self, message: str):
        self.logs.append(f"[{time.strftime('%H:%M:%S')}] {message}")

    def execute(self, query: str, context_str: str, system_prompt: str = None, max_retries: int = 2):
        """Orchestrates structured execution, handles retries, and coordinates fallback routing."""
        self.logs.clear()
        
        # 1. Prompt Governance Check
        if not context_str.strip():
            self.log("Warning: Retrieved context is empty. Injecting fallback prompt constraint.")
            user_prompt = f"User Question: {query}\n\nNote: {PromptTemplates.EMPTY_CONTEXT_INSTRUCTIONS}"
            system_prompt = system_prompt or PromptTemplates.DEFAULT_SYSTEM_INSTRUCTIONS
        else:
            self.log("Retrieved context successfully formatted.")
            user_prompt = PromptTemplates.format_context_prompt(context_str, query)
            system_prompt = system_prompt or PromptTemplates.DEFAULT_SYSTEM_INSTRUCTIONS
            
        current_mode = settings.RAG_MODE
        self.log(f"Initiating request execution. Main mode: {current_mode.upper()}")
        
        # Performance latency tracking
        start_time = time.time()
        
        # 2. Router Invocation & Fallback Loop
        attempt = 0
        while attempt <= max_retries:
            attempt += 1
            try:
                # If local Ollama, verify connectivity before request stream
                if current_mode == "ollama":
                    self.log(f"Attempt #{attempt}: Checking local Ollama service health at {settings.OLLAMA_HOST}...")
                    test_response = requests.get(settings.OLLAMA_HOST, timeout=3)
                    test_response.raise_for_status()
                    self.log("Local Ollama is online. Starting streaming response generation.")
                else:
                    self.log(f"Attempt #{attempt}: Connecting to Cloud LLM API endpoint ({settings.API_MODEL})...")
                
                first_token_time = None
                
                # Fetch stream iterator
                stream = self.router.generate_stream(system_prompt, user_prompt)
                
                # Inspect stream output generator (wrap generator to intercept start exceptions)
                def generator_inspector():
                    nonlocal first_token_time
                    iterator = iter(stream)
                    try:
                        # Grab first chunk to see if generation raises immediate errors
                        first_chunk = next(iterator)
                        if "⚠️" in first_chunk:
                            # Immediate system warning returned from router
                            raise ConnectionError(first_chunk.replace("\n", ""))
                        
                        first_token_time = time.time()
                        ttft = first_token_time - start_time
                        self.log(f"Success: First token latency (TTFT): {ttft:.4f} seconds.")
                        yield first_chunk
                    except StopIteration:
                        return
                    
                    # Yield remaining chunks if first chunk succeeded
                    char_count = len(first_chunk)
                    for chunk in iterator:
                        char_count += len(chunk)
                        yield chunk
                        
                    end_time = time.time()
                    duration = end_time - start_time
                    tok_sec = (char_count / 4.0) / duration if duration > 0 else 0
                    self.log(f"Execution complete. Total Latency: {duration:.4f}s | Speed: ~{tok_sec:.2f} tokens/s")
                    
                return generator_inspector()
                
            except Exception as e:
                self.log(f"Execution Error: {str(e)}")
                
                if current_mode == "ollama" and settings.API_KEY:
                    self.log("Ollama connection failed. Activating fallback policy → Routing to Cloud API.")
                    current_mode = "api"
                    # Force settings shift and router reconstruction for fallback
                    settings.RAG_MODE = "api"
                    self.router.__init__()
                    continue
                    
                if attempt <= max_retries:
                    backoff_delay = attempt * 2
                    self.log(f"Retry policy active: backing off for {backoff_delay}s before next attempt...")
                    time.sleep(backoff_delay)
                else:
                    self.log("Max retries exceeded. Halting pipeline execution.")
                    
        # Ultimate fallback generator returning detailed failure log trace
        def error_generator():
            yield f"⚠️ System Execution Failure. Please check execution logs below for troubleshooting diagnostics."
            
        return error_generator()
        
    def get_logs(self) -> list[str]:
        return self.logs
