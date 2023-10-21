import pyautogui as pygui
import keyboard
import random
import time

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
    target_coords = pygui.locateOnScreen('buttons/camelot_teleport.png')
    if target_coords is None:
        pygui.alert("Camelot picture not found: Open Magic tab.")
        raise ValueError("Camelot teleport button cannot be found")
    random_move_interval = int(get_random_value(min=42, max=320))
    mod = int(random_move_interval / get_random_value(min=10, max=20))
    x = target_coords[0] + get_random_value(min=0, max=target_coords[2])
    y = target_coords[1] + get_random_value(min=0, max=target_coords[3])

    for click in range(random_move_interval):
        if click % mod == 0:
            x = target_coords[0] + get_random_value(min=0, max=target_coords[2])
            y = target_coords[1] + get_random_value(min=0, max=target_coords[3])
        check_pause()
        pygui.moveTo(x, y, duration=get_random_value(min=0.3, max=0.6), tween=pygui.easeInOutQuad)
        pygui.click()
        check_pause()

        time.sleep(get_random_value(min=1.50, max=1.66))

    print("Finished a run.")
    # check_magic_stats()
    run()


def main():

    start = pygui.confirm("Preparing to bot Camelot Teleport. Make sure magic tab is open.\n - > Start Botting?")
    if start != 'Cancel':
        run()


if __name__ == "__main__":
    main()


