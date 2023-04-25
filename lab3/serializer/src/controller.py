from constants import JSON_DATA_TYPE, TOML_DATA_TYPE, \
    YAML_DATA_TYPE, UNKNOWN_TYPE_ERROR
from json_serializer import JsonSerializer


class Controller:
    serializer = None

    def __init__(self, data_format):
        if data_format == JSON_DATA_TYPE:
            self.serializer = JsonSerializer()

        elif data_format == YAML_DATA_TYPE:
            pass
            # self.serializer = YamlSerializer()

        elif data_format == TOML_DATA_TYPE:
            pass
            # self.serializer = TomlSerializer()

        else:
            raise Exception(UNKNOWN_TYPE_ERROR)
