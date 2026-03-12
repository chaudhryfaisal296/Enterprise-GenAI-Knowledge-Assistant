import os
from app.embeddings import EmbeddingModel
from app.vector_store import VectorStore
from ingestion.chunking import chunk_text

DATA_PATH = "data/documents"

embedder = EmbeddingModel()
vector_store = VectorStore()

def ingest():

    for file in os.listdir(DATA_PATH):

        with open(os.path.join(DATA_PATH, file)) as f:
            text = f.read()

        chunks = chunk_text(text)

        embeddings = embedder.embed(chunks)

        vector_store.add(embeddings, chunks)

    print("Documents ingested successfully")


if __name__ == "__main__":
    ingest()
