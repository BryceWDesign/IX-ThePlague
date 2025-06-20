"""
IX-ThePlague Viral Simulator

Simulates propagation and containment of AI viral threats within
the IX-Gibson system network for risk assessment and mitigation testing.
"""

import random
from typing import List, Dict

class ViralSimulator:
    def __init__(self, nodes: List[str]):
        """
        Initialize with a list of node identifiers in the network.
        """
        self.nodes = nodes
        self.infected_nodes = set()
        self.time_step = 0

    def infect_node(self, node_id: str):
        if node_id in self.nodes:
            self.infected_nodes.add(node_id)

    def simulate_step(self):
        """
        Simulate one time step of viral spread.
        Each infected node has a chance to infect connected nodes.
        """
        new_infections = set()
        for infected in self.infected_nodes:
            connected = self.get_connected_nodes(infected)
            for node in connected:
                if node not in self.infected_nodes and random.random() < 0.3:
                    new_infections.add(node)
        self.infected_nodes.update(new_infections)
        self.time_step += 1

    def get_connected_nodes(self, node_id: str) -> List[str]:
        """
        Return a list of connected nodes for given node_id.
        For simulation purposes, connections are simulated as neighbors in the list.
        """
        idx = self.nodes.index(node_id)
        neighbors = []
        if idx > 0:
            neighbors.append(self.nodes[idx - 1])
        if idx < len(self.nodes) - 1:
            neighbors.append(self.nodes[idx + 1])
        return neighbors

    def containment_report(self) -> Dict[str, int]:
        """
        Returns stats about infection spread.
        """
        return {
            "time_step": self.time_step,
            "total_nodes": len(self.nodes),
            "infected_count": len(self.infected_nodes),
            "infection_rate": len(self.infected_nodes) / len(self.nodes)
        }

# Example usage
if __name__ == "__main__":
    network = ["Node1", "Node2", "Node3", "Node4", "Node5"]
    sim = ViralSimulator(network)
    sim.infect_node("Node3")
    for _ in range(5):
        sim.simulate_step()
        print(sim.containment_report())
