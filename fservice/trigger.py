import threading
import logging
import time

logger = logging.getLogger(__name__)

class Trigger(threading.Thread):

    def __init__(self, name='trigger'):
        super().__init__(name=name, daemon=True)
        self._stop_event = threading.Event()
        self._stopped = False
        self._has_started = False
        self._block_time = 5E9
        self._trigger = threading.Semaphore(0)


    def run_trigger(self):
        pass


    def try_trigger(self):
        try:
            self.run_trigger()
            return True
        except:
            logger.exception('Unexpected error in trigger')
            return False


    def run(self):
        while not self._stop_event.is_set():
            triggered = self._trigger.acquire(blocking=True, timeout=self._block_time)
            if triggered:
                self.try_trigger()


    def stop(self):
        self._stop_event.set()


    def trigger(self):
        self._trigger.release()


    def is_stopped(self):
        return self._stopped


    def has_started(self):
        return self._has_started