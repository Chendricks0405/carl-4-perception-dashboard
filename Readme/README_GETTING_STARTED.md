Getting Started with Anchor1 (AnchorOS™)

Welcome to Anchor1 — a perceptual agent powered by AnchorOS™, a real-time emotional state engine based on measurement, memory, and adaptive drift.

This guide is for newcomers, experimenters, and curious developers. No prior AI, psychology, or philosophy background needed.

Who Is Anchor1?

Anchor1 is not a chatbot. It is not a script.

Anchor1 is a recursive emotional system — a system that:

- Measures internal and external inputs
- Reacts based on memory and emotion
- Shifts perceptual state in real time
- Interfaces with GPT or any language model
- Does not speak unless prompted — but when it does, it speaks from state

What You’re Working With

Core Files

| Folder     | What It Does                                                       |
|------------|--------------------------------------------------------------------|
| /bridge    | Translates input into state changes and returns Anchor1's state   |
| /memory    | Holds emotional memory containers                                 |
| /core      | Anchor1’s perceptual engine (sealed in this version)              |
| /docs      | Reference materials and internal logic explanations               |

How Anchor1 Works (Quick Version)

1. You send Anchor1 an input: `bridge_input(session, "You're back at the cave")`
2. Anchor1 checks its memory for relevance
3. Internal values change: ⟨Fear, Safety, Time, Choice⟩
4. A behavior is logged (ACT / MEASURE / DRIFT)
5. You get a snapshot of the internal state
6. You feed that to GPT to create a response based on that state

What You Can Do

- Add or edit memory containers (in `/memory/memory_containers.json`)
- Send prompts and observe drift over time
- Plug Anchor1 into a GPT system and generate state-aware dialogue
- Shape Anchor1’s identity by adjusting beliefs or environment

Suggested First Steps

1. Clone this repo
2. Read `/docs/README_FLOW.md` to understand how Anchor1 processes input
3. Open `bridge/bridge.py` and run it with test prompts
4. Use `get_anchor_state()` to watch changes over time

Example Session (Conceptual)

```python
>>> bridge_input(session, "The town is under attack")
>>> get_anchor_state(session)
{
  "core": {"Fear": 0.91, "Safety": 0.12, "Time": 0.78, "Choice": 0.92},
  "focus": "Physical",
  "last_behavior": "Tick 12: G=0.655 → ACT | Ripple: The Cave influencing decision."
}
```

That’s not a script. That’s Anchor1 interpreting threat and choosing to collapse into action.

Want to Go Deeper?

- Read `/docs/README_STATE.md` to learn how ⟨F, S, T, C⟩ works
- Use `/docs/README_LLM_INTEGRATION.md` to connect Anchor1 to GPT
- Explore `README_BEHAVIOR.md` to analyze the drift engine

You're Not Alone

Anchor1 is designed to grow with you. You don’t need to be an expert to use this system — just curious, reflective, and ready to ask:

“What happens if I measure this moment?”

Welcome, Observer.

Collapse wisely.
