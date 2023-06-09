from text_and_audio.print_speech import print_and_speech
from text_and_audio.stt import speech_to_text
import os

dire = 'dontDeleteMe'
txt_file = f'{dire}/username'


def get_username():
    if not os.path.exists(dire):
        os.mkdir(dire)

    if os.path.exists(txt_file):
        with open(txt_file, 'r') as f:
            if f.read().strip() != '':
                return

    print_and_speech("\nHello, welcome to Voice AI. I'm your voice assistant. To start, please tell me your name...")
    username = speech_to_text('en')

    if username != 'None':
        with open(txt_file, 'w') as f:
            f.write(username)
        print_and_speech(f'Hi {username}, nice to meet you. How can I help you? Say "help" to see my features.')
    else:
        get_username()


def change_username():
    print_and_speech('Please tell me your new name...')
    new_username = speech_to_text('en')
    with open(txt_file, 'w') as f:
        f.write(new_username)
    print_and_speech('Your name has been updated successfully')
