# Magic Hat Game
Ly Nguyen | May 2021 


## Overview
Magic Hat is a game you can play with your team, where you pick a question out of a hat, as a team building exercise. 
- Ask the hat to give you a question.
- Ask the hat to ask questions every X seconds.
- Ask the hat to turn off the periodic questions
The hat should not repeat questions that have been asked before (unless they've all been asked already)

## Question Bank
The question bank is built from the list of 200 questions here: https://conversationstartersworld.com/icebreaker-questions/

Scrape.py file in data folder scrapes the questions from the website and exports
it to question_bank.json to be used in the game.

For convenience, the question_bank.json file is ready to go, and you do not need to run scrape.py.
Should you want to run the file yourself, you will need to install the dependencies 
(Beautiful Soup - a Python package for parsing HTML and XML documents, and Requests - Python HTTP library)

## Installation
The game requires Python3 to run.

[Optional] Install the dependencies if you want to run the scrape.py script.

```buildoutcfg
pip3 install -r requirements.txt
```

Run play_magic_hat.py in Python interactive mode to start the game in the terminal.
```buildoutcfg
python3 -i play_magic_hat.py
```
You can interact with Magic Hat in three ways using the following commands:
- mh.ask() to ask the Magic Hat to give you a random question
- mh.ask_at_interval(x) to ask the Magic Hat to give you a question every x seconds. 
  If x is not provided, the default is 30 seconds. Value x should be greater than or equal to 5 seconds.
- mh.stop() to stop the periodic questions.

Questions will not be repeated unless they have already been asked.