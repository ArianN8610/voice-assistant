from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from os import remove


def text_to_speech(text: str):
    file = "sound.mp3"
    obj = gTTS(text=text, lang="en", slow=False)
    obj.save(file)

    sound = AudioSegment.from_mp3(file)
    play(sound)

    remove(file)
