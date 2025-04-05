import json

def load_memory(file_path="memory_containers.json"):
    with open(file_path, "r") as f:
        return json.load(f)

def initialize_carl_memory(session, memory_list):
    session.memory_orbit = memory_list
    session.behavior_log.append(f"[Bridge] Memory containers initialized. Count: {len(memory_list)}")