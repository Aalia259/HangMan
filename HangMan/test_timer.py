#defining restsuite for GuessTimer class
import unittest
import time
from timer import GuessTimer

class TestGuessTimer(unittest.TestCase):
    def test_timer_times_out(self):
        timer = GuessTimer(timeout=2) #creating timer with short timeout(2 secs)
        timer.start()  #start timer in background thread
        time.sleep(3)  #wait longer than 2 secs to ensure it expire
        self.assertTrue(timer.has_timed_out())  #assert the time is out

    def test_timer_does_not_timeout_early(self):
        timer = GuessTimer(timeout=3)  #create timer with longer timeout (3 sec)
        timer.start()  #start timer
        time.sleep(1)  #wait less than timeout duration (1 sec)
        self.assertFalse(timer.has_timed_out())  #assert that timer is not out yet

#run test suite when the file is executed directly.
if __name__ == "__main__":
    unittest.main()