from datetime import datetime, timedelta
import pytz

def calculate_elapsed_time(start_time: datetime) -> tuple:
    """
    Calculate the elapsed time since the given start time and return it as a string and as the total number of seconds.

    Parameters:
    start_time (datetime): The start time.

    Returns:
    tuple: A tuple containing the elapsed time string (in the format "HHhMMmSSs") and the total number of seconds.
    """
    tz = pytz.timezone('Asia/Tokyo')
    now = datetime.now(tz=tz)
    wait_time = timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
    elapsed_time = now - now.replace(hour=0, minute=0, second=0, microsecond=0) - wait_time
    total_seconds = int(elapsed_time.total_seconds())
    elapsed_hours, remainder = divmod(total_seconds, 3600)
    elapsed_minutes, elapsed_seconds = divmod(remainder, 60)
    elapsed_time_string = f"{elapsed_hours:02d}h{elapsed_minutes:02d}m{elapsed_seconds:02d}s"
    return elapsed_time_string, total_seconds
