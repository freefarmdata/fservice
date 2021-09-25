import threading
import logging
import time
from collections import deque

logger = logging.getLogger(__name__)

class Trigger(threading.Thread):

    def __init__(self, name='trigger'):
        super().__init__(name=name, daemon=True)
        self._stop_event = threading.Event()
        self._stopped = False
        self._has_started = False
        self._block_time = 5
        self._trigger = threading.Semaphore(0)
        self._queue = deque()

    
    def set_max_queue_size(self, max_size):
        self._queue = deque(maxlen=max_size)

    
    def set_block_time(self, block_time):
        self._block_time = block_time


    def run_start(self):
        pass


    def run_trigger(self, message):
        pass

    
    def run_end(self):
        pass


    def try_start(self):
        self._has_started = True
        try:
            self.run_start()
            return True
        except:
            logger.exception('Unexpected error in start')
            self._stopped = True
            return False
    

    def try_end(self):
        try:
            self.run_end()
        except:
            logger.exception('Unexpected error in end')
        self._stopped = True


    def try_trigger(self):
        try:
            self.run_trigger(self._queue.pop())
            return True
        except:
            logger.exception('Unexpected error in trigger')
            return False


    def run(self):
        if not self.try_start():
            return

        while not self._stop_event.is_set():
            triggered = self._trigger.acquire(timeout=self._block_time)
            if triggered:
                self.try_trigger()
        self.try_end()


    def stop(self):
        self._stop_event.set()


    def trigger(self, message=None):
        self._queue.appendleft(message)
        self._trigger.release()


    def is_stopped(self):
        return self._stopped


    def has_started(self):
        return self._has_started