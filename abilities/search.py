from webbrowser import open_new_tab
from text_and_audio.audio_conversion import speech_to_text
from text_and_audio.print_speech import print_and_speech


def search(lang: str):
    print_and_speech('What do you want to search?...')
    text = speech_to_text(lang)
    open_new_tab('https://www.google.com/search?q=' + text)
    print_and_speech('searched')
