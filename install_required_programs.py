import subprocess
import os

directory = 'dontDeleteMe'
file = f'{directory}/install_programs.txt'


def run_command():
    while True:
        message = input(
            "To use the voice assistant, you need to install chocolatey and ffmpeg. Do you want to install "
            "them? ([Y]es/[N]o): ")

        if message.lower() in ('yes', 'y'):
            print('Downloading...')
            subprocess.run(["powershell", "-Command", "Set-ExecutionPolicy Bypass -Scope Process -Force; "
                                                      "[System.Net.ServicePointManager]::SecurityProtocol = "
                                                      "[System.Net.ServicePointManager]::SecurityProtocol "
                                                      "-bor 3072; iex "
                                                      "((New-Object System.Net.WebClient).DownloadString"
                                                      "('https://community.chocolatey.org/install.ps1'))"])
            subprocess.run(["powershell", "-Command", "choco install ffmpeg"])
            print('The download was done successfully.\n')
            with open(file, 'w') as f:
                f.write('True')
            break
        elif message.lower() in ('no', 'n'):
            with open(file, 'w') as f:
                f.write('False')
            print('The program is over')
            exit()


def install():
    if not os.path.exists(directory):
        os.mkdir(directory)

    if not os.path.exists(file):
        run_command()
    else:
        with open(file, 'r') as f:
            if f.read() == 'False':
                run_command()
