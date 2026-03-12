import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

VECTOR_DB_PATH = "vector_store/index.faiss"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
