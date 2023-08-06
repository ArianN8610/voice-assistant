import os
import re
from EdgeGPT import Chatbot, ConversationStyle
from text_and_audio.print_speech import print_and_speech
from text_and_audio.stt import speech_to_text

file_mode = 'dontDeleteMe/mode'


async def ai(lang: str):
    print_and_speech('Ask me your question...')
    text = speech_to_text(lang)

    if os.path.exists(file_mode):
        with open(file_mode, 'r') as f:
            if f.read() == 'speaking mode':
                print(f'You said: {text}')
    else:
        print(f'You said: {text}')

    bot = Chatbot(cookie_path='cookies.json')
    response = await bot.ask(prompt=text, conversation_style=ConversationStyle.precise)

    for message in response['item']['messages']:
        if message['author'] == 'bot':
            bot_response = message['text']

    bot_response = re.sub('\[\^\d+\^\]', '', bot_response)

    print('Answer: ', end='')
    print_and_speech(bot_response)

    await bot.close()
