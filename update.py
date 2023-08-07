import os
import subprocess
import sys
from text_and_audio.tts import text_to_speech
from text_and_audio.print_speech import print_and_speech
import urllib.request

# URLs
public_main_file = 'https://raw.githubusercontent.com/ArianN8610/voice-assistant/master/version/main'
public_beta_file = 'https://raw.githubusercontent.com/ArianN8610/voice-assistant/develop/version/beta'
repository = 'https://github.com/ArianN8610/voice-assistant.git'

# Folder and Files
dire = 'version'
local_main_file = f'{dire}/main'
local_beta_file = f'{dire}/beta'


def get_update(branch: str):
    if branch == 'master':
        version_type = 'A new version'
    else:
        version_type = 'Beta version'

    message = f'{version_type} of the app is available. Do you want to get it? '
    text_to_speech(message)

    while True:
        query = input(message).lower()

        if query in ('y', 'yes'):
            get_update_command = ['git', 'pull', repository, f'{branch}:{branch}']
            subprocess.run(get_update_command)

            subprocess.run(['git', 'checkout', branch])
            print_and_speech('The program has been successfully updated')

            os.execl(sys.executable, sys.executable, *sys.argv)
            break
        elif query in ('n', 'no'):
            break


def git_init():
    if not os.path.exists('.git'):
        subprocess.run(['git', 'init'])
    if 'develop' not in subprocess.getoutput('git branch').lower():
        subprocess.run(['git', 'branch', 'develop'])


def get_public_versions():
    public_main_version = int(urllib.request.urlopen(public_main_file).read().decode('utf-8'))
    public_beta_version = int(urllib.request.urlopen(public_beta_file).read().decode('utf-8'))

    return public_main_version, public_beta_version


def get_local_versions():
    with open(local_main_file, 'r') as f:
        local_main_version = int(f.read())

    with open(local_beta_file, 'r') as f:
        local_beta_version = int(f.read())

    return local_main_version, local_beta_version


def check_update():
    git_init()

    public_main_version, public_beta_version = get_public_versions()
    local_main_version, local_beta_version = get_local_versions()

    if public_main_version > local_main_version:
        get_update('master')
    elif public_beta_version > local_beta_version:
        get_update('develop')
    else:
        print_and_speech('There are no updates')
