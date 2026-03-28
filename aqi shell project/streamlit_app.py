import streamlit as st
import pandas as pd

df = pd.read_csv("air_quality.csv")

st.title("Urban Air Quality Monitoring")

st.line_chart(df["pm2_5"])
st.line_chart(df["pm10"])

st.write("Air Quality Data")
st.dataframe(df)