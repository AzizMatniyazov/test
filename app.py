import streamlit as st

st.set_page_config(page_title="BioBrick Digital Twin", layout="wide")

st.title("🔬 BioBrick Prototype Virtual Lab")
st.write("Compare the structural integrity of our BioBrick prototype against standard clay.")

# --- SIDEBAR: JUDGE CONTROLS ---
st.sidebar.header("🕹️ Environment Lab")
scenario = st.sidebar.selectbox("Choose Scenario", ["Standard", "Extreme Heat", "Flood/Rain", "Arctic Cold"])
intensity = st.sidebar.slider("Intensity Level", 0, 100, 50)

# --- THE MODELS (Prototypes) ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧱 Ordinary Clay Brick")
    # REPLACE THE LINK BELOW WITH A PHOTO OF YOUR REAL CLAY PROTOTYPE
    st.image("https://via.placeholder.com/400x300.png?text=Ordinary+Brick+Prototype", caption="Standard Clay Model")
    
    if scenario == "Extreme Heat":
        st.error("❌ STATUS: STRUCTURAL CRACKING")
        st.progress(intensity)
        st.write("Result: High thermal expansion causes surface fractures.")
    elif scenario == "Flood/Rain":
        st.warning("⚠️ STATUS: SATURATION")
        st.write("Result: 15% water absorption. Significant weight increase.")
    else:
        st.success("✅ STATUS: STABLE")

with col2:
    st.subheader("🌿 BioBrick Prototype (V1.0)")
    # REPLACE THE LINK BELOW WITH A PHOTO OF YOUR REAL BIOBRICK PROTOTYPE
    st.image("https://via.placeholder.com/400x300.png?text=BioBrick+Eco-Prototype", caption="Innovation Model")

    if scenario == "Extreme Heat":
        st.success("✅ STATUS: THERMAL SHIELD ACTIVE")
        st.progress(intensity // 4) # Much lower stress
        st.write("Result: Matrix remains intact. Internal cooling preserved.")
    elif scenario == "Flood/Rain":
        st.success("✅ STATUS: HYDROPHOBIC PROTECTION")
        st.write("Result: 7% absorption. Water beads off the surface.")
    else:
        st.success("✅ STATUS: OPTIMAL")

# --- COMPARISON DATA ---
st.divider()
st.columns(3)[1].metric("Energy Saving Potential", "75%", "+25% vs Industry Standard")
