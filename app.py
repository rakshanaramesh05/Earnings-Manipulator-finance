import streamlit as st
import pandas as pd

st.title("My First Streamlit App")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)
