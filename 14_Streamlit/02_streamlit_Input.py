import streamlit as st

st.title("Deep Learning by Atharv Bhosale")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}")
