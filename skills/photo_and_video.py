import cv2
from text_and_audio.print_speech import print_and_speech
import os
from datetime import datetime
import pyautogui
import numpy as np

cam = cv2.VideoCapture(0)
now = datetime.now().strftime('%Y-%m-%d %H%M%S')


def take_photo():
    if cam.isOpened():
        result, pic = cam.read()

        if result:
            dire = 'photos'

            if not os.path.exists(dire):
                os.mkdir(dire)

            print_and_speech('You can save the photo by pressing the "s" key')

            while True:
                result, pic = cam.read()
                cv2.imshow('Video', pic)

                if cv2.waitKey(1) & 0xFF == ord('s'):
                    cv2.imwrite(f"{dire}/photo {now}.jpg", pic)
                    cam.release()
                    break

            print_and_speech(f'The photo was successfully saved in the {dire} folder')
        else:
            print_and_speech('Something went wrong. Please try again')
    else:
        print_and_speech("Can't open the camera")


def take_video():
    if cam.isOpened():
        result, frame = cam.read()
        dire = 'videos'

        if result:
            if not os.path.exists(dire):
                os.mkdir(dire)

            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(f'{dire}/video {now}.mp4', fourcc, 20.0, (640, 480))

            print_and_speech('Video will be recorded. You can stop and save the video by pressing the "s" key')

            while True:
                result, frame = cam.read()
                out.write(frame)
                cv2.imshow('Video', frame)
                if cv2.waitKey(1) & 0xFF == ord('s'):
                    break

            cam.release()
            out.release()
            cv2.destroyAllWindows()

            print_and_speech('Video was successfully saved in the "videos" folder')
        else:
            print_and_speech('Something went wrong. Please try again')
    else:
        print_and_speech("Can't open the camera")


def screenshot():
    dire = 'screenshots'

    if not os.path.exists(dire):
        os.mkdir(dire)

    screen = pyautogui.screenshot()
    screen.save(f"{dire}/screenshot {now}.jpg")
    print_and_speech(f'The screenshot was successfully saved in the {dire} folder')


def screen_recorder():
    screen_size = tuple(pyautogui.size())
    dire = 'screen records'

    if not os.path.exists(dire):
        os.mkdir(dire)

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(f'{dire}/screen record {now}.avi', fourcc, 20.0, screen_size)

    print_and_speech('screen will be recorded. You can stop and save the screen record by pressing the "s" key')

    cv2.namedWindow('Screen recorder', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Screen recorder', 480, 270)

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow('Screen recorder', frame)

        if cv2.waitKey(1) == ord('s'):
            break

    out.release()
    cv2.destroyAllWindows()

    print_and_speech('Screen record was successfully saved in the "screen records" folder')
