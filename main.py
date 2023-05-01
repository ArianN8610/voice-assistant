import asyncio
import re
from EdgeGPT import Chatbot, ConversationStyle

# Text and audio
import speech_recognition as sr
from text_and_audio.sound_production import text_to_speech
from text_and_audio.audio_conversion import speech_to_text

# Capabilities
from capabilities.date_time import date_and_time
from capabilities.internet_speed import get_internet_speed
from capabilities.system_battery_charging import get_battery_charge
from capabilities.translation import text_translation


# Create a recognizer object and wake up word
recognizer = sr.Recognizer()
WAKE_UP = "voice ai"
PHRASE = ["date time", "internet speed", "battery charge", "english to persian translation",
          "persian to english translation"]


def get_wake_word(phrase: str) -> bool:
    if WAKE_UP in phrase.lower():
        return True
    else:
        return False


def run(text: str) -> str:
    if text == "date time":
        return date_and_time()
    elif text == "internet speed":
        return get_internet_speed()
    elif text == "battery charge":
        return get_battery_charge()
    elif text == "english to persian translation":
        print("Listening...")
        text_to_speech("Listening")
        text = speech_to_text("en")
        print(f"You said: {text}")

        return text_translation(
            text,
            "en",
            "fa"
        )
    elif text == "persian to english translation":
        print("Listening...")
        text_to_speech("Listening")
        text = speech_to_text("fa")
        print(f"You said: {text}")

        return text_translation(
            text,
            "fa",
            "en"
        )


async def main():
    while True:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print(f"Waiting for wake word '{WAKE_UP}'...")

            while True:
                audio = recognizer.listen(source)
                try:
                    phrase = recognizer.recognize_google(audio, language="en")

                    if phrase == "exit":
                        print("Closing...")
                        return

                    print(f"You said: {phrase}")

                    wake_word = get_wake_word(phrase)
                    if wake_word:
                        break
                    else:
                        print("Not a wake word. Try again")
                except Exception as e:
                    print(f"Error transcribing audio: {e}")
                    continue

            print("Listening...")
            text_to_speech("Listening")
            audio = recognizer.listen(source)

            try:
                user_input = recognizer.recognize_google(audio, language="en")
                print(f"You said: {user_input}")
            except Exception as e:
                print(f"Error transcribing audio: {e}")
                continue

            if user_input.lower() not in PHRASE:
                bot = Chatbot(cookie_path='cookies.json')
                response = await bot.ask(prompt=user_input, conversation_style=ConversationStyle.precise)

                for message in response["item"]["messages"]:
                    if message["author"] == "bot":
                        bot_response = message["text"]

                bot_response = re.sub('\[\^\d+\^\]', '', bot_response)
            else:
                bot_response = run(user_input.lower())

        print("Bot's response:", bot_response)
        text_to_speech(bot_response)
        try:
            await bot.close()
        except UnboundLocalError:
            pass


if __name__ == '__main__':
    asyncio.run(main())
