# main.py — Anchor1 Test Runner

from bridge.bridge import bridge_input, get_anchor_state
from bridge.bridge_utils import load_memory, initialize_anchor1_memory

# Simulated session object
class Session:
    def __init__(self):
        self.core = {"Fear": 0.4, "Safety": 0.5, "Time": 0.3, "Choice": 0.3}
        self.focus = "Social"
        self.container = "Pub"
        self.goal = "Blend in"
        self.beliefs = {
            "I am loyal": 1.0,
            "I am unattractive": 0.8,
            "I am dangerous": 0.9,
            "I am intelligent": 0.7
        }
        self.memory_orbit = []
        self.container_links = {"Pub": {"Home": 0.5}, "Home": {"Pub": 0.5}}
        self.G_history = []
        self.behavior_log = []
        self.ticks = 0

# Initialize session
session = Session()

# Load memory
memories = load_memory("memory/memory_containers.json")
initialize_anchor1_memory(session, memories)

# Send test input
user_input = "You're back at the cave and there's a loud noise."
updated_state = bridge_input(session, user_input)

# Print output
print("Anchor1 State Snapshot:")
for k, v in updated_state.items():
    print(f"{k}: {v}")
