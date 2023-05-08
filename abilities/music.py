import os
from text_and_audio.print_speech import print_and_speech
from random import choice
from pydub import AudioSegment
from pydub.playback import play

dire = 'dontDeleteMe'


def play_random_music():
    txt_file = f'{dire}/random_music.txt'

    if os.path.exists(txt_file):
        with open(txt_file, 'r') as f:
            directory = f.read()
    else:
        print_and_speech('Please type the directory where your songs are located below')
        directory = input('Your dir: ')

    try:
        random_song = choice(os.listdir(directory))
    except FileNotFoundError:
        print_and_speech("Sorry, I couldn't find the folder")
        os.remove(txt_file)
        return

    with open(txt_file, 'w') as f:
        f.write(directory)

    print_and_speech("I'll play a random song")
    os.startfile(os.path.join(directory, random_song))


def edit_music_folder(name):
    txt_file = f'{dire}/{name}'

    print_and_speech('Please type the location of the new folder below')
    new_dir = input('New folder location: ')

    if os.path.exists(new_dir) and os.path.isdir(new_dir):
        with open(txt_file, 'w') as f:
            f.write(new_dir)
        print_and_speech('The folder location has been successfully updated')
    else:
        print_and_speech("Sorry, I couldn't find the folder")


def play_music():
    print_and_speech('Please type your song location below')
    song = input('Your song location: ')
    if os.path.exists(song) and os.path.isfile(song):
        print_and_speech("I'll play the song")
        os.startfile(song)
    else:
        print_and_speech("Sorry, I couldn't find the file")


def playlist():
    txt_file = f'{dire}/playlist.txt'

    if os.path.exists(txt_file):
        with open(txt_file, 'r') as f:
            music_list = f.read()
    else:
        print_and_speech('Please type your playlist location below')
        music_list = input('Your playlist location: ')

    with open(txt_file, 'w') as f:
        f.write(music_list)

    if os.path.exists(music_list) and os.path.isdir(music_list):
        print_and_speech("I'll play your playlist songs")
        for music in os.listdir(music_list):
            if music.endswith('.mp3'):
                sound = AudioSegment.from_file(os.path.join(music_list, music), format="mp3")
                play(sound)
    else:
        print_and_speech("Sorry, I couldn't fine your playlist")
