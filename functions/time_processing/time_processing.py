from datetime import datetime
import pytz
import requests

# Get timezone based on IP address
def get_timezone_from_ip() -> str:
    """
    Get the timezone based on the IP address of the user.

    Returns:
    str: The timezone.
     """
    try:
        response = requests.get("https://ipapi.co/timezone").text
        if "error" in response:
            return "Asia/Tokyo"
        return response
    except:
        return "Asia/Tokyo"

def select_timezone(st) -> str:
    """
    Display a dropdown menu to select the timezone.

    Parameters:
    st (streamlit): The streamlit object.

    Returns:
    str: The selected timezone.
    """
    default_timezone = get_timezone_from_ip()
    timezones = sorted(pytz.all_timezones)
    selected_timezone = st.selectbox("Select your timezone:", timezones, index=timezones.index(default_timezone))
    return selected_timezone

def combine_date_time(date, time):
    """
    Combine the given date and time into a datetime object.

    Parameters:
    date (date): The date.
    time (time): The time.

    Returns:
    datetime: The combined datetime object.
    """
    return datetime.combine(date, time)
    

def calculate_elapsed_time(start_datetime: datetime, timezone: str) -> tuple:
    """
    Calculate the elapsed time since the given start time and return it as a string and as the total number of seconds.

    Parameters:
    start_time (datetime): The start time.

    Returns:
    tuple: A tuple containing the elapsed time string (in the format "HHhMMmSSs") and the total number of seconds.
    """
    tz = pytz.timezone(timezone)
    now = datetime.now(tz=tz)
    start_datetime = start_datetime.astimezone(tz)
    wait_time = start_datetime - now
    seconds = wait_time.total_seconds()
    _seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    elapsed_time_string = f"{int(hours):02d}h{int(minutes):02d}m{int(seconds):02d}s"
    return elapsed_time_string, _seconds