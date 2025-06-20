"""
IX-ThePlague Core Infectious Disease Knowledge Module

Provides definitions, explanations, and key facts related to infectious diseases,
pathogens, transmission methods, and epidemiology.
"""

class InfectiousKnowledge:
    def __init__(self):
        self.facts = {
            "virus": "A microscopic infectious agent that replicates only inside the living cells of an organism.",
            "bacteria": "Single-celled microorganisms that can exist either as independent organisms or as parasites.",
            "pathogen": "An organism that causes disease in its host.",
            "epidemic": "A widespread occurrence of an infectious disease in a community at a particular time.",
            "pandemic": "An epidemic that has spread across multiple countries or continents, usually affecting a large number of people.",
            "transmission": "The process by which a disease spreads from one individual to another."
        }

    def get_fact(self, term: str) -> str:
        t = term.lower().strip()
        return self.facts.get(t, f"Unknown infectious disease concept: '{term}' — not found in ThePlague’s knowledge base.")

# Standalone test
if __name__ == "__main__":
    ip = InfectiousKnowledge()
    print(ip.get_fact("virus"))
    print(ip.get_fact("pandemic"))
    print(ip.get_fact("superbug"))
