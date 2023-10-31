# Screenshot com PyautoGUI

import pyautogui
import time


while True:

    pyautogui.screenshot(f"print{time.time()}.png")
    time.sleep(2)