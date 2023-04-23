from constants import PRIMITIVE_TYPES, UNKNOWN_TYPE_ERROR, INT_JSON_TYPE,\
    FLOAT_JSON_TYPE, BOOL_JSON_TYPE, STR_JSON_TYPE, DICT_JSON_TYPE, \
    SET_JSON_TYPE, TUPLE_JSON_TYPE, LIST_JSON_TYPE, NONETYPE_JSON

from supportive import convert, deconvert


class JsonSerializer:
    _current_position: int
    _indent: int

    def __init__(self):
        self._current_position = 0
        self._indent = 0

    def load(self, file):
        return self.loads(file.read())

    def loads(self, obj):
        self._current_position = 0
        return deconvert(self._deconvert_from_string(obj))

    def dump(self, obj, file):
        file.write(self.dumps(obj))

    def dumps(self, obj):
        return self._convert_to_json_str(convert(obj))

    def _convert_to_json_str(self, obj):
        if isinstance(obj, PRIMITIVE_TYPES):
            return self._serialize_primitives(obj)

        elif isinstance(obj, (list, set, tuple)):
            return self._serialize_collection(obj)

        elif isinstance(obj, dict):
            return self._serialize_dict(obj)

        else:
            raise Exception(UNKNOWN_TYPE_ERROR)

    def _deconvert_from_string(self, string_obj):
        self._current_position = string_obj.find('"type":', self._current_position)

        if self._current_position != -1:
            self._current_position += len('"type": ')

        if self._current_position >= len(string_obj) or self._current_position == -1:
            return
        if string_obj[self._current_position:self._current_position + len(INT_JSON_TYPE)] == INT_JSON_TYPE:
            self._current_position += len(INT_JSON_TYPE + '\n')
            return self._deserialize_num(string_obj)
        if string_obj[self._current_position:self._current_position + len(FLOAT_JSON_TYPE)] == FLOAT_JSON_TYPE:
            self._current_position += len(FLOAT_JSON_TYPE + '\n')
            return self._deserialize_num(string_obj)
        if string_obj[self._current_position:self._current_position + len(BOOL_JSON_TYPE)] == BOOL_JSON_TYPE:
            self._current_position += len(BOOL_JSON_TYPE + '\n')
            return self._deserialize_bool(string_obj)
        if string_obj[self._current_position:self._current_position + len(NONETYPE_JSON)] == NONETYPE_JSON:
            self._current_position += len(NONETYPE_JSON + '\n')
            return self._deserialize_null(string_obj)
        if string_obj[self._current_position:self._current_position + len(STR_JSON_TYPE)] == STR_JSON_TYPE:
            self._current_position += len(STR_JSON_TYPE + '\n')
            return self._deserialize_string(string_obj)
        if string_obj[self._current_position:self._current_position + len(DICT_JSON_TYPE)] == DICT_JSON_TYPE:
            self._current_position += len(DICT_JSON_TYPE + '\n')
            return self._deserialize_dict(string_obj)
        if string_obj[self._current_position:self._current_position + len(LIST_JSON_TYPE)] == LIST_JSON_TYPE or \
                string_obj[self._current_position:self._current_position + len(SET_JSON_TYPE)] == SET_JSON_TYPE or \
                string_obj[self._current_position:self._current_position + len(TUPLE_JSON_TYPE)] == TUPLE_JSON_TYPE:
            self._current_position += 1
            index_end = string_obj.find('"', self._current_position)
            collection_type = string_obj[self._current_position: index_end]
            self._current_position = index_end + 1

            return self._deserialize_collection(string_obj, collection_type)

        raise Exception(UNKNOWN_TYPE_ERROR)

    def _deserialize_collection(self, obj, object_type):
        self._current_position = obj.find('"value":', self._current_position) + len('"value": ')

        unpacked_collection = []
        self._current_position += 1

        while self._current_position < len(obj) and obj[self._current_position] != ']':
            if obj[self._current_position] in (' ', ',', '\n'):
                self._current_position += 1
                continue

            value = self._deconvert_from_string(obj)
            unpacked_collection.append(value)
        self._current_position = obj.find('}', self._current_position) + 1

        if object_type == 'tuple':
            return tuple(unpacked_collection)
        elif object_type == 'set':
            return set(unpacked_collection)
        return unpacked_collection

    def _deserialize_dict(self, obj):
        self._current_position = obj.find('"value":', self._current_position) + len('"value": ')
        unpacked_dict = {}

        self._current_position += 1
        while self._current_position < len(obj) and obj[self._current_position] != '}':
            if obj[self._current_position] in (' ', ',', ':', '\n'):
                self._current_position += 1
                continue

            key = self._deconvert_from_string(obj)
            value = self._deconvert_from_string(obj)

            unpacked_dict[key] = value

        self._current_position = obj.find('}', self._current_position + 1) + 1

        return unpacked_dict

    def _deserialize_string(self, obj):
        self._current_position = obj.find('"value":', self._current_position) + len('"value": ')

        unpacked_string = ''
        self._current_position += 1
        while self._current_position < len(obj) and obj[self._current_position:self._current_position + 1] not in '"\n':
            unpacked_string += obj[self._current_position]
            self._current_position += 1
        self._current_position = obj.find('}', self._current_position) + 1

        return unpacked_string

    def _deserialize_num(self, obj):
        self._current_position = obj.find('"value": ', self._current_position) + len('"value": ')
        position = self._current_position
        while self._current_position < len(obj) and \
                (obj[self._current_position].isdigit() or
                 obj[self._current_position] == '.' or
                 obj[self._current_position] == '-'):
            self._current_position += 1

        result_num = obj[position:self._current_position]
        self._current_position = obj.find('}', self._current_position) + 1
        return float(result_num) if '.' in str(result_num) else int(result_num)

    def _deserialize_bool(self, obj):
        self._current_position = obj.find('"value":', self._current_position) + len('"value": ')

        if obj[self._current_position:self._current_position + 4] == 'true':
            self._current_position = obj.find('}', self._current_position)
            return True
        else:
            self._current_position = obj.find('}', self._current_position) + 1
            return False

    def _deserialize_null(self, obj):
        self._current_position = obj.find('"value":', self._current_position) + len('"value": ')
        self._current_position = obj.find('}', self._current_position) + 1
        return None

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
        json_string = '\n' + ' ' * self._indent + '{\n'
        json_string += ' ' * self._indent + f'"type": "{type(obj).__name__}"\n'
        json_string += ' ' * self._indent + '"value": {'

        self._indent += 4

        for key, value in obj.items():
            json_string += self._convert_to_json_str(key) + ': ' + self._convert_to_json_str(value) + ', \n'

        if len(json_string) > 1 and json_string[-3] == ',':
            json_string = json_string[:-3]

        json_string += '\n' + ' ' * self._indent + '}\n'
        self._indent -= 4
        json_string += ' ' * self._indent + '}'

        return json_string
