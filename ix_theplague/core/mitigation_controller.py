"""
IX-ThePlague Mitigation Controller

Executes mitigation strategies based on threat assessment inputs.
Supports quarantine, node isolation, and system recovery protocols.
"""

from typing import List

class MitigationController:
    def __init__(self):
        self.active_measures: List[str] = []

    def apply_measures(self, recommendations: List[str]):
        for measure in recommendations:
            if measure not in self.active_measures:
                self.active_measures.append(measure)
                self.execute_measure(measure)

    def execute_measure(self, measure: str):
        # Simulate execution of mitigation measure
        print(f"Executing mitigation: {measure}")

    def clear_measures(self):
        self.active_measures.clear()
        print("All mitigation measures cleared.")

# Example usage
if __name__ == "__main__":
    controller = MitigationController()
    recs = ["Immediate system quarantine.", "Activate backup AI nodes."]
    controller.apply_measures(recs)
    print(f"Active measures: {controller.active_measures}")
    controller.clear_measures()
