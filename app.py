import io
import streamlit as st
from functions.page_styling.page_styling import set_custom_css
from functions.gcode_processing.gcode_processing import insert_wait_gcode
from functions.file_processing.file_processing import upload,create_download_link
from functions.time_processing.time_processing import calculate_elapsed_time, select_timezone, combine_date_time

def main():
    # Title and description
    st.set_page_config(page_title="G-code Wait Time Inserter")
    set_custom_css("style.css")
    st.title("G-code Wait Time Inserter")
    st.write("This app inserts a wait time into a G-code file between lines 42 and 43.")

    # File upload
    uploaded_file = upload(st)

    if not uploaded_file:
        st.warning("Please upload a G-code file.")
        return
    
    # Display the detected timezone and let the user confirm or select another one
    selected_timezone = select_timezone(st)
    
    # Wait time input
    start_date = st.date_input("Enter start date")
    start_time = st.time_input("Enter start time")
    start_datetime = combine_date_time(start_date, start_time)
    elapsed_time, seconds = calculate_elapsed_time(start_datetime, selected_timezone) 

    if seconds < 0:
        st.error("Invalid start time. Please enter a future time.")
        return

    st.write(f"Elapsed time since {start_time}: {elapsed_time}")

    # Process the uploaded file and insert wait time
    if not start_time:
        st.warning("Please enter a start time.")
        return
    
    if st.button("Insert Wait Time"):
        input_gcode_file = io.TextIOWrapper(uploaded_file)
        output_gcode = insert_wait_gcode(input_gcode_file, seconds)

        # Provide a download link for the modified G-code
        st.markdown(create_download_link(output_gcode, "modified_gcode.gcode"), unsafe_allow_html=True)

if __name__ == '__main__':
    main()
