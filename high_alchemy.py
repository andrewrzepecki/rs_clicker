import pyautogui as pygui
import keyboard
import random
import time

import Clicker

last_key = None
last_pause = 0

def pause():
    output = pygui.confirm("Botting Paused, Continue?")
    if output == 'Cancel':
        exit()


def check_pause():
    global last_key
    global last_pause
    if last_key != None and last_key.name == 'B' and last_pause < last_key.time:
        last_pause = last_key.time
        pause()


def on_key_press(event):
    global last_key
    last_key = event


def check_magic_stats():
    pass
    # Move to level tab
        # Move to n random first levels with random delays
    # hover magic level
        # Go back to magic tab


def get_random_value(min: float, max: float):
    return random.uniform(min, max)


def run():

    keyboard.on_press(on_key_press)
    # item_target_coords = pygui.locateOnScreen('buttons/magic_longbow.png')
    # magic_target_coords = pygui.locateOnScreen('buttons/magic_tab.png')
    spell_target_coords = pygui.locateOnScreen('buttons/high_alchemy.png')
    if spell_target_coords is None:
        pygui.alert("High Alchemy Spell picture not found: Open Magic tab.")
        raise ValueError("High Alchemy Spell Button cannot be found")
    # print(spell_target_coords)
    random_move_interval = int(get_random_value(min=42, max=320))
    x = spell_target_coords[0] + 1 + get_random_value(min=0, max=spell_target_coords[2] - 7)
    y = spell_target_coords[1] - 5 + get_random_value(min=0, max=spell_target_coords[3] - 2)

    for click in range(random_move_interval):
        mod = int(random_move_interval / get_random_value(min=10, max=20))
        if click % mod == 0:
            x = spell_target_coords[0] + 1 + get_random_value(min=0, max=spell_target_coords[2] - 7)
            y = spell_target_coords[1] - 5 + get_random_value(min=0, max=spell_target_coords[3] - 2)
        check_pause()
        pygui.moveTo(x, y, duration=get_random_value(min=0.2, max=0.5), tween=pygui.easeInOutQuad)
        pygui.click()
        time.sleep(get_random_value(min=0.48, max=0.76))
        pygui.click()
        check_pause()
        time.sleep(get_random_value(min=1.223, max=1.66))

    print("Finished a run.")
    # check_magic_stats()
    run()


def main():

    start = pygui.confirm("Preparing to bot High Alchemy. Make sure magic tab is open.\n - > Start Botting?")
    clicker = Clicker.Clicker()
    target_coords = pygui.locateOnScreen('buttons/high_alchemy.png')
    if start != 'Cancel':
        while True:
            clicker.run(target=target_coords)


if __name__ == "__main__":
    main()


