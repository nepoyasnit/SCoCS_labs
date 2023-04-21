

class JsonSerializer:
    _current_position: int

    def __init__(self):
        self._current_position = 0

    def load(self, file):
        return self.loads(file.read())

    def loads(self, obj):
        pass

    def dump(self, obj, file):
        file.write(self.dumps(obj))

    def dumps(self, obj):
        pass
