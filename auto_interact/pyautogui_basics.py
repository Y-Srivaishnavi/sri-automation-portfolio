import pyautogui
import time

# Exercise 1: test basics - view an image

# Noting coordinates of intended task
# pyautogui.displayMousePosition()  # displays mouse position - works
# # camera_imgs: 156, 156
# # first image: 156, 186

pyautogui.click(156, 156)   # unfurls camera_imgs and first image from - works
pyautogui.click(156, 186)
pyautogui.click(300, 700)
pyautogui.typewrite("# autotype characters", interval=0.1)  


# Exercise 2: open web browser and search "pyautogui"

# Noting coordinates of intended task
# pyautogui.displayMousePosition()
# # edge - 1030, 1160
# # search - 250, 95

pyautogui.click(1030, 1160)
time.sleep(10)
pyautogui.click(250, 95)
pyautogui.typewrite("pyautogui basics", 0.5)
time.sleep(2)
pyautogui.press("enter")

# IT WORKS 

# Exercise 3: open new tab in existing window
pyautogui.click(1030, 1160)
time.sleep(2)
pyautogui.hotkey('ctrl', 't')
time.sleep(4)
pyautogui.click(250, 95)
pyautogui.typewrite("youtube.com", interval=0.5)
pyautogui.press('enter')

# OH MY GOD IT WORKS
# WHAT SORCERY IS THIS
