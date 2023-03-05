from container import UniqueContainer


class ContainerController:
    _container: UniqueContainer = None

    def __init__(self):
        self.switch()

    @staticmethod
    def _split_keys(keys: str, function: callable):
        for key in keys.split():
            function(key)

    def add(self, args: str):
        if not args:
            print('Nothing to add!')
            return

        self._split_keys(args, self._container.add)
        print('Successfully added!')

    def list(self):
        pass

    def remove(self):
        pass

    def find(self):
        pass

    def grep(self):
        pass

    def save(self, args):
        self._container.save()
        print('Saved successfully!')

    def load(self, args):
        self._container.load()
        print('Loaded successfully!')

    def switch(self):
        username = input('Enter your name: ')
        self._container = UniqueContainer(username)

    def exit(self):
        pass
