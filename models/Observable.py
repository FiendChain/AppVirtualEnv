class Observable:
    def __init__(self):
        self.listeners = set([])

    def connect(self, listener):
        self.listeners.add(listener)
    
    def disconnect(self, listener):
        self.listeners.discard(listener)

    def emit(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)