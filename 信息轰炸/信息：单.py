import pyautogui
import time
import pyperclip

pyautogui.FAILSAFE=False #禁用放故障装置 很重要

time.sleep(3)
x,y = pyautogui.position()
pyautogui.click(x,y)
for i in range(100):
	pyperclip.copy("sb")
	# pyautogui.moveTo(x,y) #可要可不要
	pyautogui.hotkey("ctrl","v")
	pyautogui.press("enter")
	
