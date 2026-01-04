import streamlit as st
import pandas as pd

st.set_page_config(page_title="Earnings Manipulator App")

st.title("Earnings Manipulation Analyzer")

st.write("App is running successfully 🎉")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(df)
