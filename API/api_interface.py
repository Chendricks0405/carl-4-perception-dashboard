
from bridge import bridge_input
from bridge_utils import load_memory, initialize_anchor1_memory
from typing import Dict, Any, Optional

class AnchorAPI:
    def __init__(self, session):
        self.session = session

    def load_memory(self, memory_file: str) -> None:
        memory_data = load_memory(memory_file)
        initialize_anchor1_memory(self.session, memory_data)

    def send_input(self, input_data: str) -> Dict[str, Any]:
        return bridge_input(self.session, input_data)

    def run_tick(self, anchor_updates: Optional[Dict[str, float]] = None) -> Dict[str, float]:
        if anchor_updates is None:
            anchor_updates = {"Fear": 0.0, "Safety": 0.0, "Time": 0.0, "Choice": 0.0}
        self.session.tick(anchor_updates)
        return self.session.core

    def get_current_state(self) -> Dict[str, Any]:
        return {
            "anchor_vector": self.session.core,
            "latest_behavior": self.session.behavior_log[-1] if self.session.behavior_log else None,
            "tick_count": self.session.ticks
        }

    def get_full_state(self) -> Dict[str, Any]:
        return {
            "id": self.session.container.get("id", "unknown"),
            "tick": self.session.ticks,
            "anchor_vector": self.session.core,
            "container": self.session.container,
            "beliefs": self.session.beliefs,
            "memory_orbit": self.session.memory_orbit[-3:],
            "ego_resistance": self.session.ego_resistance,
            "efficiency_history": self.session.efficiency_history[-5:],
            "chaos_history": self.session.chaos_history[-5:],
            "behavior_log": self.session.behavior_log[-5:]
        }
