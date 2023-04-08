import streamlit as st


def upload_file()-> object:
    """
    ファイルのアップロードを行う関数。

    Returns:
        file (BytesIO): アップロードされたファイル。
    """
    uploaded_file = st.file_uploader("Choose a file", type=["gcode"])
    return uploaded_file


def get_gcode_data(file) -> str:
    """
    アップロードされたファイルから、G-codeデータを取得する関数。

    Args:
        file (BytesIO): アップロードされたファイル。

    Returns:
        gcode_data (str): G-codeデータ。
    """
    if file is not None:
        gcode_data = file.read().decode("utf-8")
        return gcode_data
    else:
        return None
