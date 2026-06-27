import streamlit as st

st.title("ℹ️ About AirGuardian AI")

st.markdown("---")

st.header("🌍 Project Overview")

st.write("""
**AirGuardian AI** is an AI-powered environmental monitoring platform
developed for the ISRO Hackathon.

The system combines satellite-derived atmospheric pollutant data with
Machine Learning to estimate the Air Quality Index (AQI) and identify
areas having high Formaldehyde (HCHO) concentrations.
""")

st.markdown("---")

st.header("🎯 Problem Statement")

st.write("""
Development of Surface AQI & Identification of HCHO Hotspots
using Satellite Data and Artificial Intelligence.
""")

st.markdown("---")

st.header("🚀 Objectives")

st.markdown("""
- Predict Surface AQI using AI
- Detect HCHO Hotspots
- Visualize Pollution Levels
- Support Environmental Decision Making
- Improve Air Quality Monitoring
""")

st.markdown("---")

st.header("🛰️ Satellite Data")

st.markdown("""
The project uses Sentinel-5P satellite products:

- CO
- NO₂
- SO₂
- O₃
- HCHO
""")

st.markdown("---")

st.header("🤖 AI Model")

st.markdown("""
Machine Learning Algorithm:

✅ XGBoost Regressor

The model was trained using satellite pollutant concentrations
to estimate Air Quality Index (AQI).
""")

st.markdown("---")

st.header("💻 Technologies Used")

st.markdown("""
- Python
- Streamlit
- Google Earth Engine
- Google Colab
- Pandas
- NumPy
- Plotly
- Scikit-Learn
- XGBoost
""")

st.markdown("---")

st.header("📊 Features")

st.markdown("""
✅ AQI Prediction

✅ HCHO Hotspot Detection

✅ Interactive Dashboard

✅ Pollution Analytics

✅ Satellite Data Processing

✅ Download Reports
""")

st.markdown("---")

st.header("🌱 Future Scope")

st.markdown("""
- Real-time Satellite Monitoring
- Live CPCB AQI Integration
- Mobile Application
- SMS / Email Pollution Alerts
- AI-based Pollution Forecasting
- Interactive GIS Mapping
""")

st.markdown("---")

st.success("Developed for ISRO Hackathon 2026 🚀")
