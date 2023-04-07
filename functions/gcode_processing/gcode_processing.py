def generate_gcode_wait(wait_time_seconds):
    """wait_time_seconds秒分のウェイト用G-codeを生成する"""
    max_wait_time = 999
    full_wait_blocks = wait_time_seconds // max_wait_time
    remaining_wait_time = wait_time_seconds % max_wait_time

    gcode = ""
    for _ in range(full_wait_blocks):
        gcode += f"G4 S{max_wait_time}\n"

    if remaining_wait_time > 0:
        gcode += f"G4 S{remaining_wait_time}\n"

    return gcode


def insert_wait_gcode(input_file, wait_time_seconds):
    """入力されたG-codeにウェイト用G-codeを挿入する"""
    output_gcode = ""
    for idx, line in enumerate(input_file.readlines()):
        if idx == 42:
            output_gcode += generate_gcode_wait(wait_time_seconds)
        output_gcode += line
    return output_gcode
