# ------------------------------------ IMPORTS ------------------------------------
import streamlit as st
import pandas as pd


# ------------------------------------ IMPORTS ------------------------------------
st.title(":clipboard: CSV Viewer")

st.divider()

st.subheader(':gray[Choose a CSV file:]')
uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False, label_visibility='collapsed')

# If a file was submitted, check that it is a CSV file
if uploaded_file:
    if uploaded_file.type != 'text/csv':
        st.error('Please upload a CSV file format.', icon="🚨")
    else:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)