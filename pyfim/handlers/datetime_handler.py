from datetime import datetime, timedelta


def get_file_rename_time(delta=0):
    now = datetime.now() + timedelta(seconds=delta)
    timestamp = f"{now.strftime('%Y-%m-%d_%H-%M-%S.%f')[:-3]}"
    return timestamp
