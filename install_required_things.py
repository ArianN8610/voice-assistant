import subprocess
import os
import sys

dire = 'dontDeleteMe'
txt_file = f'{dire}/restart.txt'


def install(install_list: list, install_program: str, program_name: str, admin: bool):
    try:
        subprocess.check_call(install_list, stdout=subprocess.DEVNULL)
    except FileNotFoundError:
        while True:
            ask = input(f'To use the voice assistant, you need to install {program_name}. Do you want to install it? '
                        '([Y]es/[N]o): ').lower()

            if ask in ('yes', 'y'):
                print('Installing...')
                if admin:
                    subprocess.run(["powershell", "-Command", "Start-Process", "powershell", "-ArgumentList",
                                    f"'-ExecutionPolicy', 'Bypass', '-Command', '{install_program}'",
                                    "-Verb", "runAs"])
                else:
                    subprocess.run(['powershell', '-Command', install_program])
                print('The install was done successfully\n')
                break
            elif ask in ('no', 'n'):
                print('The program is over')
                exit()


def py310():
    py_version = subprocess.run(['py', '--list'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    if '3.10' not in py_version:
        ask = input('To use the voice assistant, you need to install python 3.10. Do you want to install it? '
                    '([Y]es/[N]o): ').lower()

        if ask in ('yes', 'y'):
            print('Installing...')
            subprocess.run(["powershell", "-Command", "Start-Process", "powershell", "-ArgumentList",
                            "'-ExecutionPolicy', 'Bypass', '-Command', 'choco install python --version=3.10.10'",
                            "-Verb", "runAs"])
            print('The install was done successfully\n')
        elif ask in ('no', 'n'):
            print('The program is over')
            exit()
    else:
        if 'Active venv' not in py_version:
            os.system('py -3.10 -m venv venv')
            os.system('venv/Scripts/activate.bat')
            os.system('pip install -r requirements.txt')


def restart():
    if not os.path.exists(dire):
        os.mkdir(dire)

    with open(txt_file, 'w') as f:
        f.write('True')

    os.execl(sys.executable, sys.executable, *sys.argv)


def setup():
    if os.path.exists(txt_file):
        with open(txt_file, 'r') as f:
            if f.read() == 'True':
                return

    install(['choco', '-v'], 'Set-ExecutionPolicy Bypass -Scope Process -Force; '
                             '[System.Net.ServicePointManager]::SecurityProtocol = '
                             '[System.Net.ServicePointManager]::SecurityProtocol '
                             '-bor 3072; iex '
                             '((New-Object System.Net.WebClient).DownloadString'
                             "('https://community.chocolatey.org/install.ps1'))", 'chocolatey', False)

    install(['ffmpeg', '-version'], 'choco install ffmpeg', 'ffmpeg', True)
    install(['git', '-v'], 'choco install git.install', 'git', True)
    py310()

    if os.path.exists(txt_file):
        with open(txt_file, 'r') as f:
            if f.read() != 'True':
                restart()
    else:
        restart()
