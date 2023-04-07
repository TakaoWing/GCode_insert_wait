import streamlit as st


def upload_file():
    uploaded_file = st.file_uploader("Choose a file", type=["gcode"])
    return uploaded_file


def get_gcode_data(file):
    if file is not None:
        gcode_data = file.read().decode("utf-8")
        return gcode_data
    else:
        return None
