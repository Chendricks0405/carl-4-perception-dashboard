# 🧠 AnchorOS — Carl Runtime + Bridge

This repo includes the core AnchorOS perceptual runtime and a bridge interface to connect Carl to LLMs, agents, or user input.

## 🛠 Components

- `Carl_v6.py` — Core perceptual engine (⟨F, S, T, C⟩ + G′ logic)
- `bridge/bridge.py` — Accepts prompts, modifies state, returns JSON
- `memory/memory_containers.json` — Memory shaping Carl’s identity
- `docs/README_MEMORY.md` — Memory editing guide

## 🚧 Core Lock

The core engine is validated and should not be modified casually. Extend Carl’s personality and logic through:

- `bridge_input()`
- `memory_orbit`
- External interfaces (LLMs, APIs, apps)

## 👀 Future Integration

You can attach Carl to a CustomGPT by using `bridge_input()` to update state and feed `get_carl_state()` into the prompt template.
