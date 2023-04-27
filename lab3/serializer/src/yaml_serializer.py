from supportive import convert, deconvert
import yaml


class YamlSerializer:
    @staticmethod
    def dumps(obj):
        return yaml.dump(convert(obj))

    @staticmethod
    def dump(obj, file):
        file.write(YamlSerializer.dumps(obj))

    @staticmethod
    def loads(obj):
        return deconvert(yaml.load(obj, Loader=yaml.FullLoader))

    @staticmethod
    def load(file):
        return YamlSerializer.loads(file.read())
