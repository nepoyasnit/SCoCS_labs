from constants import JSON_DATA_TYPE, TOML_DATA_TYPE, \
    YAML_DATA_TYPE, UNKNOWN_TYPE_ERROR, XML_DATA_TYPE
from json_serializer import JsonSerializer
from yaml_serializer import YamlSerializer
from xml_serializer import XmlSerializer


class Controller:
    serializer = None

    def __init__(self, data_format):
        if data_format == JSON_DATA_TYPE:
            self.serializer = JsonSerializer()

        elif data_format == XML_DATA_TYPE:
            self.serializer = XmlSerializer()

        elif data_format == YAML_DATA_TYPE:
            self.serializer = YamlSerializer()

        elif data_format == TOML_DATA_TYPE:
            pass
            # self.serializer = TomlSerializer()

        else:
            raise Exception(UNKNOWN_TYPE_ERROR)
