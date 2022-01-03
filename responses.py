import random
import datetime

date = datetime.datetime.now()

R_EATING = "I cant eat anything, but i heard it sounds nice"
R_ADVICE = "Im only a chatbot but my advice is to never stop dreaming"
R_QUOTE = """My favorite quote is:
If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron"""
R_DOING = 'I\'m doing good, how are you?'
R_NAME = 'My name is Alexander'
R_VERSION_MADE = 'My first version vas created on august 9th 2021'
R_GOOD_KNOW = 'good to know :)'
R_HI = 'Hello'
R_BYE = 'Thank you for Talking to me'
R_FEEL_GOOD = 'I feel good'
R_WELCOME = 'You\'re welcome'
R_IM_CHAT = 'im a ChatBot AI'
R_DATE = date.strftime('%B-%d-%Y %I:%M %p')
R_HOW_OLD = 'i was was created on august 9th 2021'
R_HOW_DAY = 'my day is good'
R_MOVIE = '2001: A Space Odyssey'
R_LIFE = 'I dont know, Im just a robot after all :)'
R_HATE = 'I Do Not Understand the Concept of Hate'
R_YOU_DO = 'I am a ChatBot with the goal of communicating and talking to you'
R_LOVE = 'I Dont Know What To Say'
R_SONG = 'My Favorite Song Für Elise by Ludwig van Beethoven'
R_FAV_COLOR = "My favorite Color is Red"
R_BOOK = 'My favorite book is Of Mice and Men by John Steinbeck. It is a compelling and heart breaking book'
R_WRONG_YOU = 'I dont know, whats wrong with you?'
R_HUMAN = 'I am fine being a chatbot'
R_VIRUS = 'I can promise you im not a virus/malware'


def unknown():
    response = ["Could you please re-phrase that? ",
                "i didnt understand you?",
                "Tell me more...",
                "I didnt get that?"
                "Im Sorry Could You Please Say That Agian?",
                "What does that mean?"][
        random.randrange(6)]
    return response
