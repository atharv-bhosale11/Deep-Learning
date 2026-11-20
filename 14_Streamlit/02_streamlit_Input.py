import streamlit as st

st.title("Deep Learning Codes by Atharv Bhosale")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}")
