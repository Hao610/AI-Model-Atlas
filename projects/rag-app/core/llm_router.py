import json
import requests
from config.settings import settings
from openai import OpenAI

class LLMRouter:
    def __init__(self):
        self.mode = settings.RAG_MODE
        self.client = None
        
        if self.mode == "api":
            self.client = OpenAI(
                api_key=settings.API_KEY,
                base_url=settings.API_BASE_URL
            )
            
    def generate_stream(self, system_prompt: str, user_prompt: str):
        """Generates streaming responses from either local Ollama or Cloud API."""
        if self.mode == "ollama":
            url = f"{settings.OLLAMA_HOST}/api/chat"
            payload = {
                "model": settings.OLLAMA_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "stream": True
            }
            try:
                response = requests.post(url, json=payload, stream=True, timeout=30)
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line.decode("utf-8"))
                        content = chunk.get("message", {}).get("content", "")
                        if content:
                            yield content
            except Exception as e:
                yield f"\n⚠️ Error connecting to local Ollama client: {str(e)}. Please check if Ollama service is running on {settings.OLLAMA_HOST}."
        else:
            if not settings.API_KEY:
                yield "\n⚠️ API Key is missing. Please set API_KEY in your env or settings."
                return
            try:
                stream = self.client.chat.completions.create(
                    model=settings.API_MODEL,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    stream=True
                )
                for chunk in stream:
                    content = chunk.choices[0].delta.content
                    if content:
                        yield content
            except Exception as e:
                yield f"\n⚠️ Cloud LLM API Error: {str(e)}"
