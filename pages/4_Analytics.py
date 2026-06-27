import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Analytics", page_icon="📊")

st.title("📊 AirGuardianAI Analytics Dashboard")

if not os.path.exists("history.csv"):
    st.warning("No prediction history found.")
    st.stop()

df = pd.read_csv("history.csv")

st.subheader("Prediction History")
st.dataframe(df, use_container_width=True)

# ------------------------
# AQI Trend
# ------------------------

st.subheader("📈 AQI Trend")

fig = px.line(
    df,
    x="Date",
    y="AQI",
    color="State",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------
# HCHO Trend
# ------------------------

st.subheader("🌫 HCHO Trend")

fig = px.line(
    df,
    x="Date",
    y="HCHO",
    color="State",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------
# AQI vs HCHO
# ------------------------

st.subheader("📊 AQI vs HCHO")
df = df.dropna(subset=["AQI", "HCHO"])
fig = px.scatter(
    df,
    x="HCHO",
    y="AQI",
    color="State",
    hover_data=["Date"]
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------
# Average AQI
# ------------------------

st.subheader("📍 Average AQI by State")

fig = px.bar(
    df.groupby("State", as_index=False)["AQI"].mean(),
    x="State",
    y="AQI",
    color="AQI"
)

st.plotly_chart(fig, use_container_width=True)