from datetime import datetime
from text_and_audio.print_speech import print_and_speech


def date_and_time():
    now = datetime.now()
    result = now.strftime("Today is %A, %B %d, %Y at %X")
    print_and_speech(result)
