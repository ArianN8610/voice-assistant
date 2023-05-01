from datetime import datetime


def date_and_time() -> str:
    now = datetime.now()
    result = now.strftime("Today is %A, %B %d, %Y at %X")

    return result
