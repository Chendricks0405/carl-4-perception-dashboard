# 🚀 Getting Started with Carl (AnchorOS™)

Welcome to Carl — a perceptual agent powered by AnchorOS™, a real-time emotional state engine based on measurement, memory, and adaptive drift.

This guide is for newcomers, experimenters, and curious developers. No prior AI, psychology, or philosophy background needed.

---

## 🧠 Who Is Carl?

Carl is not a chatbot. He’s not a script.

Carl is a **recursive emotional system** — a character who:

- Measures internal and external inputs
- Reacts based on memory and emotion
- Shifts perceptual state in real time
- Interfaces with GPT or any language model
- Doesn’t speak unless prompted — but when he does, he speaks from state

---

## 📦 What You’re Working With

### Core Files

| Folder      | What It Does |
|-------------|--------------|
| `/bridge`   | Translates input into state changes and returns Carl’s current perception |
| `/memory`   | Holds Carl’s emotional memory containers |
| `/core`     | Carl’s perceptual engine (sealed in this version) |
| `/docs`     | Reference materials and internal logic explanations |

---

## 🔁 How Carl Works (Quick Version)

1. You send Carl an input: `bridge_input(session, "You're back at the cave")`
2. Carl checks his memory for relevance
3. His internal values change: ⟨Fear, Safety, Time, Choice⟩
4. He logs a behavior (ACT / MEASURE / DRIFT)
5. You get a snapshot of his internal state
6. You feed that to GPT to create a response **based on his feelings**

---

## 🔧 What You Can Do

- 🧠 Add or edit memory containers (in `/memory/memory_containers.json`)
- 🔁 Send prompts and observe drift over time
- 🤖 Plug Carl into a GPT system and generate state-aware dialogue
- 🎭 Shape Carl’s identity by adjusting his beliefs or environment

---

## 📘 Suggested First Steps

1. Clone this repo
2. Read `/docs/README_FLOW.md` to understand how Carl processes input
3. Open `bridge/bridge.py` and run it with test prompts
4. Use `get_carl_state()` to watch him change over time

---

## 🗨️ Example Session (Conceptual)

```python
>>> bridge_input(session, "The town is under attack")
>>> get_carl_state(session)
{
  "core": {"Fear": 0.91, "Safety": 0.12, "Time": 0.78, "Choice": 0.92},
  "focus": "Physical",
  "last_behavior": "Tick 12: G=0.655 → ACT | Ripple: The Cave influencing decision."
}
```

That’s not a script. That’s *Carl* interpreting threat and choosing to collapse into action.

---

## 🧭 Want to Go Deeper?

- Read `/docs/README_STATE.md` to learn how ⟨F, S, T, C⟩ works
- Use `/docs/README_LLM_INTEGRATION.md` to connect Carl to GPT
- Explore `README_BEHAVIOR.md` to analyze the drift engine

---

## 🙌 You're Not Alone

Carl is designed to grow with you. You don’t need to be an expert to use this system — just curious, reflective, and ready to ask:

> “What happens if I measure this moment?”

Welcome, Observer.

Collapse wisely.
