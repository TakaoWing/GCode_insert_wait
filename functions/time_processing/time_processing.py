from datetime import datetime, timedelta

def calculate_elapsed_time(start_time):
    now = datetime.now()
    wait_time = timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
    elapsed_time = now - now.replace(hour=0, minute=0, second=0, microsecond=0) - wait_time
    seconds = elapsed_time.total_seconds()
    _seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    elapsed_time_string = f"{int(hours):02d}h{int(minutes):02d}m{int(seconds):02d}s"
    return elapsed_time_string, _seconds