
# Anchor1 Memory Weighting Guide

This guide explicitly details how to create and structure memory nodes for effective integration with the Anchor1 Perception Engine. Properly weighted memories ensure accurate and adaptive recalibration of perceptual anchors.

## Understanding Memory Weighting

Anchor1 uses weighted memories to recalibrate anchor states (Risk, Growth, Engagement Timing, and Action Strategy). Each memory node consists of three key components:

1. **Orbit**: Determines memory influence strength (0.0 - high influence, 1.0 - low influence).
2. **Tier**: Indicates memory's active status (`"active"`, `"inactive"`).
3. **Data**: Contains specific contextual information and explicit anchor adjustments.

## Explicit Memory Structure

Here's a fully explained example of an explicitly weighted memory node:

```json
{
  "id": "high_engagement_post",
  "orbit": 0.1,
  "tier": "active",
  "data": {
    "description": "Highly successful TikTok post with strong engagement metrics.",
    "impact": {
      "Risk": -0.10,
      "Growth": 0.20,
      "Engagement Timing": 0.15,
      "Action Strategy": 0.10
    },
    "additional_info": {
      "optimal_times": ["12pm-2pm", "7pm-9pm"],
      "best_tags": ["#viral", "#fyp", "#trend"]
    }
  }
}
```

### Explanation of the Example

- **Orbit (0.1)**: Explicitly set for high immediate influence due to proven historical success.
- **Risk (-0.10)**: Reduces perceived risk of similar future content explicitly.
- **Growth (0.20)**: Explicitly boosts growth expectations based on proven performance.
- **Engagement Timing (0.15)**: Increases the anchor explicitly for optimal posting timing.
- **Action Strategy (0.10)**: Clearly enhances future content strategy confidence.

## Recommended Guidelines for Memory Creation

When creating memory nodes explicitly:

- Use lower orbit values (0.1-0.3) for memories proven to strongly influence outcomes.
- Assign higher orbit values (0.6-0.9) for background contextual information.
- Explicitly define anchor impacts according to historical success or failure metrics.
- Keep tier "active" for real-time recalibration influence.

## Integrating Memories into Anchor1

After defining your memories clearly and explicitly:

1. Save your structured memory nodes in JSON format.
2. Load the memory explicitly using AnchorAPI:

```python
from api_interface import AnchorAPI

api = AnchorAPI(session)
api.load_memory("path_to_memory.json")
```

3. Recalibrate anchor states explicitly by calling:

```python
api.run_tick(memory_node["data"]["impact"])
```

Following this explicit guide ensures your memories are optimally weighted, accurately influencing your Anchor1 adaptive recalibration process.

## Goal-Oriented Memory Example

### Example Goal:
"Increase TikTok follower growth by 20% this month."

Explicit memory reflecting past success:

```json
{
  "id": "successful_growth_event",
  "orbit": 0.1,
  "tier": "active",
  "data": {
    "description": "Previous successful growth campaign on TikTok.",
    "impact": {
      "Risk": -0.10,
      "Growth": 0.25,
      "Engagement Timing": 0.10,
      "Action Strategy": 0.15
    },
    "additional_info": {
      "optimal_tags": ["#growth", "#followers"],
      "optimal_times": ["6pm-8pm"]
    }
  }
}
```

Explicit recalibration towards the goal:

```python
goal_impact = memory_node["data"]["impact"]
api.run_tick(goal_impact)
```

This explicitly recalibrates your anchors, steering the system towards clearly defined and historically informed goal-oriented outcomes.
