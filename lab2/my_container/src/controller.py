import re

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

    def remove(self, args):
        if not args:
            print('The key to remove was not entered')
            return

        self._split_keys(args, self._remove_key)

    def _remove_key(self, key: str):
        if self._container.find(key):
            self._container.remove(key)
            print('Key removed successfully')
        else:
            print(f'The key {key} was not found')

    def find(self, args):
        if not args:
            print('Keys to find was not entered')
            return
        self._split_keys(args, self._find_key)

    def _find_key(self, key):
        if self._container.find(key):
            print(f'Key: {key}')
        else:
            print(f'The key {key} was not found')

    def grep(self, args):
        if not args:
            print('Empty regexp')
            return

        try:
            regexp = re.compile(args)
        except re.error:
            print('Incorrect regexp')
            return

        found_keys = self._container.grep(regexp)
        if not found_keys:
            print('Null elements')
            return

        print(' '.join(found_keys))

    def save(self, args):
        if len(self._container) != 0:
            self._container.save()
            print('Saved successfully!')
        else:
            print('Container is empty!')

    def load(self, args):
        self._container.load()
        print('Loaded successfully!')

    def switch(self, args=''):
        if self._container:
            self._request_for_save()

        username = CLI.parse_username()
        self._container = UniqueContainer(username)

        self._request_for_load()

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
        print('\nThe application stopped. Goodbye!')
        exit(0)
