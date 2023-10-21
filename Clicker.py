import pyautogui as pygui
from pyHM import mouse
import keyboard
import random
import time


class Clicker:

    def __init__(self):
        self.last_key = None
        self.last_pause: int = 0

    def pause(self):
        output = pygui.confirm("Auto Clicker Paused, Continue?")
        if output == 'Cancel':
            exit()
        self.last_pause = self.last_key.time

    def check_pause(self):
        if self.last_key and self.last_key.name == 'B' and self.last_pause < self.last_key.time:
            self.pause()

    def on_key_press(self, event):
        self.last_key = event

    @staticmethod
    def get_random_value(low: float, high: float) -> float:
        return random.uniform(low, high)

    def run(self, target, name: str = "RuneScape Clicker"):

        # Capture keyboard press for pausing using 'B/b'
        keyboard.on_press(self.on_key_press)

        target_coords = target
        if target_coords is None:
            pygui.alert(f"{name} picture not found: Read docs. Exiting.")
            raise ValueError("Target not found on screen.")

        random_interval = int(self.get_random_value(low=42, high=320))
        x = int(target_coords[0] + 1 + self.get_random_value(low=0, high=target_coords[2] - 7))
        y = int(target_coords[1] - 5 + self.get_random_value(low=0, high=target_coords[3] - 2))

        # Each iteration is a cast of high alchemy
        for click in range(random_interval):

            self.check_pause()
            mod = int(random_interval / self.get_random_value(low=10, high=20))

            # Change x, y and y randomly.
            if click % mod == 0:
                x = int(target_coords[0] + 1 + self.get_random_value(low=0, high=target_coords[2] - 7))
                y = int(target_coords[1] - 5 + self.get_random_value(low=0, high=target_coords[3] - 2))

            # Click on Spell.
            if pygui.position() != (x, y):
                mouse.move(x, y, multiplier=self.get_random_value(low=1.0, high=8.5))
            pygui.click()

            # Random Pause
            time.sleep(self.get_random_value(low=0.48, high=0.76))

            # Click on Willow Longbow Stack.
            if pygui.position() != (x, y):
                mouse.move(x, y, multiplier=self.get_random_value(low=1.0, high=8.5))
            pygui.click()

            time.sleep(self.get_random_value(low=1.123, high=1.66))
