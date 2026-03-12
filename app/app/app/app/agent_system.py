from app.rag_pipeline import generate_answer

class ResearchAgent:

    def run(self, query):
        return generate_answer(query)


class CriticAgent:

    def review(self, answer):
        if len(answer) < 50:
            return "Answer too short"
        return answer


class AgentOrchestrator:

    def __init__(self):
        self.research = ResearchAgent()
        self.critic = CriticAgent()

    def execute(self, query):

        answer = self.research.run(query)

        reviewed = self.critic.review(answer)

        return reviewed
