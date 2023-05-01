from googletrans import Translator

trans = Translator()


def text_translation(text: str, src: str, dest: str) -> str:
    result = trans.translate(text, dest, src).text

    return result
