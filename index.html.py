import streamlit as st
import math

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="NanoLab Digital Assistant", page_icon="🔬", layout="wide")

# --- TITLE ---
st.title("🔬 NanoLab: Advanced Analysis and Calculation Platform")
st.markdown("---")

# --- SIDEBAR ---
st.sidebar.header("🗂️ Analysis Modules")
choice = st.sidebar.radio(
    "Select Category:",
    [
        "🏠 Home", 
        "📏 Basic Conversions", 
        "🧪 Chemistry: Molarity & Solution", 
        "⚛️ Physics: Classical Mechanics",
        "🌡️ Thermodynamics & Gases",
        "🧲 Adsorption Isotherms",
        "🧬 Nanomaterials & XRD",
        "🌈 Analytical (HPLC & UV-Vis)"
    ]
)

# --- FUNCTIONS / MODULES ---

if choice == "🏠 Home":
    st.subheader("Welcome to the Laboratory & Engineering Assistant!")
    st.write("This comprehensive platform provides digital solutions across a wide spectrum, from fundamental physics to advanced materials science, chromatographic analysis, and surface adsorption kinetics.")
    st.info("Please select a module from the sidebar menu on the left to start working.")

elif choice == "📏 Basic Conversions":
    st.header("Unit and Dimension Converter")
    col1, col2 = st.columns(2)
    with col1:
        val = st.number_input("Value:", value=1.0)
        from_unit = st.selectbox("From:", ["Meter (m)", "Millimeter (mm)", "Micrometer (µm)", "Nanometer (nm)", "Angstrom (Å)"])
    with col2:
        to_unit = st.selectbox("To:", ["Meter (m)", "Millimeter (mm)", "Micrometer (µm)", "Nanometer (nm)", "Angstrom (Å)"])
    
    factors = {"Meter (m)": 1, "Millimeter (mm)": 1e-3, "Micrometer (µm)": 1e-6, "Nanometer (nm)": 1e-9, "Angstrom (Å)": 1e-10}
    if st.button("Convert"):
        result = val * (factors[from_unit] / factors[to_unit])
        st.success(f"Result: {result:.4e} {to_unit.split(' ')[0]}")

elif choice == "🧪 Chemistry: Molarity & Solution":
    st.header("Solution Preparation Kinetics")
    tab1, tab2 = st.tabs(["Molarity from Mass", "Dilution (C1V1 = C2V2)"])
    
    with tab1:
        m = st.number_input("Solute Mass (g):", min_value=0.0, format="%.4f")
        ma = st.number_input("Molecular Weight (g/mol):", min_value=0.0)
        v = st.number_input("Solution Volume (mL):", min_value=0.0)
        if st.button("Calculate Molarity") and ma > 0 and v > 0:
            res = (m / ma) / (v / 1000)
            st.metric("Result", f"{res:.6f} M")
            
    with tab2:
        c1 = st.number_input("Stock Concentration (C1):", min_value=0.0, key="c1")
        c2 = st.number_input("Target Concentration (C2):", min_value=0.0, key="c2")
        v2 = st.number_input("Target Volume (V2):", min_value=0.0, key="v2")
        if st.button("Calculate Required V1 Volume"):
            if c1 > 0:
                v1 = (c2 * v2) / c1
                st.metric("Required Stock Volume", f"{v1:.4f} Units")

elif choice == "⚛️ Physics: Classical Mechanics":
    st.header("Newtonian Mechanics and Kinematics")
    mod = st.selectbox("Select Operation:", ["Force & Acceleration (F = m·a)", "Kinetic Energy (Ek = 1/2 · m · v²)"])
    
    if mod == "Force & Acceleration (F = m·a)":
        m_mech = st.number_input("Mass (kg):", min_value=0.0)
        a_mech = st.number_input("Acceleration (m/s²):")
        if st.button("Calculate Force"):
            f = m_mech * a_mech
            st.success(f"Applied Force: {f:.2f} Newton")
            
    elif mod == "Kinetic Energy (Ek = 1/2 · m · v²)":
        m_ke = st.number_input("Mass (kg):", key="m_ke", min_value=0.0)
        v_ke = st.number_input("Velocity (m/s):", key="v_ke")
        if st.button("Calculate Energy"):
            ke = 0.5 * m_ke * (v_ke ** 2)
            st.success(f"Kinetic Energy: {ke:.2f} Joule")

elif choice == "🌡️ Thermodynamics & Gases":
    st.header("Ideal Gas Law (P·V = n·R·T)")
    st.write("R = 0.08206 L·atm/(mol·K)")
    
    p = st.number_input("Pressure (atm):", min_value=0.0)
    v_gas = st.number_input("Volume (Liter):", min_value=0.0)
    n = st.number_input("Amount of Substance (n - mol):", min_value=0.0)
    t_cel = st.number_input("Temperature (°C):")
    
    calc_target = st.selectbox("What do you want to calculate?", ["Pressure (P)", "Volume (V)", "Moles (n)", "Temperature (T)"])
    
    if st.button("Calculate Thermodynamics"):
        t_kelvin = t_cel + 273.15
        R = 0.08206
        if calc_target == "Pressure (P)" and v_gas > 0:
            st.info(f"Calculated Pressure: {(n * R * t_kelvin) / v_gas:.4f} atm")
        elif calc_target == "Volume (V)" and p > 0:
            st.info(f"Calculated Volume: {(n * R * t_kelvin) / p:.4f} Liter")
        elif calc_target == "Moles (n)" and t_kelvin > 0:
            st.info(f"Calculated Moles: {(p * v_gas) / (R * t_kelvin):.4f} mol")
        elif calc_target == "Temperature (T)" and n > 0:
            st.info(f"Calculated Temperature: {((p * v_gas) / (n * R)) - 273.15:.2f} °C")

elif choice == "🧲 Adsorption Isotherms":
    st.header("Surface Retention Kinetics")
    st.write("Ideal for heavy metal removal efficiency and nanocomposite performance testing.")
    tab_lang, tab_fre = st.tabs(["Langmuir Isotherm", "Freundlich Isotherm"])
    
    with tab_lang:
        st.latex(r"q_e = \frac{q_{max} \cdot K_L \cdot C_e}{1 + K_L \cdot C_e}")
        qmax = st.number_input("Maximum Adsorption Capacity (q_max) [mg/g]:", value=50.0)
        kl = st.number_input("Langmuir Constant (K_L) [L/mg]:", value=0.1)
        ce = st.number_input("Equilibrium Concentration (C_e) [mg/L]:", value=10.0)
        if st.button("Calculate q_e (Equilibrium Retention)"):
            qe = (qmax * kl * ce) / (1 + (kl * ce))
            st.success(f"Adsorbed Amount (q_e): {qe:.3f} mg/g")
            
    with tab_fre:
        st.latex(r"q_e = K_F \cdot C_e^{1/n}")
        kf = st.number_input("Freundlich Constant (K_F):", value=5.0)
        n_fre = st.number_input("Adsorption Intensity (n):", value=2.0)
        ce_fre = st.number_input("Equilibrium Concentration (C_e) [mg/L]:", key="ce_fre", value=10.0)
        if st.button("Calculate Freundlich q_e"):
            if n_fre != 0:
                qe_f = kf * (ce_fre ** (1/n_fre))
                st.success(f"Adsorbed Amount (q_e): {qe_f:.3f} mg/g")

elif choice == "🧬 Nanomaterials & XRD":
    st.header("Crystallography and Photonics")
    mod_nano = st.radio("Sub-Module:", ["Scherrer Equation (Crystallite Size)", "Bragg's Law (d-spacing)", "Photon Energy (E = h·c/λ)"])
    
    if mod_nano == "Scherrer Equation (Crystallite Size)":
        st.latex(r"D = \frac{K \cdot \lambda}{\beta \cdot \cos(\theta)}")
        wave = st.number_input("Wavelength (λ) nm:", value=0.15406)
        fwhm = st.number_input("FWHM (Radians - β):", format="%.5f", value=0.005)
        theta = st.number_input("Peak Angle (θ - Degrees):", value=15.0)
        k = st.number_input("Shape Factor (K Constant):", value=0.9)
        if st.button("Calculate Size") and fwhm > 0:
            d = (k * wave) / (fwhm * math.cos(math.radians(theta)))
            st.success(f"Crystallite Size (D): {d:.2f} nm")
            
    elif mod_nano == "Bragg's Law (d-spacing)":
        st.latex(r"n \cdot \lambda = 2d \cdot \sin(\theta)")
        n_bragg = st.number_input("Diffraction Order (n):", value=1)
        wave_b = st.number_input("Wavelength (λ) nm:", value=0.15406, key="wave_b")
        theta_b = st.number_input("Diffraction Angle (θ - Degrees):", value=15.0, key="theta_b")
        if st.button("Calculate d-spacing"):
            d_space = (n_bragg * wave_b) / (2 * math.sin(math.radians(theta_b)))
            st.success(f"Interplanar Spacing (d): {d_space:.4f} nm")
            
    elif mod_nano == "Photon Energy (E = h·c/λ)":
        wave_nm = st.number_input("Light Wavelength (nm):", min_value=1.0, value=500.0)
        if st.button("Calculate Energy"):
            h = 6.626e-34  
            c = 3e8        
            e_joule = (h * c) / (wave_nm * 1e-9)
            e_ev = e_joule / 1.602e-19
            st.info(f"Energy: {e_ev:.3f} eV  ({e_joule:.3e} Joule)")

elif choice == "🌈 Analytical (HPLC & UV-Vis)":
    st.header("Chromatography and Spectroscopy")
    tab_hplc, tab_uv = st.tabs(["HPLC Kinetics", "Beer-Lambert Law"])
    
    with tab_hplc:
        tr = st.number_input("Analyte Retention Time (tR):", min_value=0.0, value=5.0)
        t0 = st.number_input("Dead Time / Void Time (t0):", min_value=0.0, value=1.0)
        if st.button("Analyze Retention Factor"):
            if t0 > 0:
                k_prime = (tr - t0) / t0
                st.success(f"Retention Factor (k'): {k_prime:.3f}")
                
    with tab_uv:
        st.latex(r"A = \epsilon \cdot c \cdot l")
        a = st.number_input("Absorbance (A):", min_value=0.0)
        eps = st.number_input("Molar Absorptivity (ε):", value=10000.0)
        l = st.number_input("Cuvette Path Length (cm):", value=1.0)
        if st.button("Calculate Concentration"):
            if eps * l > 0:
                c_uv = a / (eps * l)
                st.info(f"Solution Concentration: {c_uv:.3e} Molar")

with st.sidebar:
    st.markdown("---")
    st.caption("NanoLab Digital Assistant v1.1")