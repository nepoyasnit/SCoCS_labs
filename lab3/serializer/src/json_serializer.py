from constants import PRIMITIVE_TYPES


class JsonSerializer:
    _current_position: int
    _indent: int

    def __init__(self):
        self._current_position = 0
        self._indent = 0

    def load(self, file):
        return self.loads(file.read())

    def loads(self, obj):
        pass

    def dump(self, obj, file):
        file.write(self.dumps(obj))

    def dumps(self, obj):
        return self._convert_to_json_str(obj)

    def _convert_to_json_str(self, obj):
        if isinstance(obj, PRIMITIVE_TYPES):
            return self._serialize_primitives(obj)

        elif isinstance(obj, (list, set, tuple)):
            return self._serialize_collection(obj)

    def _serialize_to_string(self, obj):
        pass

    def _serialize_primitives(self, obj):
        json_string = '\n' + ' ' * self._indent + '{\n'
        json_string += ' ' * self._indent + f'"type": "{type(obj).__name__}"\n'
        json_string += ' ' * self._indent + f'"value": '

        if obj is None:
            json_string += 'null'
        elif isinstance(obj, bool):
            json_string += 'true' if obj else 'false'
        elif isinstance(obj, (int, float)):
            json_string += str(obj)
        elif isinstance(obj, str):
            json_string += f'"{obj}"'

        json_string += '\n' + ' ' * self._indent + '}'
        return json_string

    def _serialize_collection(self, obj):
        json_string = '\n' + ' ' * self._indent + '{\n'
        json_string += ' ' * self._indent + f'"type": "{type(obj).__name__}"\n'
        json_string += ' ' * self._indent + '"value": ['

        self._indent += 4
        for i in obj:
            json_string += self._convert_to_json_str(i) + ','

        if len(json_string) > 1 and json_string[-1] == ',':
            json_string = json_string[:-1]

        self._indent -= 4
        json_string += '\n' + ' ' * self._indent + ']\n' + ' ' * self._indent + '}'

        return json_string

    def _serialize_dict(self, obj):
        pass
