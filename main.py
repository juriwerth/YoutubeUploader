###########################################################################
# 👤 github.com/juriwerth 
###########################################################################
# 🟢 Imports

import pyautogui
import keyboard
import time

from credentails import *

###########################################################################
# 📝 Main

def uploading(n: int):
    for _ in range(n):

        pyautogui.moveTo(1765, 110, 1)
        pyautogui.click()
        pyautogui.moveTo(1765, 155, 1)
        pyautogui.click()
        pyautogui.moveTo(pyautogui.size()[0]/2, pyautogui.size()[1]/2, 1)
        pyautogui.click()
        time.sleep(.5)

        # Uploading

        pyautogui.write(video)
        pyautogui.moveTo(pyautogui.size()[0]/2 - 150, pyautogui.size()[1]/2 - 40, 1)
        pyautogui.click()
        time.sleep(.5)
        pyautogui.press("enter")
        time.sleep(5)

        # Video Settings
        pyautogui.click()
        keyboard.write(description)
        pyautogui.moveTo(1385, 950, 1)
        pyautogui.click()
        pyautogui.moveTo(1385, 950, 1)
        pyautogui.click()
        pyautogui.moveTo(1385, 950, 1)
        pyautogui.click()
        time.sleep(.5)
        pyautogui.moveTo(585, 550, 1)
        pyautogui.click()
        time.sleep(.5)
        pyautogui.moveTo(1385, 950, 1)
        pyautogui.click()
        time.sleep(1.5)
        pyautogui.moveTo(1150, 700, 1)
        time.sleep(1)
        pyautogui.click()

def setup():
    # Opening browser
    pyautogui.hotkey("win", "r")
    pyautogui.write(browser, interval=.1)
    pyautogui.press("enter")
    time.sleep(1)

    # Opening login screen 
    pyautogui.write(link)
    pyautogui.press("enter")
    time.sleep(1.5)

    # Loggin in (email)
    keyboard.write(mail)
    pyautogui.press("enter")
    time.sleep(.75)

    # Logging in (password)
    pyautogui.write(password, interval=.1)
    pyautogui.press("enter")
    time.sleep(.5)

if __name__ == "__main__":
    num_of_vids = int(input("How many videos do you wan't to upload?\n"))
    setup()
    uploading(num_of_vids)