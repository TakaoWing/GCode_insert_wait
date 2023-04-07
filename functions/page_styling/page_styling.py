import streamlit as st

def load_css_from_file(file_path):
    with open(file_path, "r") as f:
        css = f.read()
    return f"<style>{css}</style>"

def custom_css():
    css = load_css_from_file("style.css")
    st.markdown(css, unsafe_allow_html=True)