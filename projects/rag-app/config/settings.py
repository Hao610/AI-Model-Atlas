import os
from dotenv import load_dotenv

# Load local environment files if present
load_dotenv()

class Settings:
    # System Mode: 'ollama' or 'api'
    RAG_MODE = os.getenv("RAG_MODE", "ollama").lower()
    
    # LLM Settings
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
    
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
    API_KEY = os.getenv("API_KEY", "")
    API_MODEL = os.getenv("API_MODEL", "gpt-4o-mini")
    
    # Embedding Settings
    EMBEDDING_MODE = os.getenv("EMBEDDING_MODE", "local").lower() # 'local' or 'api'
    LOCAL_EMBEDDING_MODEL = os.getenv("LOCAL_EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    API_EMBEDDING_MODEL = os.getenv("API_EMBEDDING_MODEL", "text-embedding-3-small")
    
    # Vector DB Settings
    DB_DIR = os.getenv("DB_DIR", "./data/chromadb")
    UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./data/uploads")

settings = Settings()
