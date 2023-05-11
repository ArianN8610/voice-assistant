import subprocess
import os


def install(install_list: list, install_program: str, program_name: str):
    try:
        subprocess.check_call(install_list, stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        while True:
            ask = input(f'To use the voice assistant, you need to install {program_name}. Do you want to install it? '
                        '([Y]es/[N]o): ').lower()

            if ask in ('yes', 'y'):
                print('Installing...')
                subprocess.run(['powershell', '-Command', install_program])
                print('The install was done successfully.\n')
            elif ask in ('no', 'n'):
                print('The program is over')
                exit()


def py310():
    py_version = subprocess.run(['py', '--list'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    if '-V:3.10' not in py_version:
        ask = input('To use the voice assistant, you need to install python 3.10. Do you want to install it? '
                    '([Y]es/[N]o): ').lower()

        if ask in ('yes', 'y'):
            print('Installing...')
            subprocess.run(['powershell', '-Command', 'choco install python --version=3.10.10'])
            print('The install was done successfully.\n')
        elif ask in ('no', 'n'):
            print('The program is over')
            exit()
    else:
        if 'Active venv' not in py_version:
            os.system('py -3.10 -m venv venv')
            os.system('venv/Scripts/activate.bat')
            os.system('pip install -r requirements.txt')


def setup():
    install(['choco', '-v'], 'Set-ExecutionPolicy Bypass -Scope Process -Force; '
                             '[System.Net.ServicePointManager]::SecurityProtocol = '
                             '[System.Net.ServicePointManager]::SecurityProtocol '
                             '-bor 3072; iex '
                             '((New-Object System.Net.WebClient).DownloadString'
                             "('https://community.chocolatey.org/install.ps1'))", 'chocolatey')

    install(['ffmpeg', '-version'], 'choco install ffmpeg', 'ffmpeg')
    py310()
