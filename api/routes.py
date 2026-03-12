from fastapi import APIRouter
from app.agent_system import AgentOrchestrator

router = APIRouter()

agent = AgentOrchestrator()

@router.post("/ask")

def ask_question(query: str):

    response = agent.execute(query)

    return {"answer": response}
