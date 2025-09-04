from game import HangmanGame
from dictionary import get_random_entry
from inputimeout import inputimeout, TimeoutOccurred

def choose_level():
    """
    Prompt the user to choose a difficulty level: basic or intermediate.
    Returns the corresponding level string.
    """
    while True:
        print("\nChoose difficulty level:")
        print("  a. Basic (single word)")
        print("  b. Intermediate (phrase)")
        choice = input("Enter 'a' or 'b': ").strip().lower()
        if choice == 'a':
            return "basic"
        elif choice == 'b':
            return "intermediate"
        else:
            print("Invalid input. Please enter 'a' or 'b'.")

def play_game():
    """
    Main game loop for Hangman. Handles level selection, input timeout,
    guess validation, and win/loss conditions.
    """
    print("Welcome to Hangman!")
    level = choose_level()  #get difficulty level from player
    answer = get_random_entry(level)   #get random word or phrase from dictionary
    game = HangmanGame(answer)      #initialize game logic

    #loop until player lose, win or quit
    while not game.is_won() and not game.is_lost():
        print(f"\n Word: {game.get_display()}")  #display current stat of game
        print(f"Lives remaining: {game.get_lives()}")
        guessed = game.get_guessed_letters()
        print(f"Letters guessed: {', '.join(guessed) if guessed else 'None'}")

        try:
            # Enforce 15-second input timeout
            guess = inputimeout(prompt="Enter a letter (15s, or type 'quit' to exit): ", timeout=15).strip()
        except TimeoutOccurred:
            print("Time's up! You lost a life.")
            game.lives -= 1
            continue
        #allow user to quit the game
        if guess.lower() == "quit":
            print("You quit the game.")
            break
 
        #imput should be single alphabet letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet letter.")
            continue

        #process input and update game state
        if game.guess(guess):
            print("Correct guess!")
        else:
            print("Wrong guess. Life deducted.")

    #final message
    print("\n Game Over.")
    if game.is_won():
        print(f"You won! The answer was: '{answer}'")
    elif game.is_lost():
        print(f"You lost. The answer was: '{answer}'")

#entry point for the scripts
if __name__ == "__main__":
    play_game()