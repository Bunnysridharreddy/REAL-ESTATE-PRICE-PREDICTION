
import streamlit as st
st.set_page_config(page_title="Real Estate Price Predictor", page_icon="⚡", layout="centered", initial_sidebar_state="expanded")
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Configure matplotlib fonts to avoid font warnings
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans', 'Bitstream Vera Sans', 'sans-serif']

# Define feature names for consistent use throughout the app
FEATURE_NAMES = ['transaction_year', 'house_age', 'distance_to_mrt', 'num_convenience_stores', 'latitude', 'longitude']


# ---------------------------
# Load custom CSS
# ---------------------------
def load_css():
    try:
        with open("app/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

def modern_hr():
    st.markdown('''
    <div style="text-align: center; margin: 2rem 0;">
        <div style="height: 2px; background: linear-gradient(90deg, transparent, #6366f1, #ec4899, #06b6d4, transparent); width: 100%; margin: 1rem 0; border-radius: 2px;"></div>
        <div style="display: inline-block; width: 8px; height: 8px; background: linear-gradient(135deg, #6366f1, #ec4899); border-radius: 50%; animation: dynamicPulse 3s infinite;"></div>
    </div>
    <style>
    @keyframes dynamicPulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        33% { opacity: 0.7; transform: scale(1.3); }
        66% { opacity: 0.9; transform: scale(1.1); }
    }
    </style>
    ''', unsafe_allow_html=True)

# ---------------------------
# Title and Intro
# ---------------------------
st.subheader(" Enter Property Details")

st.markdown("""
<div style='text-align: center; margin: 2rem 0;'>
    <div style='font-size: 3rem; font-weight: 800; margin-bottom: 0.5rem; font-family: "Montserrat", sans-serif; background: linear-gradient(135deg, #6366f1, #ec4899, #06b6d4); background-size: 200% 200%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: titleFlow 0.8s ease-out, gradientShift 4s ease-in-out infinite;'>
        Real Estate Price Predictor
    </div>
    <div style='font-size: 1.2rem; color: #cbd5e1; font-weight: 500; font-family: "Source Sans Pro", sans-serif; letter-spacing: 0.5px; margin-bottom: 1rem; text-transform: uppercase;'>
        Advanced Machine Learning Property Valuation System
    </div>
</div>
<style>
@keyframes titleFlow {
    from { opacity: 0; transform: translateY(30px) scale(0.95); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}
</style>
""", unsafe_allow_html=True)

modern_hr()

st.markdown("""
<div style='text-align: center; font-size: 1.8rem; font-weight: 700; color: #6366f1; margin: 1.5rem 0; font-family: "Montserrat", sans-serif; letter-spacing: 0.5px; text-transform: uppercase;'>
    Property Configuration
</div>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar - User Guide
# ---------------------------

with st.sidebar:
    st.markdown("""
    <div style='text-align: center; font-size: 2rem; font-weight: 800; color: #6366f1; margin-bottom: 1.5rem; font-family: "Montserrat", sans-serif; letter-spacing: 0.5px; text-transform: uppercase;'>
        User Guide
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: rgba(99, 102, 241, 0.15); padding: 1.4rem; border-radius: 18px; border: 1px solid rgba(99, 102, 241, 0.4); margin-bottom: 1rem; backdrop-filter: blur(15px);'>
        <div style='color: #6366f1; font-size: 1.2rem; margin-bottom: 0.8rem; font-family: "Montserrat", sans-serif; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;'><strong>How to Use:</strong></div>
        <ol style='color: #f1f5f9; font-size: 1rem; line-height: 1.8; font-family: "Source Sans Pro", sans-serif; font-weight: 500;'>
            <li> Note: This model is trained on Taiwan real estate data. Predictions and price units (NT/ping) are specific to the Taiwan market</li>
            <li>Enter property details in the form</li>
            <li>Click "Predict Price" to get valuation</li>
            <li>Review the predicted price result</li>
            <li>Analyze feature importance chart</li>
        </ol>   
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: rgba(236, 72, 153, 0.15); padding: 1.4rem; border-radius: 18px; border: 1px solid rgba(236, 72, 153, 0.4); backdrop-filter: blur(15px);'>
        <div style='color: #ec4899; font-size: 1.2rem; margin-bottom: 0.8rem; font-family: "Montserrat", sans-serif; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;'><strong>Input Parameters:</strong></div>
        <ul style='color: #f1f5f9; font-size: 1rem; line-height: 1.8; list-style-type: none; padding-left: 0; font-family: "Source Sans Pro", sans-serif; font-weight: 500;'>
            <li>• Transaction Year</li>
            <li>• Property Age</li>
            <li>• MRT Distance (meters)</li>
            <li>• Convenience Store Count</li>
            <li>• Latitude & Longitude</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("Algorithm: Optimized Random Forest Model", icon="⚡")

# ---------------------------
# Input Fields
# ---------------------------

col1, col2 = st.columns(2)
with col1:
    transaction_year = st.selectbox("Transaction Year", [2012, 2013])
    house_age = st.slider("House Age (Years)", 0, 50, 10)
    num_convenience_stores = st.slider("Number of Convenience Stores", 0, 20, 5)
with col2:
    distance_to_mrt = st.number_input("Distance to MRT (meters)", min_value=0.0, value=500.0)
    latitude = st.number_input("Latitude", value=24.96, format="%.6f")
    longitude = st.number_input("Longitude", value=121.54, format="%.6f")

# ---------------------------
# Load the trained model
# ---------------------------
@st.cache_resource
def load_model():
    return joblib.load("models/final_model.pkl")

@st.cache_resource
def load_scaler():
    return joblib.load("models/scaler.pkl")

model = load_model()
scaler = load_scaler()

# ---------------------------
# Prediction
# ---------------------------

modern_hr()

predict_btn = st.button("Predict Price", use_container_width=True)
if predict_btn:
    if distance_to_mrt < 0:
        st.error("ERROR: Invalid MRT distance parameter")
    else:
        # Prepare input data with proper feature names (matching training data)
        input_data = pd.DataFrame([[transaction_year, house_age, distance_to_mrt, num_convenience_stores, latitude, longitude]], 
                                columns=FEATURE_NAMES)
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)
        st.success(f"Prediction Complete: ${prediction[0]:,.2f} NT$/ping")
        st.markdown(f"""
        <div style='text-align: center; margin: 2rem 0; padding: 2.5rem; background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(236, 72, 153, 0.15)); border-radius: 20px; border: 1px solid rgba(99, 102, 241, 0.4); backdrop-filter: blur(20px); animation: resultPulse 2s ease-in-out infinite alternate;'>
            <div style='font-size: 1.1rem; color: #cbd5e1; margin-bottom: 0.8rem; font-family: "Montserrat", sans-serif; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;'>Predicted Value</div>
            <div style='font-size: 2.8rem; background: linear-gradient(135deg, #6366f1, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 900; font-family: "Montserrat", sans-serif;'>{prediction[0]:,.2f}</div>
            <div style='font-size: 1rem; color: #94a3b8; font-family: "Source Sans Pro", sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;'>NT$ per unit area</div>
        </div>
        <style>
        @keyframes resultPulse {{
            0% {{ box-shadow: 0 0 20px rgba(99, 102, 241, 0.3); }}
            100% {{ box-shadow: 0 0 40px rgba(236, 72, 153, 0.4), 0 0 60px rgba(99, 102, 241, 0.2); }}
        }}
        </style>
        """, unsafe_allow_html=True)

        
# ---------------------------
# Feature Importance Plot
# ---------------------------

modern_hr()
st.markdown("""
<div style='text-align: center; font-size: 1.6rem; font-weight: 700; color: #6366f1; margin: 1.5rem 0; font-family: "Montserrat", sans-serif; text-transform: uppercase; letter-spacing: 0.5px;'>
    Feature Importance Analysis
</div>
""", unsafe_allow_html=True)
try:
    importances = model.feature_importances_
    if len(importances) != len(FEATURE_NAMES):
        st.warning(f"Matrix dimension mismatch: {len(FEATURE_NAMES)} vs {len(importances)}")
    else:
        importance_df = pd.DataFrame({'Feature': FEATURE_NAMES, 'Importance': importances}).sort_values(by='Importance', ascending=True)
        
        # Create modern dynamic plot
        fig, ax = plt.subplots(figsize=(12, 7))
        fig.patch.set_facecolor('none')
        ax.set_facecolor('#1a1a2e')
        
        # Dynamic gradient colors
        colors = ['#6366f1', '#8b5cf6', '#ec4899', '#f97316', '#06b6d4', '#10b981']
        bars = ax.barh(importance_df['Feature'], importance_df['Importance'], color=colors)
        
        # Enhanced styling
        for i, bar in enumerate(bars):
            bar.set_edgecolor('#ffffff')
            bar.set_linewidth(1)
            # Add gradient effect
            bar.set_alpha(0.9)
        
        ax.set_xlabel("Importance Score", fontsize=14, color='#f1f5f9', fontfamily='sans-serif', fontweight='600')
        ax.set_title("Feature Importance Analysis", fontsize=18, color='#f1f5f9', 
                    fontweight='800', fontfamily='sans-serif', pad=25)
        
        # Modern clean styling
        ax.tick_params(colors='#e2e8f0', labelsize=11)
        for spine in ax.spines.values():
            spine.set_color('#64748b')
            spine.set_linewidth(1)
        ax.grid(True, alpha=0.4, color='#64748b', linestyle='--', linewidth=0.8)
        
        plt.tight_layout()
        st.pyplot(fig, transparent=True)
except AttributeError:
    st.info("Feature importance analysis unavailable for current model type")
