

import argparse
import os
from agent import Agent
from dotenv import load_dotenv

def read_rules(rules_path):
	if not rules_path or not os.path.exists(rules_path):
		return []
	with open(rules_path, 'r', encoding='utf-8') as f:
		return [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

def main():
	load_dotenv(dotenv_path='.env.local')
	model_path = os.getenv('MULTIMODAL_MODEL')
	clip_model_path = os.getenv("CLIP_MODEL")
	rules_path = os.getenv('RULE_SET')

	parser = argparse.ArgumentParser(description="Autonomous Local AI Agent")
	parser.add_argument('--goal', type=str, required=True, help='Task description for the agent')
	args = parser.parse_args()

	rules = read_rules(rules_path)
	agent = Agent(goal=args.goal, rules=rules, model_path=model_path, clip_model_path=clip_model_path)
	agent.run()

if __name__ == '__main__':
	main()
