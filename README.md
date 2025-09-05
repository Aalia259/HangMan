# HangMan

Introduction:
The goal of the project is to design and implement a full functional program “Hangman using TDD and automated unit testing tools in Python. Hangman is an old school word game where the players goal is to find the missing or phrase based on the level of difficulty (basic/ intermediate). The game includes dynamic word/phrase generation based on difficulty level, automatic life deduction and real-time countdown logic. Tkinter has been used for python`s standard GUI toolkit which natively supports across different platforms.
The key program development strategy Test-Driven development (TDD) has been used with built-in unittest framework. This allowed to write automated tests for core components like countdown timer, word generator dictionary and the game engine “HangManGame”. The process starts with writing the test first before writing actual code and run the test. It fails because the feature doesn’t exist yet. After enough code is written to pass the test. After that refactoring (cleaning code) is done while keeping the test green and testing is repeated for every new feature added. This test methodology provides instant feedback during development process and ensures the changes made don’t break existing functionality.

Process:
Test-Driven Development (TDD):
Test-Driven Development has been applied as a development of core functionality and logics. Each function has first written as test case and then followed up with implementation the code to satisfy the test. Each core module has been built with step by step in a game:
1.	Write test first: The feature was defined before implementation of logic. For example: how the game should display words with/ without blanks, how the letter guessed should be validated or how the timing should be shown. Below code defines expected word display before implementing the logic.
 
 

2.	Run the test: The test will fail with error message. This will happen because the feature is not built yet. This result makes sure that the test is detecting missing functionality correctly. Below is the screenshot showing expected failed test and assertion error.
 
 
3.	Write minimum code to pass the test: Simple logic with minimum code will be implemented to pass the test. Here I used get_display( ) method  in game.py to satisfy the test .
 
 
4.	Repeating and refactoring each feature: After the test pass, each feature will be repeated, and code will be cleaned. This cycle will be applied to all major components: game.py, timer.py and dictionary.py along with handling input. Also, the GUI will be considered as a result of tested logic. Below is the screenshot for multiple passed test results and the Tkinter GUI for the game:
 
 
Automated Unit Testing
Python’s inbuilt framework “unittest” have been used for automated unit testing. It is applied for test_game.py and test_timer.py ensuring the game responds correctly to the players’ guesses and maintains accurate through out the game. 

Test_game.py: verifies correct guesses are revealed and incorrect guesses deduct life by one. Get_display() method is returned with correct word with underscore and letter. Is_won() is returned true when all the letters are guessed correctly and is_lost() triggers when zero lives are left. Also, it makes sure guessed letters are stored and not duplicated. Below is the screenshot for the logic applied:

Test_timer.py: This automated testing makes sure the timer expires after the set time (15 secs) which is the key component. Here timer should not expire prematurely, and valid time out should be displayed. Here the method timed_out = True confirms that the timer is correctly set after specific duration. Has_timed_out () method reliably reports the timer state which results the game loop to response correctly. Real-time time and bug finding has been easier with automated unit testing. Below is the screenshot of test_timer.py and the logic behind it:
 
Conclusion:
This Hangman project was more than just a game- it was a hands-on journey through disciplined software development. By applying Test-Driven Development (TDD) and leveraging Python’s unittest framework, it is ensured that each feature is built with clarity, reliability, and purpose. From validating core game logic to enforcing real-time countdown behavior, automated testing provided the confidence to refactor, extend, and polish the codebase without fear of regressions.
Building both a Command Line Interface (CLI) and a Graphical User Interface (GUI) version allowed to explore different user interaction models and integrating a visual timer using Tkinter’s after () method helped to get into event driven tests. Incorporating static analysis tools like flake8 and pylint helped elevating code quality and align with professional standards.
The game development process, it provided the understanding of modular design, user experience, and the value of clean documentation. More functionality like scoring system, better GUI with Tkinter’s advance features and providing hint system can be implemented in future.

