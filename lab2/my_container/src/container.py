import os.path
import pickle
import re


class UniqueContainer:
    _storage: set[str] = set()
    _username: str
    _container_filename: str

    def __init__(self, username: str):
        self._username = username
        self._container_filename = f'./data/{username}_container.dmp'

    def __len__(self):
        return len(self._storage)

    def add(self, key: str):
        self._storage.add(key)

    def list(self):
        return list(self._storage)

    def find(self, key):
        return key in self._storage

    def save(self):
        with open(self._container_filename, 'wb') as file:
            pickle.dump(self._storage, file)

    def load(self):
        with open(self._container_filename, 'rb') as file:
            loaded = pickle.load(file)
            self._storage = self._storage | loaded

    def is_exist(self):
        return os.path.exists(self._container_filename)

    def remove(self, key: str):
        self._storage.remove(key)

    def grep(self, regex):
        return list(filter(lambda key: re.match(regex, key), self._storage))
