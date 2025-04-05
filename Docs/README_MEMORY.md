# 🧠 Memory Containers in Carl (AnchorOS™)

Carl’s self-awareness is built through structured memory containers. These are not just data — they shape perceptual drift and behavioral response.

## Memory Format

Each memory includes:

- `id`: Unique memory name
- `EQ`: Emotional Quotient (0.0–1.0)
- `orbit`: How far it is from present attention (0 = close, 1 = distant)
- `tier`: `"active"`, `"cache"`, or `"archive"`
- `focus_lens`: Tags linking to Carl’s internal focus (`Physical`, `Emotional`, `Social`, or `Multi`)

## Example

```json
{
  "id": "First Step",
  "EQ": 0.7,
  "orbit": 0.3,
  "tier": "active",
  "focus_lens": ["Physical", "Emotional"]
}
```

## Load Memory

```python
from bridge.bridge import initialize_carl_memory, load_memory

memories = load_memory("memory/memory_containers.json")
initialize_carl_memory(st.session_state, memories)
```

## Behavior

Memories closer to orbit and with high EQ values influence Carl's drift ticks. Use memories to simulate developmental arcs, traumas, attachments, or identity loops.
