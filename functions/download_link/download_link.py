from io import BytesIO
import base64


def create_download_link(gcode_data, filename):
    """ダウンロードリンクを生成する"""
    b64_gcode = base64.b64encode(gcode_data.encode()).decode()
    return f'<a class="download-button" href="data:file/gcode;base64,{b64_gcode}" download="{filename}">Download modified G-code</a>'
