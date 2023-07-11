from googletrans import Translator
from text_and_audio.stt import speech_to_text
from text_and_audio.print_speech import print_and_speech

trans = Translator()


def text_translation(src: str, dest: str):
    print_and_speech('What do you want to translate?...')
    text = speech_to_text(src)

    print(f"You said: {text}")

    result = trans.translate(text, dest, src).text

    print_and_speech(f'Translation: {result}')
