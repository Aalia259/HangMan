class HangmanGame:
    def __init__(self, answer, lives=6):
        self.answer = answer.lower()   #answer will be stored in lowercase for consistency.
        self.display = ['_' if c.isalpha() else c for c in answer] #create the display as underscores for letters, keep non-letters.
        self.guessed = set()   #track entered letters to prevent duplicates.
        self.lives = lives     #set number or lives the player has.

    def get_display(self):
        return ' '.join(self.display)   #return current state of word or phrase with space between characters.

    # Return false if already guessed
    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed:
            return False  
        self.guessed.add(letter) #add letter to the set of guessed letters.
        if letter in self.answer:  #reveal all the positions of word if the letters are in the answer.
            for i, c in enumerate(self.answer):
                if c == letter:
                    self.display[i] = letter
            return True
        else:
            self.lives -= 1   #life deduct for a wrong guess.
            return False

    def is_won(self):
        return '_' not in self.display   #game won if no underscore left.

    def is_lost(self):
        return self.lives <= 0     #game over if lives reach 0.

    def get_lives(self):
        return self.lives     #returns current number of lives.

    def get_guessed_letters(self):
        return sorted(self.guessed)    #returns sorted list of guessed letters. 
    
    