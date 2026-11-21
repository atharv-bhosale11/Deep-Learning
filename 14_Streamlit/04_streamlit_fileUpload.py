import streamlit as st

st.title("Welcome to My Hone Page")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success("PDF Uploaded Successfully")
 
