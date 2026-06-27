import streamlit as st
import ee

ee.Initialize(project="airguardian-ai")

kerala = ee.Geometry.Rectangle([74.85, 8.18, 77.58, 12.79])

st.success("Geometry created successfully!")

collection = (
    ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_CO")
    .filterDate("2024-01-01", "2024-01-31")
    .mean()
)

value = collection.reduceRegion(
    reducer=ee.Reducer.mean(),
    geometry=kerala,
    scale=10000,
    maxPixels=1e9
)

st.write(value.getInfo())