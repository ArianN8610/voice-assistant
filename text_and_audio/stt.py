import speech_recognition as sr
from text_and_audio.print_speech import print_and_speech
import os

recognizer = sr.Recognizer()
file_mode = 'dontDeleteMe/mode'


def speech_to_text(lang: str, sorry_print: bool = True) -> str:
    if os.path.exists(file_mode):
        with open(file_mode, 'r') as f:
            ai_mode = f.read()
    else:
        ai_mode = 'speaking mode'

    if ai_mode == 'typing mode':
        return input('>>> ')
    else:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            recognizer.pause_threshold = 0.5
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language=lang)
        except sr.exceptions.UnknownValueError:
            if sorry_print:
                print_and_speech("Sorry, I can't recognize your voice")
            text = 'None'

        return text
