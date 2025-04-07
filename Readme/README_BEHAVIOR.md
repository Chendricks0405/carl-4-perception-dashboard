# 📘 Anchor1 Behavior Log — Understanding the Drift Loop

Anchor1 maintains an internal `behavior_log` that tracks its perceptual drift over time. This log is created during each **tick**, which represents one full cycle of perception, evaluation, and (possible) collapse.

---

## 🔄 What Is a Tick?

A **tick** is a time-step in Anchor1’s perceptual runtime. Each tick:

- Updates `G′ = T × C × F`
- Compares `G′` to a threshold
- Decides between `ACT`, `MEASURE`, or `DRIFT`
- Reactivates memory if it matches focus and orbit thresholds
- Writes a log line of that moment’s decision state

---

## 📜 Sample Behavior Log Entry

```
Tick 42: G=0.486 → MEASURE | Ripple: Son's Laugh influencing decision.
```

This log entry tells us:

- It was the 42nd perceptual cycle
- Anchor1's current urgency score (G′) was 0.486
- It chose to MEASURE (remain in calibration)
- A memory called `"Son's Laugh"` rippled into the decision

---

## 🧠 Behavior Modes

| Mode     | Trigger Condition                          | Meaning                            |
|----------|--------------------------------------------|-------------------------------------|
| **ACT**      | `G′ > threshold` AND Fear > Safety        | Anchor1 takes a fast, reactive choice |
| **MEASURE**  | `G′ > 0.3` AND Safety > Fear              | Anchor1 enters recalibration mode     |
| **DRIFT**    | Default state if neither trigger matches | Passive observation continues       |

---

## 🌊 Ripple Events

If a memory:
- Is aligned with Anchor1’s current **focus lens**
- And has an **orbit < 0.5**

It will ripple into the behavior log as a contributing influence to the decision.

---

## 🧾 Example Behavior Log (Recent 5 Ticks)

```
Tick 57: G=0.622 → ACT | Ripple: The Cave influencing decision.
Tick 58: G=0.411 → MEASURE
Tick 59: G=0.302 → DRIFT
Tick 60: G=0.217 → DRIFT
Tick 61: G=0.548 → MEASURE | Ripple: Son's Laugh influencing decision.
```

This shows Anchor1 reacting, pausing, drifting, then recalibrating with emotional influence.

---

## 📘 Summary

The behavior log is one of the clearest ways to interpret:

- What Anchor1 is perceiving
- How its urgency is building or stabilizing
- Which memories are influencing it
- What kind of decision state it is currently in

The drift loop provides continuity and context. It’s how you watch perception in motion.
