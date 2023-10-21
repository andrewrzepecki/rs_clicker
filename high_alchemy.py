import pyautogui as pygui
import keyboard
import random
import time

import Clicker


def main():

    start = pygui.confirm("Preparing to bot High Alchemy. Make sure magic tab is open.\n - > Start Botting?")
    clicker = Clicker.Clicker()
    target_coords = pygui.locateOnScreen('buttons/high_alchemy.png')
    if start != 'Cancel':
        while True:
            clicker.run(target=target_coords)


if __name__ == "__main__":
    main()


