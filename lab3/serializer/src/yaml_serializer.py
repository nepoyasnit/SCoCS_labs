

class YamlSerializer:
    @staticmethod
    def dumps(obj):
        pass

    @staticmethod
    def dump(obj, file):
        file.write(YamlSerializer.dumps(obj))

    @staticmethod
    def loads(obj):
        pass

    @staticmethod
    def load(file):
        return YamlSerializer.loads(file.read())
