# 🧠 Carl’s Internal State — The Anchor Vector ⟨F, S, T, C⟩

Carl’s core perceptual awareness is defined by a 4-dimensional vector:

⟨Fear, Safety, Time, Choice⟩  
Represented as: `core["Fear"]`, `core["Safety"]`, `core["Time"]`, `core["Choice"]`

This Anchor Vector determines Carl’s **real-time alignment** within his environment. It is continuously updated through ripple input, memory weight, focus lens, and perceptual collapse logic.

---

## ⚖️ State Definitions

### 🟥 Fear (F)
- Perceived instability or threat
- Increased by ripple memory aligned with risk
- Decreased by stability signals, routine, or control
- Directly competes with Safety to determine urgency

### 🟩 Safety (S)
- Perceived stability or confidence
- Increased by trust signals, environmental familiarity, or positive reinforcement
- Decreased by rapid change, conflicting input, or failed expectations

### 🕒 Time (T)
- Drift pressure or urgency
- Increases with container shifts or contextual delay
- Interacts with Choice and Focus Lens to produce G′

### ⚡ Choice (C)
- Directional intent
- High Choice = Carl is more decisive or reactive
- Low Choice = hesitation, deferral to measurement phase

---

## 🧮 The Drift Formula

Carl’s decision pressure is calculated as:

**G′ = T × C × F**

This scalar informs:
- How close Carl is to threshold collapse
- Whether `Act` or `Measure` is triggered
- How fast Carl shifts into a new internal state

---

## 🔄 How State Updates Work

1. A memory triggers ripple
2. Ripple modifies F/S weighting
3. Carl’s focus lens adjusts scalar F
4. G′ is calculated from T × C × F
5. G′ compared to threshold
6. If exceeded → ACT (collapse)
7. Else → MEASURE (recalibrate)

---

## 🧠 Reading Carl’s State

Returned via `get_carl_state()` in `bridge.py`:

```json
{
  "core": {
    "Fear": 0.38,
    "Safety": 0.62,
    "Time": 0.31,
    "Choice": 0.45
  },
  "tick": 42,
  "G_prime": 0.053,
  "focus": "Social",
  "container": "Pub"
}
```

---

## 🧘 Summary

Carl’s state isn’t static. It drifts, recalibrates, and collapses based on internal memory and external interaction.

This model gives developers and agents a reliable framework for observing how perception evolves in real time — without exposing the logic engine behind it.

Use Carl’s Anchor Vector to monitor emotional alignment, model impact, and design meaningful interactions.

