"""
Magic hat is a game you can play with your team, where you pick a question out of a hat, as a team building exercise. 
Ask the hat to give you a question.
Ask the hat to ask questions every X seconds.
Ask the hat to turn off the periodic questions
The hat should not repeat questions that have been asked before (unless they've all been asked already)
"""

import random
import threading
import time


class MagicHat:
    """ Create a MagicHat class """

    def __init__(self, question_bank):
        """ 
        Initiate the class with a question_bank, an empty list of already asked questions
        and a thread variable for periodic questions feature.
        """
        self.question_bank = question_bank
        self.asked_questions = []
        self.thread = None  # Start a thread variable to activate periodic questions later

        random.shuffle(self.question_bank)  # Shuffle the list of questions

    def ask(self):
        """ 
        Ask the hat to give a random question 
        """
        # If all the questions have been asked, refill the question_bank
        # by copying questions from the asked_questions list
        if not self.question_bank:
            self.question_bank = self.asked_questions.copy()
            self.asked_questions = []  # Empty the asked_questions list to start a new round
            random.shuffle(self.question_bank)  # Shuffle the list of questions again

        print("Here is your question from the Magic Hat:")
        # Select the last question in the question bank, which is already randomly shuffled.
        # Pop the selected question from the bank and add it to the list of asked_question.
        selected_question = self.question_bank.pop() 
        self.asked_questions.append(selected_question)
        print(selected_question, "\n")

    def ask_at_interval(self, seconds=30):
        """ 
        Ask the hat to give a question every x seconds using
        Python Timer Objects https://docs.python.org/3/library/threading.html#timer-objects.
        The default interval if no argument is provided is 30 seconds
        """
        if seconds < 5:
            print("Please enter a value greater than 4 seconds. For example: mh.ask_at_interval(10).")
        else:
            self.ask()
            self.thread = threading.Timer(seconds, self.ask_at_interval, [seconds])
            self.thread.start()  # Start the thread running periodic questions

    def stop(self):
        """ 
        Ask the hat to stop periodic questions initiated by function ask_at_interval 
        """
        if not self.thread:
            print("You have not asked the Magic Hat to ask periodic questions yet so there is nothing to stop.")
        else:
            print("Sure thing. Magic Hat will stop giving you questions.")
            self.thread.cancel()  # Stop the thread running periodic questions

    def help(self):
        """ Display instructions for user """
        print("USER GUIDE")
        print("- Type mh.ask() if you would like the Magic Hat to give you a question.")
        print("- Type mh.ask_at_interval() if you would like Magic Hat to give you a question every 30 seconds.")
        print("     + To change the interval, type mh.ask_at_interval(x) where x is the number of seconds.")
        print("     + For example: mh.ask_at_interval(15) will ask a question every 15 seconds")
        print("- Type mh.stop() if you would like the Magic Hat to stop periodic questions.")
        print("- Type mh.help() any time to display the user guide again.", "\n")
        







