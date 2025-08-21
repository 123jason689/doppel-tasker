
import pyautogui
import time

def CLICK(x: int, y: int, reason: str = ""):
	"""
	Move mouse to (x, y) and perform a single left-click.
	"""
	try:
		print(f"CLICK({x}, {y}): {reason}")
		pyautogui.moveTo(x, y)
		time.sleep(0.1)
		pyautogui.click()
	except Exception as e:
		print(f"CLICK error: {e}")

def TYPE(text: str, reason: str = ""):
	"""
	Type the given string using the keyboard.
	"""
	try:
		print(f'TYPE("{text}"): {reason}')
		pyautogui.typewrite(text)
	except Exception as e:
		print(f"TYPE error: {e}")

def PRESS(key_name: str, reason: str = ""):
	"""
	Press a special key (e.g., 'enter', 'esc', 'win').
	"""
	try:
		print(f'PRESS("{key_name}"): {reason}')
		pyautogui.press(key_name)
	except Exception as e:
		print(f"PRESS error: {e}")
