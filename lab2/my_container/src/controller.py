from container import UniqueContainer
from cli import CLI


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
            print('Nothing to add')
            return

        self._split_keys(args, self._container.add)
        print('Successfully added!')

    def list(self, args):
        container_list = self._container.list()

        if not container_list:
            print('Container is empty!')
            return

        print(' '.join(container_list))

    def remove(self):
        pass

    def find(self):
        pass

    def grep(self):
        pass

    def save(self, args):
        if len(self._container) != 0:
            self._container.save()
            print('Saved successfully!')
        else:
            print('Container is empty!')

    def load(self, args):
        self._container.load()
        print('Loaded successfully!')

    def switch(self):
        username = CLI.parse_username()
        self._container = UniqueContainer(username)

    def _request_for_save(self):
        user_answer = input('Do you want to save container? (y/n): ')

        if user_answer.lower() in ['yes', 'y']:
            self._container.save()

    def _request_for_load(self):
        user_answer = input('Do you want to load container? (y/n): ')

        if user_answer.lower() in ['yes', 'y']:
            self._container.load()

    def exit(self, args):
        self._request_for_save()
        print('\nThe application is stopped. Goodbye!')
        exit(0)
