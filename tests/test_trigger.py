import sys

sys.path.append('..')

from fservice import state
from fservice import trigger

import time

class Trig(trigger.Trigger):

  def __init__(self):
      super().__init__(name='trig')
    
  def run_start(self):
    print('start trig')
  
  def run_trigger(self):
    print('trigger trig')
  
  def run_stop(self):
    print('stop trig')


if __name__ == "__main__":

  state.register_trigger('trig', Trig)
  state.start_triggers()

  for i in range(10):
    state.update_trigger('trig')
    time.sleep(0.5)
  
  state.stop_triggers()