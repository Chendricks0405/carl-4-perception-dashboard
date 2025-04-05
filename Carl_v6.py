# Re-run the finalized clean core logic after environment reset
import streamlit as st

# Initialize AnchorOS Engine core state
if "core" not in st.session_state:
    st.session_state.core = {
        "Fear": 0.42,
        "Safety": 0.55,
        "Time": 0.31,
        "Choice": 0.38
    }
    st.session_state.focus = "Social"
    st.session_state.container = "Pub"
    st.session_state.goal = "Blend in socially"
    st.session_state.beliefs = {
        "I am loyal": 1.0,
        "I am unattractive": 0.8,
        "I am dangerous": 0.9,
        "I am intelligent": 0.7
    }
    st.session_state.memory_orbit = [
        {"id": "The Cave", "EQ": 0.8, "orbit": 0.3, "tier": "active", "focus_lens": ["Physical", "Emotional"]},
        {"id": "Son's Laugh", "EQ": 0.6, "orbit": 0.6, "tier": "cache", "focus_lens": ["Emotional"]},
        {"id": "Bran Joke", "EQ": 0.3, "orbit": 0.9, "tier": "archive", "focus_lens": ["Social"]}
    ]
    st.session_state.container_links = {
        "Pub": {"Home": 0.5, "Smithy": 0.4},
        "Home": {"Pub": 0.3, "Smithy": 0.6},
        "Smithy": {"Home": 0.7, "Pub": 0.3}
    }
    st.session_state.G_history = []
    st.session_state.behavior_log = []
    st.session_state.ticks = 0

focus_scalar_map = {"Physical": 1.2, "Emotional": 1.4, "Social": 1.6, "Multi": 2.0}

def run_drift_tick():
    st.session_state.ticks += 1
    T = st.session_state.core["Time"]
    C = st.session_state.core["Choice"]
    F = focus_scalar_map[st.session_state.focus]
    G = round(T * C * F, 4)
    st.session_state.G_history.append(G)

    ego_resistance = sum(w for w in st.session_state.beliefs.values() if w > 0.7)
    G_threshold = 0.6 + (ego_resistance * 0.1)

    if G > G_threshold and st.session_state.core["Fear"] > st.session_state.core["Safety"]:
        decision = "ACT"
    elif G > 0.3 and st.session_state.core["Safety"] > st.session_state.core["Fear"]:
        decision = "MEASURE"
    else:
        decision = "DRIFT"

    ripple_events = []
    for mem in st.session_state.memory_orbit:
        if st.session_state.focus in mem["focus_lens"] and mem["orbit"] < 0.5:
            ripple_events.append(f"{mem['id']} influencing decision.")

    behavior = f"Tick {st.session_state.ticks}: G={G} → {decision}"
    if ripple_events:
        behavior += f" | Ripple: {'; '.join(ripple_events)}"
    st.session_state.behavior_log.append(behavior)

st.set_page_config(layout="wide")
st.title("🧠 Carl 5.0 — AnchorOS Engine v1.0")
st.caption("Runtime drift with focus lensing, memory orbit, ego resistance, and container inertia")

st.sidebar.header("Anchor Core")
for k in st.session_state.core:
    st.session_state.core[k] = st.sidebar.slider(k, 0.0, 1.0, st.session_state.core[k], 0.01)

st.sidebar.header("Focus Lens")
st.session_state.focus = st.sidebar.radio("Select Lens:", list(focus_scalar_map.keys()))

st.sidebar.header("Container")
next_container = st.sidebar.selectbox("Switch Container:", list(st.session_state.container_links[st.session_state.container].keys()))
if next_container and next_container != st.session_state.container:
    inertia = st.session_state.container_links[st.session_state.container][next_container]
    st.session_state.core["Time"] += inertia * 0.1
    st.session_state.container = next_container
    st.session_state.goal = f"Adjusted for {next_container}"
    st.session_state.behavior_log.append(f"Moved to {next_container} with inertia modifier.")

if st.button("▶️ Run Drift Tick"):
    run_drift_tick()

col1, col2 = st.columns(2)
with col1:
    st.metric("Tick", st.session_state.ticks)
    st.metric("Focus", st.session_state.focus)
    st.metric("G′ (T × C × F)", st.session_state.G_history[-1] if st.session_state.G_history else 0.0)
    st.metric("Container", st.session_state.container)
    st.metric("Goal", st.session_state.goal)

with col2:
    st.subheader("Behavior Log")
    for b in st.session_state.behavior_log[-5:]:
        st.markdown(f"- {b}")

if st.button("🧭 Carl says: 'Impact'"):
    st.session_state.core["Fear"] = max(st.session_state.core["Fear"] - 0.1, 0.0)
    st.session_state.core["Safety"] = min(st.session_state.core["Safety"] + 0.1, 1.0)
    st.session_state.core["Choice"] = min(st.session_state.core["Choice"] + 0.2, 1.0)
    st.session_state.behavior_log.append(f"Tick {st.session_state.ticks}: Carl recalibrated (Impact).")