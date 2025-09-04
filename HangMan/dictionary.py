import random

#create a dictionarty for the random list of words and phrases for both levels
WORDS = ["python", "hangman", "developer", "keyboard", "function"]
PHRASES = ["unit testing", "open source", "code review", "object oriented"]

#if player enters basic, start basic level.
def get_random_entry(level="basic"):
    if level == "basic":
        return random.choice(WORDS)
    #if player enters intermediate level, start inter level.
    elif level == "intermediate":
        return random.choice(PHRASES)
    
#raise error handling
    else:
        raise ValueError("Invalid level. Choose 'basic' or 'intermediate'.")