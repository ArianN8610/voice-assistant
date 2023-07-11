from text_and_audio.print_speech import print_and_speech
from text_and_audio.stt import speech_to_text
from datetime import datetime
import os

txt_file = 'dontDeleteMe/notes'


def write_note():
    print_and_speech('What do you want to write?...')
    text = speech_to_text('en')

    with open(txt_file, 'a') as f:
        f.write(f'{text} --- {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

    print_and_speech('Note added successfully')


def show_notes():
    if os.path.exists(txt_file):
        with open(txt_file, 'r') as f:
            print(f'\n{f.read()}')
    else:
        print_and_speech('No notes have been added yet')


def delete_notes():
    if os.path.exists(txt_file):
        print_and_speech('Are you sure you want to delete all notes?')
        answer = speech_to_text('en').lower()

        if answer == 'yes':
            os.remove(txt_file)
            print_and_speech('All notes have been successfully deleted')
    else:
        print_and_speech('There are no notes to delete')
