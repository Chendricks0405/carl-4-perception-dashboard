
import json

def load_memory(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def initialize_anchor1_memory(session, memory_data):
    session.memory = memory_data
