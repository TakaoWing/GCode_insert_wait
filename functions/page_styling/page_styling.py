import streamlit as st


def load_css_from_file(file_path: str) -> str:
    """
    指定されたファイルパスからCSSを読み込み、HTMLに変換する。

    Parameters
    ----------
    file_path : str
        読み込むCSSファイルのパス。

    Returns
    -------
    str
        HTMLに変換されたCSS。
    """
    with open(file_path, "r") as f:
        css = f.read()
    return f"<style>{css}</style>"


def set_custom_css(file_path: str) -> None:
    """
    指定されたファイルパスのCSSを読み込み、Streamlitのページに適用する。

    Parameters
    ----------
    file_path : str
        適用するCSSファイルのパス。

    Returns
    -------
    None
    """
    css = load_css_from_file(file_path)
    st.markdown(css, unsafe_allow_html=True)
