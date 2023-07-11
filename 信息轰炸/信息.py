import pyautogui
import time
import pyperclip
import random

pyautogui.FAILSAFE=False #禁用放故障装置 很重要

yuan = [#这里写句子，每个句子用英文逗号隔开" , "

]

time.sleep(3)
x,y = pyautogui.position()
pyautogui.click(x,y)
for i in range(5):
	# pyperclip.copy(random.choice(yuan))
	pyperclip.copy(yuan[0])
	# pyautogui.moveTo(x,y) #可要可不要
	pyautogui.hotkey("ctrl","v")
	pyautogui.press("enter")
	
