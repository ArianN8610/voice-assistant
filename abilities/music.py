import os
from text_and_audio.print_speech import print_and_speech
from text_and_audio.sound_production import text_to_speech
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
        while True:
            random_song = choice(os.listdir(directory))

            if random_song.endswith('.mp3'):
                break
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
    if os.path.exists(song) and os.path.isfile(song) and song.endswith('.mp3'):
        print_and_speech("I'll play the song")
        os.startfile(song)
    else:
        print_and_speech("Sorry, I couldn't find the file")


def play_song_from_playlist(song, delete_song=''):
    txt_file = f'{dire}/playlist.txt'

    if os.path.isdir(song):
        if delete_song != '':
            song_list = os.listdir(song)
            song_list = song_list[song_list.index(delete_song) + 1:]
        else:
            song_list = os.listdir(song)

        for music in song_list:
            if music.endswith('.mp3'):
                song_path = os.path.join(song, music)
                sound = AudioSegment.from_file(song_path, format='mp3')
                play(sound)

                while True:
                    text = 'Do you want the next song to play? '
                    text_to_speech(text)
                    ask = input(text + '([Y]es/[N]o): ').lower()
                    with open(txt_file, 'w') as f:
                        f.write(song_path)
                    if ask in ('yes', 'y'):
                        break
                    elif ask in ('no', 'n'):
                        return
    elif os.path.isfile(song):
        song_dir = song.split('\\')
        del_song = song_dir[-1]
        song_dir.remove(song_dir[-1])
        song_dir = '\\'.join(song_dir)
        play_song_from_playlist(song_dir, del_song)


def playlist():
    txt_file = f'{dire}/playlist.txt'

    if os.path.exists(txt_file):
        with open(txt_file, 'r') as f:
            song = f.read()
    else:
        print_and_speech('Please type your playlist location below')
        song = input('Your playlist location: ')

        if not os.path.exists(song) or not os.path.isdir(song):
            print_and_speech("Sorry, I couldn't find your playlist")
            return

    with open(txt_file, 'w') as f:
        f.write(song)

    if os.path.exists(song) and os.path.isdir(song):
        print_and_speech("I'll play your playlist songs")
        play_song_from_playlist(song)
    elif os.path.exists(song) and os.path.isfile(song) and song.endswith('.mp3'):
        print_and_speech("I'll play your playlist songs")
        play_song_from_playlist(song)
    else:
        print_and_speech("Sorry, I couldn't find your playlist")
