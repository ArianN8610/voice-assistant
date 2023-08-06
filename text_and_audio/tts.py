from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

file_mode = 'dontDeleteMe/mode'


def text_to_speech(text: str):
    if os.path.exists(file_mode):
        with open(file_mode, 'r') as f:
            ai_mode = f.read()
    else:
        ai_mode = 'speaking mode'

    if ai_mode == 'speaking mode':
        file = "sound.mp3"
        obj = gTTS(text=text, lang="en", slow=False)
        obj.save(file)

        sound = AudioSegment.from_mp3(file)
        play(sound)

        os.remove(file)
    else:
        pass
