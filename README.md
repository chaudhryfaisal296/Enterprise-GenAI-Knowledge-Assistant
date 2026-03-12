# Enterprise GenAI RAG Platform

Production-grade Retrieval Augmented Generation system for enterprise knowledge search.

## Features

- RAG pipeline
- Vector database (FAISS)
- Multi-agent orchestration
- FastAPI backend
- Docker deployment
- Kubernetes scaling
- MLOps integration

## Architecture

User Query
↓
Embedding Model
↓
Vector Search
↓
Relevant Documents
↓
LLM Reasoning
↓
Final Answer

## Run locally

pip install -r requirements.txt

uvicorn app.main:app --reload

## API

POST /ask

{
 "query": "What is our architecture design?"
}
