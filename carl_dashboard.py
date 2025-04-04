# Carl 5.0 Perceptual Engine GUI (streamlit)
import streamlit as st

# --- Persistent State Initialization ---
if "Fear" not in st.session_state:
    st.session_state.Fear = 0.42
    st.session_state.Safety = 0.55
    st.session_state.Time = 0.31
    st.session_state.Choice = 0.38
    st.session_state.W = round(st.session_state.Time * st.session_state.Choice, 4)
    st.session_state.Physical = {"mobility": "limited", "limitation": "missing eye"}
    st.session_state.Goal = "Take over the smithy as master ages out"
    st.session_state.AM_decision = "WAIT"
    st.session_state.memory_log = []
    st.session_state.npc_influence = []
    st.session_state.container = "Pub"
    st.session_state.behavior_log = []

st.set_page_config(layout="wide")
st.title("🧠 Carl 5.0 — Full Perceptual Engine GUI")
st.caption("Real-time cognitive simulation with memory, identity, drift, and goal pressure")

# --- Anchor Vector Sliders ---
st.sidebar.header("Core Anchor Vector (F/S/T/C)")
fear = st.sidebar.slider("Fear", 0.0, 1.0, st.session_state.Fear, 0.01,
                         help="Emotional instability or perceived threat")
safety = st.sidebar.slider("Safety", 0.0, 1.0, st.session_state.Safety, 0.01,
                           help="Sense of stability and internal calm")
time = st.sidebar.slider("Time", 0.0, 1.0, st.session_state.Time, 0.01,
                         help="Urgency or external pressure to act")
choice = st.sidebar.slider("Choice", 0.0, 1.0, st.session_state.Choice, 0.01,
                           help="Confidence or perceived freedom to act")

# --- Recalculate W (G = Goal Pressure) ---
G = round(time * choice, 4)
st.session_state.W = G

# --- A&M Gateway Logic ---
if G > 0.6 and fear > safety:
    am_decision = "ACT"
elif G > 0.3 and safety > fear:
    am_decision = "MEASURE"
else:
    am_decision = "WAIT"
st.session_state.AM_decision = am_decision

# --- Layout ---
left, right = st.columns([2, 2])
with left:
    st.subheader("🧭 Live Cognitive State")
    st.metric("Goal Pressure (G = T × C)", G)
    st.metric("A&M Gateway", st.session_state.AM_decision)
    st.metric("Container", st.session_state.container)
    st.markdown(f"**Goal:** {st.session_state.Goal}")
    st.markdown(f"**Physical Limitation:** {st.session_state.Physical['limitation']}")

    st.subheader("📦 Memory Cache")
    for mem in st.session_state.memory_log[-3:]:
        st.markdown(f"- {mem}")

    st.subheader("👣 Behavior Log")
    for b in st.session_state.behavior_log[-3:]:
        st.markdown(f"- {b}")

with right:
    st.subheader("👥 NPC Influence (Toggle Presence)")
    for npc in ["Mira", "Bran", "Steve", "Jessa", "Orlin"]:
        if st.checkbox(f"{npc} Nearby"):
            if npc not in st.session_state.npc_influence:
                st.session_state.npc_influence.append(npc)
            st.markdown(f"✅ {npc} is affecting Carl")
        else:
            if npc in st.session_state.npc_influence:
                st.session_state.npc_influence.remove(npc)

    st.subheader("🦿 Physical Container Status")
    if G > 0.6:
        st.markdown("⚠️ **Hesitant movement** detected (Goal pressure high)")
    elif G < 0.2:
        st.markdown("✅ **Fluid movement** — Carl is stable")
    else:
        st.markdown("🔄 **Neutral stance** — Monitoring")

# --- Impact Button ---
if st.button("🧭 Carl says: 'Impact' (Recalibrate)"):
    st.session_state.Fear = max(fear - 0.1, 0.0)
    st.session_state.Choice = min(choice + 0.2, 1.0)
    st.session_state.Safety = min(safety + 0.1, 1.0)
    st.session_state.behavior_log.append("Carl recalibrated via Impact.")

# --- Update Session Values ---
st.session_state.Fear = fear
st.session_state.Safety = safety
st.session_state.Time = time
st.session_state.Choice = choice