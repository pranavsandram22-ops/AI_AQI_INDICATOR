import streamlit as st
import ee
from datetime import date

st.set_page_config(page_title="HCHO Monitor", page_icon="🌫")

PROJECT_ID = "airguardian-ai"

if not ee.data.is_initialized():
    ee.Initialize(project=PROJECT_ID)

st.title("🌫 Live HCHO Monitoring")

state = st.selectbox(
    "Select State",
    ["Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh", "Telangana", "Maharashtra", "Gujarat", "Delhi"]
)

start_date = st.date_input("Start Date", value=date(2024,1,1))
end_date = st.date_input("End Date", value=date(2024,1,7))

state_bounds = {
    "Kerala":[74.85,8.18,77.58,12.79],
    "Tamil Nadu":[76.15,8.00,80.35,13.60],
    "Karnataka":[74.00,11.50,78.60,18.50],
    "Andhra Pradesh":[76.75,12.60,84.75,19.20],
    "Telangana":[77.20,15.80,81.00,19.90],
    "Maharashtra":[72.50,15.60,80.90,22.10],
    "Gujarat":[68.10,20.10,74.50,24.70],
    "Delhi":[76.84,28.40,77.35,28.88]
}

def fetch_hcho():

    region = ee.Geometry.Rectangle(state_bounds[state])

    image = (
        ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_HCHO")
        .select("tropospheric_HCHO_column_number_density")
        .filterDate(
            start_date.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d")
        )
        .mean()
    )

    value = image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=region,
        scale=10000,
        maxPixels=1e9
    ).getInfo()

    return value["tropospheric_HCHO_column_number_density"]

if st.button("🌫 Get Live HCHO"):

    with st.spinner("Fetching HCHO from Sentinel-5P..."):

        hcho = fetch_hcho()

    st.success("Live HCHO Retrieved Successfully")

    st.metric(
        "HCHO Concentration",
        f"{hcho:.8f} mol/m²"
    )

    if hcho < 0.0001:
        st.success("🟢 Low HCHO")

    elif hcho < 0.0002:
        st.warning("🟡 Moderate HCHO")

    else:
        st.error("🔴 High HCHO")

    st.info("Source: Sentinel-5P Satellite (Google Earth Engine)")