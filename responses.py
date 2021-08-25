import random
import datetime

date = datetime.datetime.now()
s_date = date.strftime('%B-%d-%Y %I:%M %p')

R_EATING = "I cant eat anything, but i heard it sounds nice"
R_ADVICE = "Im only a chatbot but my advice is to never stop dreaming"
R_QUOTE = """My favorite quote is:
If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron"""
R_DOING = 'I\'m doing good, how are you?'
R_NAME = 'My name is Alexander'
R_VERSION_MADE = 'My first version vas created on august 9th 2021'
R_GOOD_KNOW = 'good to know :)'
R_HI = 'Hello!'
R_BYE = 'Thank you for seeing me today!'
R_FEEL_GOOD = 'I feel good!'
R_WELCOME = 'You\'re welcome!'
R_IM_CHAT = 'im a ChatBot AI'
R_DATE = s_date
R_HOW_OLD = 'i was was created on august 9th 2021'
R_HOW_DAY = 'my day is good!'
R_MOVIE = '2001: A Space Odyssey'
R_LIFE = 'I dont know, Im just a robot after all! :)'
R_HATE = 'I Do Not Understand the Concept of Hate!'
R_ALEX = 'Hi!'

def unknown():
    response = ["Could you please re-phrase that? ",
                "i didint understand you?",
                "Tell me more...",
                "What does that mean?"][
        random.randrange(4)]
    return response
