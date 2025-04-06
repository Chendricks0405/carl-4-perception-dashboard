# 🌀 AnchorOS Perceptual Flow: How Carl Processes Information

This document explains how **AnchorOS™** and Carl move information from **probability to action** through a structured, layered perception system. Understanding this flow is essential for developers, experimenters, and LLM integrations working with Carl’s memory, behavior, and perceptual state.

---

## 🌌 1. Memory = The Probability Field

Memory represents **all potential** perceptual data — echoes of past experience stored in orbit.

- Format: `memory_containers.json`
- Encoded by:
  - `EQ` (Emotional Quotient)
  - `orbit` (distance from active state)
  - `focus_lens` (Physical, Emotional, Social)
- This layer is **non-collapsed** until filtered.

🧠 *Think of memory as Schrödinger’s probability field — everything exists until something filters it.*

---

## 🧭 2. Container = Local Field Collapse

Carl’s environment (e.g., Home, Pub, Work) filters global memory into a **local scope**.

- Reduces perceptual entropy
- Only relevant container-linked values remain active
- Example: “Pub” activates social tethers, memory bias toward relational context

This is the **first perceptual collapse** — narrowing what matters *right now*.

---

## 🎯 3. Focus Lens (P, E, S) = Priority Sharpening

Carl's focus lens amplifies which domain dominates perception.

- Physical = movement, threat proximity
- Emotional = memory EQ, mood resonance
- Social = beliefs, approval dynamics
- The focus lens affects scalar **F** in G′ = T × C × F

This defines **urgency weight**, making incoming data sharper or softer in measurement.

---

## 🔄 4. Act vs. Measure (A&M) = Collapse Decision

This is the binary behavior switch:

- **ACT** = collapse now (threshold met, chaos triggered)
- **MEASURE** = gather more data (within variance range)

This governs:
- Adjustment **speed** of Carl’s state
- Whether the drift recalibrates quickly or gradually
- If chaos is perceived, Carl acts
- If variance is tolerable, Carl measures

Mathematically, this maps to:
- `G′ = T × C × F`
- Compared against `G_threshold = base + (ego_resistance × factor)`
- **If G′ > G_threshold** → ACT
- Else → MEASURE

---

## 🧠 5. Core Shift = Anchor Vector Realignment

Carl updates his Anchor Vector:

⟨Fear, Safety, Time, Choice⟩ = ⟨F, S, T, C⟩

This vector represents:
- Carl’s current perceptual alignment
- Emotional and cognitive state
- Readiness for action

The new state then propagates back:
- Reweights memory orbit values
- Updates G′ for next tick
- Logs behavior trace

---

## 🧘 Bonus: Flow State for Humans

When PES lensing is clean and core state aligns with incoming signal:
- Measurement becomes easy
- Reaction becomes intentional
- **G′ stabilizes**, drift slows, chaos fades

This is perceived as **Flow**.

---

## Summary

| Layer       | Function                          |
|-------------|-----------------------------------|
| Memory      | Probabilistic field               |
| Container   | Local entropy filter              |
| Focus Lens  | Scalar priority amplification     |
| A&M Logic   | Binary collapse toggle            |
| Core Vector | Real-time perceptual alignment    |

---

This file belongs in `/docs/README_FLOW.md`. Please include it when sharing or expanding the AnchorOS/Carl framework.
