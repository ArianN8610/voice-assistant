import os
from text_and_audio.print_speech import print_and_speech
from text_and_audio.sound_production import text_to_speech

txt_file = 'dontDeleteMe/password.txt'


def set_passwd():
    if not os.path.exists(txt_file):
        print_and_speech('Please type your desired password below')
        passwd = input('Your password: ')

        with open(txt_file, 'w') as f:
            f.write(passwd)

        print_and_speech('The password has been set successfully')
    else:
        print_and_speech('You have already created a password')


def check_passwd():
    if os.path.exists(txt_file):
        passwd_print = 'Enter the password'
        text_to_speech(passwd_print)

        with open(txt_file, 'r') as f:
            correct_passwd = f.read()

        while True:
            passwd = input(passwd_print + ': ')

            if passwd != correct_passwd:
                print_and_speech('The password is incorrect')
            else:
                break


def change_passwd():
    if os.path.exists(txt_file):
        check_passwd()

        print_and_speech('Please type your new password below')
        with open(txt_file, 'r') as f:
            passwd = f.read()

        while True:
            new_passwd = input('New password: ')

            if new_passwd == passwd:
                print_and_speech('Duplicate password')
            else:
                with open(txt_file, 'w') as f:
                    f.write(new_passwd)
                break

        print_and_speech('Password changed successfully')
    else:
        print_and_speech('There is no password yet')
