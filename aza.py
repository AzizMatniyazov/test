import streamlit as st

# Page setup
st.set_page_config(page_title="BioBrick Simulation Lab", layout="wide")
st.title("🧱 BioBrick vs. Ordinary Brick: Stress Test Simulator")
st.write("Select environmental conditions below to see how the materials react.")

# --- CONTROL PANEL ---
st.sidebar.header("🕹️ Environment Controls")
temp = st.sidebar.slider("Outside Temperature (°C)", -30, 60, 20)
water_test = st.sidebar.checkbox("Apply Heavy Rain (Humidity)")
fire_test = st.sidebar.checkbox("Ignite Fire Test (High Heat)")

# --- CALCULATION LOGIC ---
# Thermal conductivity: BioBrick (0.25) vs Ordinary (0.6)
bio_inside = 22 - ((temp - 22) * 0.15)
ord_inside = 22 - ((temp - 22) * 0.45)

# --- SIMULATION DISPLAY ---
col1, col2 = st.columns(2)

# BIOBRICK SITUATION
with col1:
    st.header("🌿 BioBrick Situation")
    st.metric("Internal House Temp", f"{round(bio_inside, 1)}°C")
    
    # Fire Situation
    if fire_test:
        st.error("🔥 STATUS: HEAT RESISTANT")
        st.write("The biomass-plastic matrix carbonizes to form a protective layer. No structural collapse.")
    # Water Situation
    elif water_test:
        st.info("💧 STATUS: HYDROPHOBIC")
        st.write("Water absorption: **7%**. The brick remains dry and maintains strength.")
    # Temperature Situation
    else:
        if temp > 35: st.warning("☀️ STATUS: COOL INTERIOR. Reflects external heat.")
        elif temp < 0: st.snow() ; st.info("❄️ STATUS: WARM RETAINED. Prevents heat leak.")
        else: st.success("✅ STATUS: OPTIMAL. Energy saving active.")

# ORDINARY BRICK SITUATION
with col2:
    st.header("🧱 Ordinary Brick Situation")
    st.metric("Internal House Temp", f"{round(ord_inside, 1)}°C")
    
    # Fire Situation
    if fire_test:
        st.error("🔥 STATUS: THERMAL CRACKING")
        st.write("High heat causes rapid expansion. Micro-cracks appearing in the clay structure.")
    # Water Situation
    elif water_test:
        st.warning("💧 STATUS: SATURATED")
        st.write("Water absorption: **15%**. Heavy moisture increases weight and foundation load.")
    # Temperature Situation
    else:
        if temp > 35: st.error("☀️ STATUS: OVERHEATING. AC costs will increase.")
        elif temp < 0: st.snow() ; st.error("❄️ STATUS: HEAT LOSS. Rapid cooling inside.")
        else: st.success("✅ STATUS: STABLE. Standard performance.")

st.divider()
st.write("### 📊 Live Efficiency Comparison")
st.bar_chart({"BioBrick Efficiency": [85], "Ordinary Brick Efficiency": [40]})
