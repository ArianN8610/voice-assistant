import speech_recognition as sr
from text_and_audio.print_speech import print_and_speech

recognizer = sr.Recognizer()


def speech_to_text(lang: str, sorry_print: bool = True) -> str:
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
