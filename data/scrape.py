import requests
from bs4 import BeautifulSoup
import re  # regular expression
import json


# Set the URL to scrape the questions from
URL = 'https://conversationstartersworld.com/icebreaker-questions/'

# Connect to the URL
response = requests.get(URL)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# Use regular expression to find all p tags whose texts contain a number followed
# by a period in the text, indicating that these are questions (eg: 1. and 123.)
question_p_tags = soup.findAll('p', text=re.compile('\d+\.'))

# A list of questions
questions = []

for p_tag in question_p_tags:
    text = p_tag.get_text()  # Extract the text from the p_tag
    text = re.sub(r'\d+\.+ ', '', text)  # Remove the number & the period before the question
    questions.append(text)


# Export the question to a json file to use in the game
question_bank = {'questions': questions}

out_file = open("data/question_bank.json", "w")
json.dump(question_bank, out_file, indent=4)
out_file.close()


# REFERENCES
# https://stackoverflow.com/questions/866000/using-beautifulsoup-to-find-a-html-tag-that-contains-certain-text
# https://realpython.com/beautiful-soup-web-scraper-python/#find-elements-by-class-name-and-text-content
# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460
