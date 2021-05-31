"""
Magic hat is a game you can play with your team, where you pick a question out of a hat, as a team building exercise. 
Ask the hat to give you a question.
Ask the hat to ask questions every X seconds.
Ask the hat to turn off the periodic questions
The hat should not repeat questions that have been asked before (unless they've all been asked already)
"""

import random, threading
import time


questions = ["What’s the best thing you’ve got going on in your life at the moment?",
             "What incredibly common thing have you never done?",
             "What has taken you the longest to get good or decent at?",
             "abc",
             "xyz",
             "lmnop"]

# random.shuffle(questions)

class MagicHat:


    def __init__(self, question_bank):
        self.question_bank = question_bank
        random.shuffle(self.question_bank) #Shuffle the list of questions
        self.unasked_questions = question_bank.copy()
        self.thread = None # Start a thread variable to activate periodic questions later
        self.asked_questions = None


    def ask(self):
        """ Ask the hat to give a random question """
        # Restock the questions if all the questions have been asked
        if not self.unasked_questions:
            self.unasked_questions = self.question_bank.copy()
            random.shuffle(self.unasked_questions) # Shuffle the list of unasked questions again

        print("Here is your question from the Magic Hat:")
        print(self.unasked_questions.pop(), "\n")


    def ask_at_interval(self, seconds=30):
        """ 
        Ask the hat to give a question every x seconds using
        Python Timer Objects https://docs.python.org/3/library/threading.html#timer-objects.
        The default interval if no argument is provided is 30 seconds
        """   
        self.ask()
        self.thread = threading.Timer(seconds, self.ask_at_interval, [seconds])
        self.thread.start() #Start the thread running periodic questions
        
    def stop(self):
        """ Ask the hat to stop periodic questions initiated by function ask_at_interval """
        if not self.thread:
            print("You have not asked the Magic Hat to ask periodic questions yet so there is nothing to stop.")
        else:
            self.thread.cancel() #Stop the thread running periodic questions

mh = MagicHat(questions)







