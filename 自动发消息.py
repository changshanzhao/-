import time
import random
import pyautogui
txt = "测试，请勿回复"
time.sleep(3)
for _ in range(10):
    pyautogui.typewrite(txt)
    pyautogui.press("enter")
    time.sleep(2)