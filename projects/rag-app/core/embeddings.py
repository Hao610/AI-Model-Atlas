from config.settings import settings
from openai import OpenAI

class EmbeddingsManager:
    def __init__(self):
        self.mode = settings.EMBEDDING_MODE
        self.local_model = None
        
        if self.mode == "local":
            from sentence_transformers import SentenceTransformer
            self.local_model = SentenceTransformer(settings.LOCAL_EMBEDDING_MODEL)
        else:
            api_key = (settings.API_KEY or "").strip()
            if api_key:
                try:
                    self.client = OpenAI(
                        api_key=api_key,
                        base_url=settings.API_BASE_URL
                    )
                except Exception:
                    self.client = None
            else:
                self.client = None

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        if self.mode == "local":
            return self.local_model.encode(texts).tolist()
        else:
            if not getattr(self, "client", None):
                raise ValueError("Cloud API Key is required for API embeddings. Please set API_KEY in settings or sidebar.")
            response = self.client.embeddings.create(
                input=texts,
                model=settings.API_EMBEDDING_MODEL
            )
            return [data.embedding for data in response.data]

    def embed_query(self, text: str) -> list[float]:
        return self.embed_documents([text])[0]
