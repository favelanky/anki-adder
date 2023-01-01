import keyboard
import pyperclip
from threading import Thread
from threading import Event
from synonims_api import ReversoContextAPI
import card_adder


def add_card():
    API = ReversoContextAPI(source_lang="en", target_lang="ru")
    API.sentence = word
    card_adder.add_card(API.sentence, API.get_translation(), API.get_synonyms())


def add_wait():
    global event
    while True:
        print("Waiting key")
        event.wait()
        add_card()
        print("Added")
        event.clear()


def wait_key():
    keyboard.add_hotkey('ctrl+s', signal)
    keyboard.wait()


def signal():
    global word
    global event
    word = pyperclip.paste()
    print("Giving a word")
    event.set()


word = ''
event = Event()
if __name__ == '__main__':
    hotkey = Thread(target=wait_key)
    adder = Thread(target=add_wait)
    hotkey.start()
    adder.start()
    hotkey.join()
    adder.join()
