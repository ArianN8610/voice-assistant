import os

file = 'dontDeleteMe/mode'


def mode(file_mode: str):
    if os.path.exists(file):
        with open(file, 'r') as f:
            ai_mode = f.read()

        if ai_mode == file_mode:
            print(f'You are already in {file_mode}')
        else:
            with open(file, 'w') as f:
                f.write(file_mode)
    else:
        with open(file, 'w') as f:
            f.write(file_mode)
