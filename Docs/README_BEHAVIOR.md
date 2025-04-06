# 📘 Carl’s Behavior Log — Understanding the Drift Loop

Carl maintains an internal `behavior_log` that tracks his perceptual drift over time. This log is created during each **tick**, which represents one full cycle of perception, evaluation, and (possible) collapse.

---

## 🔄 What Is a Tick?

A **tick** is a time-step in Carl’s perceptual runtime. Each tick:

1. Updates `G′ = T × C × F`
2. Compares `G′` to a threshold
3. Decides between `ACT`, `MEASURE`, or `DRIFT`
4. Reactivates memory if it matches focus and orbit thresholds
5. Writes a log line of that moment’s decision state

---

## 📜 Sample Behavior Log Entry

```
Tick 42: G=0.486 → MEASURE | Ripple: Son's Laugh influencing decision.
```

This log entry tells us:
- It was the 42nd perceptual cycle
- Carl's current urgency score (G′) was 0.486
- He chose to MEASURE (remain in calibration)
- A memory called `"Son's Laugh"` rippled into the decision

---

## 🧠 Behavior Modes

| Mode     | Trigger Condition                          | Meaning                            |
|----------|--------------------------------------------|-------------------------------------|
| **ACT**      | `G′ > threshold` AND Fear > Safety        | Carl takes a fast, reactive choice |
| **MEASURE**  | `G′ > 0.3` AND Safety > Fear              | Carl enters recalibration mode     |
| **DRIFT**    | Default state if neither trigger matches | Passive observation continues      |

---

## 🌊 Ripple Events

If a memory:
- Is aligned with Carl’s current **focus lens**
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

This shows Carl reacting, pausing, drifting, then recalibrating with emotional influence.

---

## 📘 Summary

The behavior log is one of the clearest ways to interpret:
- What Carl is perceiving
- How his urgency is building or stabilizing
- Which memories are influencing him
- What kind of decision state he is currently in

The drift loop provides continuity and context. It’s how you watch perception in motion.
