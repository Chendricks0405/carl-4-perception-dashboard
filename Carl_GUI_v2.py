# Begin full rewrite of the GUI for Carl 5.0+ (v2) — Modular, ripple-aware, container-switching, memory-aware
import streamlit as st

# Initialize state if needed
if "core" not in st.session_state:
    st.session_state.core = {
        "Fear": 0.42,
        "Safety": 0.55,
        "Time": 0.31,
        "Choice": 0.38
    }
    st.session_state.goal = "Blend in socially"
    st.session_state.container = "Pub"
    st.session_state.W = round(st.session_state.core["Time"] * st.session_state.core["Choice"], 4)
    st.session_state.npc_log = []
    st.session_state.memory_log = []
    st.session_state.behavior_log = []
    st.session_state.beliefs = {
        "I am loyal": 1.0,
        "I am unattractive": 0.8,
        "I am dangerous": 0.9,
        "I am intelligent": 0.7
    }
    st.session_state.G_history = []

# Define containers
containers = {
    "Pub": {
        "goal": "Blend in socially",
        "distortions": {
            "Mira": {"Safety": 0.2, "Choice": 0.1},
            "Bran": {"Time": 0.2, "Fear": 0.2},
            "Steve": {"Fear": 0.3, "Choice": -0.2}
        }
    },
    "Blacksmith": {
        "goal": "Gain mastery and take over the smithy",
        "distortions": {
            "Orlin": {"Fear": -0.1, "Safety": 0.3, "Choice": 0.2}
        }
    },
    "Home": {
        "goal": "Rest and stabilize emotionally",
        "distortions": {}
    }
}

# Layout
st.set_page_config(layout="wide")
st.title("🧠 Carl 5.0 — Full Field GUI (v2)")
st.caption("Live simulation of memory-aware, goal-aligned perceptual drift")

# Sidebar — Core anchor vector with real-time update
st.sidebar.header("Core Perceptual Anchor (F/S/T/C)")
for var in ["Fear", "Safety", "Time", "Choice"]:
    st.session_state.core[var] = st.sidebar.slider(var, 0.0, 1.0, st.session_state.core[var], 0.01)

# Calculate G
G = round(st.session_state.core["Time"] * st.session_state.core["Choice"], 4)
st.session_state.W = G
st.session_state.G_history.append(G)

# Act/Measure/Wait logic
if G > 0.6 and st.session_state.core["Fear"] > st.session_state.core["Safety"]:
    decision = "ACT"
elif G > 0.3 and st.session_state.core["Safety"] > st.session_state.core["Fear"]:
    decision = "MEASURE"
else:
    decision = "WAIT"

# Top Row
top_left, top_mid, top_right = st.columns([2, 2, 2])
with top_left:
    st.subheader("📊 Current Core State")
    st.metric("G = T × C", G)
    st.metric("State:", decision)
    st.metric("Active Container", st.session_state.container)
    st.markdown(f"**Goal:** {containers[st.session_state.container]['goal']}")

with top_mid:
    st.subheader("📦 Memory Field (Cache)")
    if st.session_state.memory_log:
        for m in st.session_state.memory_log[-3:]:
            st.markdown(f"- {m}")
    else:
        st.info("No active memory cache entries.")

with top_right:
    st.subheader("🧠 Self-Perception Beliefs")
    for belief, weight in st.session_state.beliefs.items():
        st.markdown(f"**{belief}**: {round(weight, 2)}")

# Container Switcher
st.subheader("🌍 Environment")
container_choice = st.selectbox("Switch Container", list(containers.keys()))
if container_choice != st.session_state.container:
    st.session_state.container = container_choice
    st.session_state.goal = containers[container_choice]["goal"]
    st.session_state.behavior_log.append(f"Switched to {container_choice}")

# NPC Toggles — Apply ripple on toggle
st.subheader("👥 NPC Influence")
for npc in containers[st.session_state.container]["distortions"].keys():
    if st.checkbox(f"{npc} Nearby"):
        ripple = containers[st.session_state.container]["distortions"][npc]
        for var, delta in ripple.items():
            st.session_state.core[var] = max(0.0, min(1.0, st.session_state.core[var] + delta))
        st.session_state.npc_log.append(f"{npc} modified Carl via distortion field.")

# Physical Reflection
st.subheader("🦿 Physical Response")
if G > 0.6:
    st.warning("⚠️ Movement hesitant — goal pressure high")
elif G < 0.2:
    st.success("✅ Movement fluid — stability regained")
else:
    st.info("🟡 Neutral stance — observing field")

# Impact Button
if st.button("🧭 Carl says: 'Impact'"):
    st.session_state.core["Fear"] = max(st.session_state.core["Fear"] - 0.1, 0.0)
    st.session_state.core["Safety"] = min(st.session_state.core["Safety"] + 0.1, 1.0)
    st.session_state.core["Choice"] = min(st.session_state.core["Choice"] + 0.2, 1.0)
    st.session_state.behavior_log.append("Carl recalibrated via Impact.")

# Behavior Log
st.subheader("🧾 Behavior Log")
for b in st.session_state.behavior_log[-5:]:
    st.markdown(f"- {b}")