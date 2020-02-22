from .Observable import Observable

class ObservableList(list):
    def __init__(self, items=[]):
        super().__init__(items)
        self.changed = Observable()

    def append(self, object):
        rv = super().append(object)
        self.changed.emit()
        return rv
    
    def extend(self, iterable):
        rv = super().extend(iterable)
        self.changed.emit()
        return rv

    def remove(self, value):
        rv = super().remove(value) 
        self.changed.emit()
        return rv
    
    def insert(self, index, object):
        rv = super().insert(index, object)
        self.changed.emit()
        return rv
    
    def sort(self, *args, **kwargs):
        rv = super().sort(*args, **kwargs)
        self.changed.emit()
        return rv
    
    def __setitem__(self, key, value):
        rv = super().__setitem__(key, value)
        self.changed.emit()
        return rv


    
