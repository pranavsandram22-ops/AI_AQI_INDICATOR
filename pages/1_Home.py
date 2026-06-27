import streamlit as st
import pandas as pd

# -------------------------
# Load Dataset
# -------------------------
data = pd.read_csv("Processed_AQI_Data.csv")

# -------------------------
# Page Title
# -------------------------
st.title("🌍 AirGuardian AI")
st.subheader("AI-Powered Surface AQI Prediction & HCHO Hotspot Detection")

st.markdown("---")

# -------------------------
# Calculate Statistics
# -------------------------
avg_aqi = round(data["AQI"].mean(), 2)
max_aqi = int(data["AQI"].max())
min_aqi = int(data["AQI"].min())
hotspots = len(data[data["Hotspot"] == "Hotspot"])

# -------------------------
# KPI Cards
# -------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("🌫 Average AQI", avg_aqi)
col2.metric("📈 Maximum AQI", max_aqi)
col3.metric("📉 Minimum AQI", min_aqi)
col4.metric("🔥 Hotspots", hotspots)

st.markdown("---")

# -------------------------
# Dataset Preview
# -------------------------
st.subheader("📄 Latest Satellite Data")

st.dataframe(data.head(10))

st.markdown("---")

# -------------------------
# Pollution Summary
# -------------------------
st.subheader("📊 Pollution Summary")

st.write(data[["CO","NO2","SO2","O3","HCHO"]].describe())

st.success("✅ AI Model Loaded Successfully")