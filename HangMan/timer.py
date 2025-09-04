import threading
import time

#define time class to track guessed timeouts
class GuessTimer:
    def __init__(self, timeout=15): #initialize timer with a default timeout value (15 secs)
        self.timeout = timeout   #duration before timeout triggers
        self.timed_out = False   #flag to indicate if time has expired
        self._thread = None   #thread object for running countdown

    def start(self):
        self.timed_out = False   #reset timeout flag before start
        self._thread = threading.Thread(target=self._countdown)
        self._thread.daemon = True  #ensure thread exists when main program ends
        self._thread.start()  #start countdown

    def _countdown(self):
        time.sleep(self.timeout)   #wait for specific duration and set timeout flag
        self.timed_out = True

     #return whether timer has expired
    def has_timed_out(self):
        return self.timed_out