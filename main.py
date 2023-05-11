import os
import ctypes
import time
import asyncio
import sys

# Install required programs
from install_required_things import setup

try:
    # Text and audio
    from text_and_audio.sound_production import text_to_speech
    from text_and_audio.audio_conversion import speech_to_text
    from text_and_audio.print_speech import print_and_speech

    # Abilities
    from abilities.date_time import date_and_time
    from abilities.internet_speed import get_internet_speed
    from abilities.translation import text_translation
    from abilities.search import search
    from abilities.photo_and_video import take_photo, take_video, screenshot, screen_recorder
    from abilities.music import play_random_music, play_music, edit_music_folder, playlist
    from abilities.note import write_note, show_notes, delete_notes
    from abilities.username import get_username, change_username
    from abilities.ai import ai
except ModuleNotFoundError:
    pass

# The folder where the data is stored
dire = 'dontDeleteMe'


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


def main():
    setup()
    os.execl(sys.executable, sys.executable, *sys.argv)
    get_username()

    while True:
        print('Listening...')
        query = speech_to_text('en').lower()

        if query not in ('exit', 'none'):
            print(f'You said: {query}')

        if query == 'exit':
            print_and_speech('Goodbye! Have a nice day!')
            exit()
        elif query == 'help':
            print_and_speech('You can see my abilities below')
            print('exit, (play random music, play random song), (edit songs folder, edit song folder, '
                  'edit music folder), (play music, play song), play playlist, edit playlist, date and time, '
                  'change my name, search, lock screen, shutdown, restart, sleep, don\'t listen, take a photo, '
                  'screenshot, take a video, screen record, write a note, show notes, delete notes, internet speed, '
                  'english to persian translation, persian to english translation, english ai, persian ai')
        elif query == 'play random music' or query == 'play random song':
            play_random_music()
        elif query == 'edit songs folder' or query == 'edit song folder' or query == 'edit music folder':
            edit_music_folder('random_music.txt')
        elif query == 'play music' or query == 'play song':
            play_music()
        elif query == 'play playlist':
            playlist()
        elif query == 'edit playlist':
            edit_music_folder('playlist.txt')
        elif query == 'date and time':
            date_and_time()
        elif query == 'change my name':
            change_username()
        elif query == 'english search':
            search('en')
        elif query == 'persian search':
            search('fa')
        elif query == 'lock screen':
            print_and_speech('Locking the device...')
            ctypes.windll.user32.LockWorkStation()
        elif query == 'shutdown':
            print_and_speech('Shutting down...')
            os.system('shutdown /s /t 1')
        elif query == 'restart':
            print_and_speech('Restarting...')
            os.system('shutdown /r /t 1')
        elif query == 'sleep':
            print_and_speech('Sleeping...')
            os.system('rundll32.exe powrprof.dll, SetSuspendState Sleep')
        elif query == "don't listen":
            dont_listen()
        elif query == 'take a photo':
            take_photo()
        elif query == 'screenshot':
            screenshot()
        elif query == 'take a video':
            take_video()
        elif query == 'screen record':
            screen_recorder()
        elif query == 'write a note':
            write_note()
        elif query == 'show notes':
            show_notes()
        elif query == 'delete notes':
            delete_notes()
        elif query == 'internet speed':
            get_internet_speed()
        elif query == 'english to persian translation':
            text_translation('en', 'fa')
        elif query == 'persian to english translation':
            text_translation('fa', 'en')
        elif query == 'english ai':
            asyncio.run(ai('en'))
        elif query == 'persian ai':
            asyncio.run(ai('fa'))
        else:
            if query != 'none':
                print_and_speech("Sorry, I didn't understand")


if __name__ == '__main__':
    main()
