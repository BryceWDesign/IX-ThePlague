"""
IX-ThePlague Threat Assessor

Analyzes viral simulation data and other system inputs to assess
current risk levels and recommend mitigation strategies.
"""

from typing import Dict

class ThreatAssessor:
    def __init__(self):
        self.risk_level = "Low"
        self.recommendations = []

    def assess(self, data: Dict) -> str:
        infected_ratio = data.get("infection_rate", 0)
        time_step = data.get("time_step", 0)
        
        self.recommendations.clear()

        if infected_ratio > 0.6:
            self.risk_level = "Critical"
            self.recommendations.append("Immediate system quarantine.")
            self.recommendations.append("Activate backup AI nodes.")
        elif infected_ratio > 0.3:
            self.risk_level = "High"
            self.recommendations.append("Isolate infected nodes.")
            self.recommendations.append("Increase monitoring frequency.")
        elif infected_ratio > 0.1:
            self.risk_level = "Moderate"
            self.recommendations.append("Run detailed system scans.")
        else:
            self.risk_level = "Low"
            self.recommendations.append("Maintain standard security protocols.")

        return self.risk_level

    def get_recommendations(self):
        return self.recommendations

# Example usage
if __name__ == "__main__":
    assessor = ThreatAssessor()
    sample_data = {"infection_rate": 0.45, "time_step": 10}
    level = assessor.assess(sample_data)
    print(f"Risk Level: {level}")
    print("Recommendations:")
    for rec in assessor.get_recommendations():
        print(f"- {rec}")
