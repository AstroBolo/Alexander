import re
import long_responses as long
from art import *
import time
import sys

toolbar_width = 30

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', 'yo'], single_response=True)
    response('Thank you for seeing me today!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, how are you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('My name is Alexander', ['what', 'is', 'your', 'name'], required_words=['name'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('good to know :)', ['happy', 'sad', 'mad', 'joyfull', 'anger', 'angry', 'joy', 'good', 'fine'], single_response=True)
    response('My first version vas created on august 9th 2021', ['when', 'were', 'you', 'made', 'created'], single_response=True)

    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_QUOTE, ['tell', 'give', 'me', 'a', 'quote'], required_words=['quote'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
tprint("Alexander")
input("Press Enter To Setup Alexander: ")
# setup Alexander
print("Setting Up Alexander...")
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))
for i in range(toolbar_width):
    time.sleep(0.5)
    sys.stdout.write("▓")
    sys.stdout.flush()
sys.stdout.write("]\n")
print("Hello, my name is Alexander. I'll be your chatbot today.")

while True:
    print('Alexander: ' + get_response(input('You: ')))
