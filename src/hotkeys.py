import keyboard
from time import sleep


def do():
    print("heh")


keyboard.add_hotkey('ctrl+c', do)

# TODO: add delay
keyboard.wait()
