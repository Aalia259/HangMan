import unittest
from game import HangmanGame

#Defining testsuit for a HangmanGame class.
class TestHangmanGame(unittest.TestCase):

     #test that display shows underscore for each letter in the word.
    def test_initial_display(self):
        game = HangmanGame("python")
        self.assertEqual(game.get_display(), "_ _ _ _ _ _")

     #test that correct guessed letter reveals in the display.
    def test_correct_guess(self):
        game = HangmanGame("python")
        game.guess('p')
        self.assertEqual(game.get_display(), "p _ _ _ _ _")

     #test that wrong guess deducts life by 1.
    def test_wrong_guess(self):
        game = HangmanGame("python")
        initial_lives = game.get_lives()
        game.guess('z')
        self.assertEqual(game.get_lives(), initial_lives - 1)

     #test that repeating same wrong letter twice doesnt deduct extra lives.
    def test_repeated_guess_does_not_affect_lives(self):
        game = HangmanGame("python")
        game.guess('x')
        lives_after_first = game.get_lives()
        game.guess('x')  # repeated wrong guess.
        self.assertEqual(game.get_lives(), lives_after_first)

     #test that the game is won when all letters are guessed.
    def test_win_condition(self):
        game = HangmanGame("python")
        for letter in "python":
            game.guess(letter)
        self.assertTrue(game.is_won())
        self.assertFalse(game.is_lost())

     #test that game is lost when lives are zero.
    def test_loss_condition(self):
        game = HangmanGame("python", lives=4)
        for letter in ['a', 'b', 'c', 'd']:   #all wrong guesses.
            game.guess(letter)
        self.assertTrue(game.is_lost())
        self.assertFalse(game.is_won())

     #test that space in phrases are preserved in display.
    def test_display_with_phrase(self):
        game = HangmanGame("unit test")
        self.assertEqual(game.get_display(), "_ _ _ _   _ _ _ _")

     #test that guessed letters are tracked and returned in sorted order
    def test_guessed_letters_tracking(self):
        game = HangmanGame("python")
        game.guess('p')
        game.guess('x')
        self.assertEqual(game.get_guessed_letters(), ['p', 'x'])

# run the test when the file is exrecuted directly.
if __name__ == "__main__":
    unittest.main()