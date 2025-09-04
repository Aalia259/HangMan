import tkinter as tk
from tkinter import messagebox
from game import HangmanGame
from dictionary import get_random_entry

#gui using tkinter
class HangmanGUI:
    def __init__(self, root):

        #initialize main window and game
        self.root = root
        self.root.title("Hangman Game")
        self.level = tk.StringVar(value="basic")  #stores selected difficulty level
        self.lives = 6

        #timer related variables
        self.timer_label = None
        self.time_remaining = 15
        self.timer_id = None
        self.setup_level_screen()  #level selection screen

    def setup_level_screen(self):
        for widget in self.root.winfo_children(): #clear existing widgets and show difficulty selection
            widget.destroy()
        
        #visual appearance
        self.root.geometry("500x400")
        self.root.eval('tk::PlaceWindow . center')
        self.root.configure(bg="#2e9970")
        
        #UI for level selection (Basic, intermediate)
        tk.Label(self.root, text="Choose Level", font=("Helvetica", 16), bg="purple", fg="white").pack(pady=10)
        tk.Radiobutton(self.root, text="Basic", variable=self.level, value="basic", font=("Helvetica", 12)).pack(pady=5)
        tk.Radiobutton(self.root, text="Intermediate", variable=self.level, value="intermediate", font=("Helvetica", 12)).pack(pady=5)
        tk.Button(self.root, text="Start Game", font=("Helvetica", 12), command=self.start_game).pack(pady=20)

    #clear screen and set up game UI
    def start_game(self):
        self.answer = get_random_entry(self.level.get())
        self.game = HangmanGame(self.answer)
        self.setup_game_screen()

    def setup_game_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
 
        #display entered wird/phrase with underscores
        self.display_label = tk.Label(self.root, text=self.game.get_display(), font=("Courier", 24), bg="#2e9970", fg="white")
        self.display_label.pack(pady=10)
        
        #entry box for guessed letter
        self.lives_label = tk.Label(self.root, text=f"Lives: {self.game.get_lives()}", font=("Helvetica", 14), bg="#2e9970", fg="white")
        self.lives_label.pack()

         #countdown timer
        self.timer_label = tk.Label(self.root, text="Time left: 15s", font=("Helvetica", 14), bg="#2e9970", fg="yellow")
        self.timer_label.pack(pady=5)

        #entry box for letter guessed
        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.guess_entry.pack()
        self.guess_entry.bind("<Return>", self.process_guess)

        #display guessed letters
        self.guessed_label = tk.Label(self.root, text="Guessed: None", font=("Helvetica", 12), bg="#2e9970", fg="white")
        self.guessed_label.pack()

        #start countdown timer
        self.start_timer()

    def start_timer(self):    #reset and start countdown timer
        self.time_remaining = 15
        self.update_timer()

    def update_timer(self):   #update timer label every sec and sheck for timeout
        self.timer_label.config(text=f"Time left: {self.time_remaining}s")
        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            messagebox.showwarning("Timeout", "Time's up! You lost a life.")  #deduct life, check game state after time ran out.
            self.game.lives -= 1
            self.check_game_state()
            self.reset_timer()

    def reset_timer(self):   #cancle existing timer and start new
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        self.start_timer()

    def process_guess(self, event):  #handle players guess input
        guess = self.guess_entry.get().strip().lower()
        self.guess_entry.delete(0, tk.END)

         #validate input
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        
    #reset timer 15 sec after valid guess
        self.reset_timer()

        #update game state based on guess
        result = self.game.guess(guess)
        self.check_game_state()

    def check_game_state(self):

        #update display and check win/lose
        self.display_label.config(text=self.game.get_display())
        self.lives_label.config(text=f"Lives: {self.game.get_lives()}")
        self.guessed_label.config(text=f"Guessed: {', '.join(self.game.get_guessed_letters())}")

        if self.game.is_won():
            messagebox.showinfo("Victory", f"You won! The answer was: {self.answer}")
            self.setup_level_screen()
        elif self.game.is_lost():
            messagebox.showerror("Game Over", f"You lost. The answer was: {self.answer}")
            self.setup_level_screen()
#launch gui
if __name__ == "__main__":
    root = tk.Tk()
    app = HangmanGUI(root)
    root.mainloop()
