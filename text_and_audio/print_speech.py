from text_and_audio.sound_production import text_to_speech


def print_and_speech(text: str):
    print(text)
    text_to_speech(text)
