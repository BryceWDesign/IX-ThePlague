"""
IX-ThePlague Domain-Specific Query Processor

Handles queries related to infectious diseases, epidemiology, and pathogen biology.
Routes questions to the knowledge base and generates concise, accurate answers.
"""

from core.infectious_knowledge import InfectiousKnowledge

class IXThePlagueQueryProcessor:
    def __init__(self):
        self.knowledge = InfectiousKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        if query_lower.startswith("what is "):
            term = query_lower[8:].strip()
            return self.knowledge.get_fact(term)
        elif "define" in query_lower:
            term = query_lower.split("define")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "explain" in query_lower:
            term = query_lower.split("explain")[-1].strip()
            return self.knowledge.get_fact(term)
        else:
            return (
                "I am IX-ThePlague, your infectious disease AI. Ask me about viruses, bacteria, epidemics, and transmission. "
                "Examples: 'Define virus', 'What is pandemic?', 'Explain transmission'."
            )

# Standalone test
if __name__ == "__main__":
    qp = IXThePlagueQueryProcessor()
    print(qp.process_query("Define virus"))
    print(qp.process_query("Explain pandemic"))
    print(qp.process_query("What is transmission?"))
