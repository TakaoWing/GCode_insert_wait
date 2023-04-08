import base64

def upload(st):
    """
    G-code ファイルをアップロードする。

    Returns
    -------
    file
        アップロードされたファイル。
    """
    uploaded_file = st.file_uploader("Choose a file", type=["gcode"])
    return uploaded_file

def create_download_link(gcode_data, filename):
    """
    Create a download link for the modified G-code.

    Parameters:
    gcode_data (str): The modified G-code.
    filename (str): The filename for the downloaded file.

    Returns:
    str: The HTML for the download link.
    """
    b64_gcode = base64.b64encode(gcode_data.encode())
    href = f'data:file/gcode;base64,{b64_gcode.decode()}'
    return f'<a class="download-button" href="{href}" download="{filename}">Download modified G-code</a>'