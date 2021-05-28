"""
Magic hat is a game you can play with your team, where you pick a question out of a hat, as a team building exercise. 
Ask the hat to give you a question.
Ask the hat to ask questions every X seconds.
Ask the hat to turn off the periodic questions
The hat should not repeat questions that have been asked before (unless they've all been asked already)
"""

import random


questions = ["What’s the best thing you’ve got going on in your life at the moment?",
             "What incredibly common thing have you never done?",
             "What has taken you the longest to get good or decent at?"]

class MagicHat:

    def __init__(self, questionbank):
        self.questionbank = questionbank
        self.asked_questions = None

    def give_question(self):
        """ Ask the hat to give a random question """
        print(random.choice(self.questionbank))


magic_hat = MagicHat(questions)



