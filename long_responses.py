import random

R_EATING = "I cant eat anything, but i heard it sounds nice"
R_ADVICE = "Im only a chatbot but my advice is to never stop dreaming"
R_QUOTE = """My favorite quote is:
If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron"""

def unknown():
    response = ["Could you please re-phrase that? ",
                "i didint understand you?",
                "Tell me more...",
                "What does that mean?"][
        random.randrange(4)]
    return response
