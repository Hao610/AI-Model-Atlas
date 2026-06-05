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
            self.client = OpenAI(
                api_key=settings.API_KEY,
                base_url=settings.API_BASE_URL
            )

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        if self.mode == "local":
            return self.local_model.encode(texts).tolist()
        else:
            response = self.client.embeddings.create(
                input=texts,
                model=settings.API_EMBEDDING_MODEL
            )
            return [data.embedding for data in response.data]

    def embed_query(self, text: str) -> list[float]:
        return self.embed_documents([text])[0]
