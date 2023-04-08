import io

def generate_gcode_wait(wait_time_seconds: int) -> str:
    """
    Generates G-code to wait for a specified time in seconds

    Parameters:
        wait_time_seconds (int): The number of seconds to wait

    Returns:
        str: The G-code for the wait time
    """
    max_wait_time = 999
    full_wait_blocks = wait_time_seconds // max_wait_time
    remaining_wait_time = wait_time_seconds % max_wait_time

    gcode = ""
    for _ in range(full_wait_blocks):
        gcode += f"G4 S{max_wait_time}\n"

    if remaining_wait_time > 0:
        gcode += f"G4 S{remaining_wait_time}\n"

    return gcode


def insert_wait_gcode(input_file: io.TextIOWrapper, wait_time_seconds: int) -> str:
    """
    Inserts wait time G-code into a given G-code file

    Parameters:
        input_file (io.TextIOWrapper): The file object for the input G-code file
        wait_time_seconds (int): The number of seconds to wait

    Returns:
        str: The G-code with the wait time inserted
    """
    output_gcode = ""
    for idx, line in enumerate(input_file.readlines()):
        if idx == 42:
            output_gcode += generate_gcode_wait(wait_time_seconds)
        output_gcode += line
    return output_gcode
