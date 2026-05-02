import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Page config
st.set_page_config(
    page_title="Engineering Validator Pro",
    page_icon="⚙️",
    layout="wide"
)

# ===== HEADER =====
st.title("⚙️ Engineering Heat Transfer Dashboard")
st.caption("Built by EBUBECHUKWU David | Mechanical Engineer")
st.markdown("🔗 [View Source Code](https://github.com/gdave1/engineering-validator-dashboard)")
st.markdown("Validate and analyze heat transfer using engineering principles.")

# ===== SIDEBAR =====
st.sidebar.header("🔧 Input Parameters")

k = st.sidebar.number_input("Thermal Conductivity (W/mK)", value=200.0)
A = st.sidebar.number_input("Area (m²)", value=0.5)
T1 = st.sidebar.number_input("Hot Temperature (°C)", value=100.0)
T2 = st.sidebar.number_input("Cold Temperature (°C)", value=30.0)
L = st.sidebar.number_input("Thickness (m)", value=0.02)

# ===== VALIDATION =====
errors = []
if k <= 0:
    errors.append("Thermal conductivity must be positive")
if A <= 0:
    errors.append("Area must be positive")
if L <= 0:
    errors.append("Thickness must be positive")

if errors:
    st.error("❌ Input Errors:")
    for e in errors:
        st.write("-", e)
else:
    # ===== CALCULATION =====
    Q = k * A * (T1 - T2) / L


 # ===== DOWNLOAD RESULTS =====
data = {
    "Parameter": ["k", "A", "T1", "T2", "L", "Q"],
    "Value": [k, A, T1, T2, L, Q]
}

df = pd.DataFrame(data)

st.download_button(
    label="📥 Download Results",
    data=df.to_csv(index=False),
    file_name="engineering_results.csv",
    mime="text/csv"
)

    # ===== METRICS (TOP CARDS) =====
    col1, col2, col3 = st.columns(3)

    col1.metric("Heat Transfer (W)", f"{Q:.2f}")
    col2.metric("Temperature Difference (°C)", f"{T1 - T2:.2f}")
    col3.metric("Thermal Gradient", f"{(T1 - T2)/L:.2f}")

    st.divider()

    # ===== MAIN CONTENT =====
    col_left, col_right = st.columns([2, 1])

    # ----- LEFT: GRAPH -----
    with col_left:
        st.subheader("📊 Heat Transfer Analysis")

        temps = np.linspace(T2, T1 + 50, 30)
        Q_values = [k * A * (temp - T2) / L for temp in temps]

        fig, ax = plt.subplots()
        ax.plot(temps, Q_values)
        ax.set_xlabel("Hot Temperature (°C)")
        ax.set_ylabel("Heat Transfer (W)")
        ax.set_title("Heat Transfer vs Temperature")
        ax.grid()

        st.pyplot(fig)

    # ----- RIGHT: INSIGHTS -----
    with col_right:
        st.subheader("🧠 Insights")

        if Q > 0:
            st.success("Heat flows from hot side to cold side")
        else:
            st.warning("Unexpected heat flow direction")

        st.markdown("### ⚠️ Warnings")

        if abs(Q) > 1e6:
            st.write("- Heat transfer unusually high")
        if T1 == T2:
            st.write("- No temperature difference")

        st.markdown("### 📌 Assumptions")
        st.write("- Steady-state")
        st.write("- 1D conduction")
        st.write("- No heat loss")

    st.divider()

    # ===== EXPANDABLE DETAILS =====
    with st.expander("🔍 Detailed Engineering Output"):
        st.write(f"Thermal Conductivity: {k}")
        st.write(f"Area: {A}")
        st.write(f"Thickness: {L}")
        st.write(f"T1: {T1} °C")
        st.write(f"T2: {T2} °C")
        st.write(f"Calculated Heat Transfer: {Q:.2f} W")


 # ===== ABOUT THIS TOOL =====
with st.expander("ℹ️ About This Tool"):
    st.write("""
    This application validates engineering heat transfer calculations using Python.

    Features:
    - Heat transfer computation (Fourier’s Law)
    - Input and constraint validation
    - Engineering assumption analysis
    - Graphical visualization of system behavior

    Designed to demonstrate engineering reasoning and computational validation.
    """)
