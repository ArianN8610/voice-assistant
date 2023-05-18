import requests
import os
import subprocess
import sys
from text_and_audio.sound_production import text_to_speech
from text_and_audio.print_speech import print_and_speech

# URLs
master = 'https://api.github.com/repos/ArianN8610/voice-assistant/commits?sha=master'
develop = 'https://api.github.com/repos/ArianN8610/voice-assistant/commits?sha=develop'
repository = 'https://github.com/ArianN8610/voice-assistant.git'

# Folder and Files
dire = 'dontDeleteMe'
master_version = f'{dire}/master_version.txt'
develop_version = f'{dire}/develop_version.txt'


def get_version():
    response_master = requests.get(master).json()
    response_develop = requests.get(develop).json()

    if 'message' not in response_master or 'message' not in response_develop:
        if not os.path.exists(master_version):
            with open(master_version, 'w') as f:
                f.write(str(len(response_master)))

        if not os.path.exists(develop_version):
            with open(develop_version, 'w') as f:
                f.write(str(len(response_develop)))


def get_update(branch: str):
    download_command = ['git', 'pull', repository, f'{branch}:{branch}']
    subprocess.call(download_command)


def run_update(message: str, branch: str, version: int):
    input_print = message
    text_to_speech(input_print)

    while True:
        query = input(input_print).lower()

        if query in ('y', 'yes'):
            get_update(branch)
            subprocess.call(['git', 'checkout', branch])
            print_and_speech('The program has been successfully updated')

            with open(f'{dire}/{branch}_version', 'w') as f:
                f.write(str(version))

            os.execl(sys.executable, sys.executable, *sys.argv)
            break
        elif query in ('n', 'no'):
            break


def git_init():
    if not os.path.exists('.git'):
        subprocess.call(['git', 'init'])
        subprocess.call(['git', 'branch', 'develop'])


def check_update(start: bool = False):
    git_init()

    if os.path.exists(master_version) and os.path.exists(develop_version):
        response_master = requests.get(master).json()
        response_develop = requests.get(develop).json()

        if 'message' not in response_master and 'message' not in response_develop:
            with open(master_version, 'r') as f:
                main_version = int(f.read())

            with open(develop_version, 'r') as f:
                beta_version = int(f.read())

            if len(response_master) > main_version:
                run_update('A new version of the app is available. Do you want to get it? ', 'master',
                           len(response_master))
            elif len(response_develop) > beta_version:
                run_update('Beta version of the app is available. Do you want to get it? ', 'develop',
                           len(response_develop))
            else:
                if not start:
                    print_and_speech('There are no updates')
        else:
            if not start:
                print_and_speech("Sorry, you're not able to receive the update now. Please try again later")
