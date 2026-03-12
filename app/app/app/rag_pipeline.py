from openai import OpenAI
from app.embeddings import EmbeddingModel
from app.vector_store import VectorStore
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

embedder = EmbeddingModel()
vector_store = VectorStore()

def generate_answer(query):

    query_embedding = embedder.embed([query])[0]

    docs = vector_store.search(query_embedding)

    context = "\n".join(docs)

    prompt = f"""
    Use the following context to answer.

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content
