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
                response = requests.post(url, json=payload, stream=True, timeout=settings.LLM_TIMEOUT)
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line.decode("utf-8"))
                        content = chunk.get("message", {}).get("content", "")
                        if content:
                            yield content
            except Exception as e:
                raise ConnectionError(f"Ollama connection error: {str(e)}")
        else:
            if not settings.API_KEY:
                raise ValueError("API Key is missing from settings configuration.")
            try:
                stream = self.client.chat.completions.create(
                    model=settings.API_MODEL,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    stream=True,
                    timeout=settings.LLM_TIMEOUT
                )
                for chunk in stream:
                    content = chunk.choices[0].delta.content
                    if content:
                        yield content
            except Exception as e:
                raise ConnectionError(f"Cloud LLM API connection error: {str(e)}")

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """Generates a complete synchronous response. Useful for evaluation grading."""
        if self.mode == "ollama":
            url = f"{settings.OLLAMA_HOST}/api/chat"
            payload = {
                "model": settings.OLLAMA_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "stream": False
            }
            try:
                response = requests.post(url, json=payload, timeout=settings.LLM_TIMEOUT * 2)
                response.raise_for_status()
                return response.json().get("message", {}).get("content", "")
            except Exception as e:
                raise ConnectionError(f"Ollama connection error: {str(e)}")
        else:
            if not settings.API_KEY:
                raise ValueError("API Key is missing from settings configuration.")
            try:
                response = self.client.chat.completions.create(
                    model=settings.API_MODEL,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    stream=False,
                    timeout=settings.LLM_TIMEOUT * 2
                )
                return response.choices[0].message.content
            except Exception as e:
                raise ConnectionError(f"Cloud LLM API connection error: {str(e)}")
