import io
import streamlit as st
from functions.page_styling.page_styling import custom_css
from functions.gcode_processing.gcode_processing import insert_wait_gcode
from functions.download_link.download_link import create_download_link
from functions.time_processing.time_processing import calculate_elapsed_time

def main():
    # Title and description
    st.set_page_config(page_title="G-code Wait Time Inserter")
    custom_css()
    st.title("G-code Wait Time Inserter")
    st.write("This app inserts a wait time into a G-code file between lines 42 and 43.")

    # File upload
    uploaded_file = st.file_uploader("Upload your G-code file", type=["gcode"])

    # Wait time input
    start_time = st.time_input("Enter start time")
    elapsed_time,seconds = calculate_elapsed_time(start_time)
    st.write(f"Elapsed time since {start_time}: {elapsed_time}")


    # Process the uploaded file and insert wait time
    if uploaded_file and start_time:
        if st.button("Insert Wait Time"):
            input_gcode_file = io.TextIOWrapper(uploaded_file)
            output_gcode = insert_wait_gcode(input_gcode_file, seconds)

            # Provide a download link for the modified G-code
            st.markdown(create_download_link(output_gcode, "modified_gcode.gcode"), unsafe_allow_html=True)
    elif not uploaded_file:
        st.warning("Please upload a G-code file.")
    elif not start_time:
        st.warning("Please enter a start time.")


if __name__ == '__main__':
    main()
