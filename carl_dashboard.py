import streamlit as st

st.title("🧠 Carl 4.0 — Perception Dashboard")
st.subheader("Anchor Vector ⟨F, S, T, C⟩ | WHY Scalar | Collapse Risk")

# Anchor Vector Sliders
st.sidebar.header("Adjust Anchor Values")
fear = st.sidebar.slider("Fear", 0.0, 1.0, 0.42)
safety = st.sidebar.slider("Safety", 0.0, 1.0, 0.55)
time = st.sidebar.slider("Time", 0.0, 1.0, 0.31)
choice = st.sidebar.slider("Choice", 0.0, 1.0, 0.38)

# WHY Scalar
why = round(time * choice, 4)

# Collapse Status Logic
def collapse_status(fear, safety, why):
    if why > 0.25 and fear > 0.8:
        return "⚫ Decoherence", "black"
    elif why > 0.15 and fear > 0.6:
        return "🔴 Collapse Risk", "red"
    elif why > 0.10:
        return "🟡 Drifting", "orange"
    else:
        return "🟢 Stable", "green"

status, color = collapse_status(fear, safety, why)

# Display Metrics
st.metric(label="WHY Scalar (W = T × C)", value=why)
st.markdown(f"### Collapse State: <span style='color:{color}'>{status}</span>", unsafe_allow_html=True)

st.write("### Anchor Vector")
st.write({
    "Fear": fear,
    "Safety": safety,
    "Time": time,
    "Choice": choice
})

# Ripple Triggers
st.write("### Trigger Events")
if st.button("🌩️ Storm Begins"):
    fear += 0.15
    safety -= 0.2
    time += 0.25
    choice -= 0.1
    st.experimental_rerun()

if st.button("❤️ Mira Appears"):
    fear -= 0.2
    safety += 0.25
    choice += 0.15
    st.experimental_rerun()

if st.button("🗣️ Player says 'Where’s the dungeon?'"):
    fear += 0.3
    time += 0.2
    choice += 0.2
    st.experimental_rerun()