from magic_hat_class import MagicHat
import json


""" 
Run this file in interactive mode in Python3 to play the Magic Hat game
python3 -i play_magic_hat.py
"""

# Get the question bank
with open('data/question_bank.json') as f:
    data = json.load(f)
    question_bank = data['questions']

# Create an instance of the MagicHat class using the question bank
mh = MagicHat(question_bank)

print("Welcome to the Magic Hat game!", "\n")

# Display the user guide showing different commands to interact with the game
mh.help()


