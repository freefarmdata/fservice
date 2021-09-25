# fservice

A stateful threaded management service.

### What am I?

fservice is a lib that can be used to create applications with
dependable lifecycles. Similar to React.js, you can define your services
with a starting, looping, updating, and ending cycle. For example:

```python
from fservice.tservice import TService
from fservice import state

class MyComponent(TService):

    def __init__(self):
        super().__init__(self, name="MyComponent")
        self.set_interval(1E9) # in nano seconds

    def run_start(self):
        print('componentDidMount')
    
    def run_loop(self):
        print('render')
    
    def run_update(self, update):
        print('componentDidUpdate', update)
    
    def run_end(self):
        print('componentDidUnmount')

state.register_service('my_component', MyComponent)
state.start_services()
```

Or, you can setup triggers that you can send messages to. For instance,
to notify another part of the app that an event has occured. The trigger
uses a fast FIFO deque and a Semaphore for thread safe communication. For example:

```python
from fservice.trigger import Trigger
from fservice import state

class MyTrigger(Trigger):

    def __init__(self):
        super().__init__(name="MyTrigger")

    def run_trigger(self, message):
        print(f'something just happened: {message}')

state.register_trigger('my_trigger', MyTrigger)
state.start_triggers()

state.update_trigger('my_trigger', { 'hello': 'world' })
```