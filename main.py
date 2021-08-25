import re
import responses as respo
from art import *
import datetime
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
    
    response(respo.R_DATE, ['whats', 'the', 'date', 'times', 'time'], single_response=True)
    response(respo.R_HI, ['hello', 'hi', 'hey', 'sup', 'heyo', 'yo'], single_response=True)
    response(respo.R_BYE, ['bye', 'goodbye'], single_response=True)
    response(respo.R_FEEL_GOOD, ['how', 'do', 'you', 'feel'], required_words=['feel', 'you'])
    response(respo.R_HOW_OLD, ['how', 'old', 'are', 'you'], required_words=['old'])
    response(respo.R_DOING, ['how', 'doing', 'are'], required_words=['you'])
    response(respo.R_NAME, ['what', 'is', 'your', 'name'], required_words=['name'])
    response('your name is ' + name, ['what', 'is', 'my', 'name'], required_words=['my','name'])
    response(respo.R_WELCOME, ['thank', 'thanks'], single_response=True)
    response(respo.R_IM_CHAT, ['what', 'are', 'yo u'], required_words=['are'])
    response(respo.R_HOW_DAY, ['how', 'is', 'your', 'day'], required_words=['your', 'day'])
    response(respo.R_GOOD_KNOW, ['im', 'doing', 'happy', 'great', 'sad', 'mad', 'joyfull', 'anger', 'angry', 'joy', 'good', 'fine'], single_response=True)
    response(respo.R_VERSION_MADE, ['when', 'you', 'were', 'you', 'made', 'created'], single_response=True)
    response(respo.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(respo.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(respo.R_QUOTE, ['tell', 'give', 'me', 'a', 'quote'], required_words=['quote'])
    response(respo.R_MOVIE, ['your', 'favorite', 'movie'], required_words=['movie'])
    response(respo.R_LIFE, ['the', 'meaning', 'of', 'life'], required_words=['life'])
    response(respo.R_HATE, ['I','Hate', 'hate', 'you'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    return respo.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

tprint("Alexander")
input("Press Enter To Setup Alexander: ")
# setup Alexander
print("Setting Up Alexander...")
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))
for i in range(toolbar_width):
    time.sleep(0.1)
    sys.stdout.write("▓")
    sys.stdout.flush()
sys.stdout.write("]\n")
name = input("Enter Your Name: ")
print(f"Hello {name}, my name is Alexander. I'll be your chatbot today.")

while True:
    try:
        print('Alexander: ' + get_response(input(f'{name}: ')))

    except:
        print("Error!!!")
