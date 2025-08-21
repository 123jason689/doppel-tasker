

from vision import capture_screen, image_to_base64_data_uri
from control import CLICK, TYPE, PRESS
from llm_handler import LlamaHandler
from prompt_manager import build_prompt
import time
import re

class Agent:
	def __init__(self, goal: str, rules: list, model_path: str, clip_model_path: str):
		self.goal = goal
		self.rules = rules
		self.model_path = model_path
		self.clip_model_path = clip_model_path
		# The LlamaHandler now manages its own device setup
		self.llm = LlamaHandler(model_path=self.model_path, clip_model_path=self.clip_model_path)

	def run(self):
		print(f"Agent started with goal: {self.goal}")
		while True:
			# 1. Perceive
			img = capture_screen()
			img_data_uri = image_to_base64_data_uri(img)

			# 2. Think
			# Build the text prompt
			text_prompt = build_prompt(self.goal, self.rules)
			# Get the next action from the model
			action_str = self.llm.create_chat_completion(user_prompt=text_prompt, image_data_uri=img_data_uri)
			print(f"Model suggests action: {action_str}")

			# 3. Act
			self.execute_action(action_str)

			# 4. Check for completion
			if action_str.startswith("DONE("):
				print("Task marked as complete by the agent.")
				break

			time.sleep(2) # Wait for UI to update

	def execute_action(self, action: str):
		try:
			if action.startswith("CLICK("):
				match = re.match(r'CLICK\((\d+),\s*(\d+),\s*"(.*)"\)', action, re.DOTALL)
				if match:
					x, y, reason = int(match.group(1)), int(match.group(2)), match.group(3)
					CLICK(x, y, reason)
			elif action.startswith("TYPE("):
				match = re.match(r'TYPE\("(.*)",\s*"(.*)"\)', action, re.DOTALL)
				if match:
					text, reason = match.group(1), match.group(2)
					TYPE(text, reason)
			elif action.startswith("PRESS("):
				match = re.match(r'PRESS\("(.*)",\s*"(.*)"\)', action, re.DOTALL)
				if match:
					key_name, reason = match.group(1), match.group(2)
					PRESS(key_name, reason)
			elif action.startswith("DONE("):
				pass # Handled in the main loop
			else:
				print(f"Warning: Unrecognized or malformed action string: '{action}'")
		except Exception as e:
			print(f"Error executing action '{action}': {e}")
