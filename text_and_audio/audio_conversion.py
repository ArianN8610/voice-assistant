import speech_recognition as sr

recognizer = sr.Recognizer()


def speech_to_text(lang: str) -> str:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio, language=lang)

        return text
