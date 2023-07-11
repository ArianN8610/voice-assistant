import subprocess
import os
import sys

need_to_restart = False


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

        need_to_restart = True


def py310():
    py_version = str(subprocess.check_output('py --list'))

    if '3.10' not in py_version:
        while True:
            ask = input('To use the voice assistant, you need to install python 3.10. Do you want to install it? '
                        '([Y]es/[N]o): ').lower()

            if ask in ('yes', 'y'):
                print('Installing...')
                subprocess.run(["powershell", "-Command", "Start-Process", "powershell", "-ArgumentList",
                                "'-ExecutionPolicy', 'Bypass', '-Command', 'choco install python --version=3.10.10'",
                                "-Verb", "runAs"])
                print('The install was done successfully\n')
                break
            elif ask in ('no', 'n'):
                print('The program is over')
                exit()

        need_to_restart = True
    else:
        if not os.path.exists('venv'):
            os.system('py -3.10 -m venv venv')
            os.system('venv/Scripts/activate.bat')
            os.system('pip install -r requirements.txt')

            need_to_restart = True


def restart():
    if need_to_restart:
        os.execl(sys.executable, sys.executable, *sys.argv)  # Restart program


def setup():
    install(['choco', '-v'], 'Set-ExecutionPolicy Bypass -Scope Process -Force; '
                             '[System.Net.ServicePointManager]::SecurityProtocol = '
                             '[System.Net.ServicePointManager]::SecurityProtocol '
                             '-bor 3072; iex '
                             '((New-Object System.Net.WebClient).DownloadString'
                             "('https://community.chocolatey.org/install.ps1'))", 'chocolatey', False)
    install(['ffmpeg', '-version'], 'choco install ffmpeg', 'ffmpeg', True)
    install(['git', '--version'], 'choco install git.install', 'git', True)
    py310()
    restart()
