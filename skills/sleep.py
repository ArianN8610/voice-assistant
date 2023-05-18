from text_and_audio.sound_production import text_to_speech
from text_and_audio.audio_conversion import speech_to_text
from text_and_audio.print_speech import print_and_speech
import time


def dont_listen():
    text = 'How many minutes do you want me to sleep: '
    text_to_speech(text)
    try:
        sleep_time = int(input(text))
    except ValueError:
        print_and_speech('Please type a number')
        return
    print_and_speech('See you later')
    time.sleep(sleep_time * 60)


def sleep_voice_ai():
    print_and_speech('I\'ll go to sleep. You can wake me up by saying "wake up"...')

    while True:
        text = speech_to_text('en', False).lower()
        if text == 'wake up':
            break
