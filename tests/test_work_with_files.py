import unittest
from lab3.serializer.src.factory import Factory

VALUE = -21
VALUES_LIST = [11, 22, 33, 44]
DATA_DIR_PATH = '../tests/test_data/'

json_serializer = Factory.create_serializer('.json')
xml_serializer = Factory.create_serializer('.xml')


def simple_func():
    return 17


def recursion_func(x):
    if x < 2:
        return 1
    return recursion_func(x - 1) * x


class TestClass:
    value = 23

    def method(self):
        return self.value * self.value


class TestObjectsFromFile(unittest.TestCase):
    def test_primitive(self):
        with open(DATA_DIR_PATH + 'test_primitive.json', 'w+') as file:
            json_serializer.dump(obj=VALUE, file=file)
        with open(DATA_DIR_PATH + 'test_primitive.json', 'r') as file:
            json_decoded = json_serializer.load(file=file)

        with open(DATA_DIR_PATH + 'test_primitive.xml', 'w+') as file:
            xml_encoded = xml_serializer.dump(obj=VALUE, file=file)
        with open(DATA_DIR_PATH + 'test_primitive.xml', 'r') as file:
            xml_decoded = xml_serializer.load(file=file)

        return self.assertEqual(VALUE, json_decoded, xml_decoded)

    def test_list(self):
        with open(DATA_DIR_PATH + 'test_list.json', 'w+') as file:
            json_serializer.dump(obj=VALUES_LIST, file=file)
        with open(DATA_DIR_PATH + 'test_list.json', 'r') as file:
            json_decoded = json_serializer.load(file=file)

        with open(DATA_DIR_PATH + 'test_list.xml', 'w+') as file:
            xml_encoded = xml_serializer.dump(obj=VALUES_LIST, file=file)
        with open(DATA_DIR_PATH + 'test_list.xml', 'r') as file:
            xml_decoded = xml_serializer.load(file=file)

        return self.assertEqual(VALUES_LIST, json_decoded, xml_decoded)

    def test_function(self):
        with open(DATA_DIR_PATH + 'test_function.json', 'w+') as file:
            json_serializer.dump(obj=simple_func, file=file)
        with open(DATA_DIR_PATH + 'test_function.json', 'r') as file:
            json_decoded = json_serializer.load(file=file)

        with open(DATA_DIR_PATH + 'test_function.xml', 'w+') as file:
            xml_encoded = xml_serializer.dump(obj=simple_func, file=file)
        with open(DATA_DIR_PATH + 'test_function.xml', 'r') as file:
            xml_decoded = xml_serializer.load(file=file)

        return self.assertEqual(simple_func(), json_decoded(), xml_decoded())

    def test_recursive_function(self):
        with open(DATA_DIR_PATH + 'test_recursion.json', 'w+') as file:
            json_serializer.dump(obj=recursion_func, file=file)
        with open(DATA_DIR_PATH + 'test_recursion.json', 'r') as file:
            json_decoded = json_serializer.load(file=file)

        with open(DATA_DIR_PATH + 'test_recursion.xml', 'w+') as file:
            xml_encoded = xml_serializer.dump(obj=recursion_func, file=file)
        with open(DATA_DIR_PATH + 'test_recursion.xml', 'r') as file:
            xml_decoded = xml_serializer.load(file=file)

        return self.assertEqual(recursion_func(3), recursion_func(3), recursion_func(3))

    def test_class(self):
        with open(DATA_DIR_PATH + 'test_class.json', 'w+') as file:
            json_serializer.dump(obj=TestClass, file=file)
        with open(DATA_DIR_PATH + 'test_class.json', 'r') as file:
            json_decoded = json_serializer.load(file=file)

        with open(DATA_DIR_PATH + 'test_class.xml', 'w+') as file:
            xml_encoded = xml_serializer.dump(obj=TestClass, file=file)
        with open(DATA_DIR_PATH + 'test_class.xml', 'r') as file:
            xml_decoded = xml_serializer.load(file=file)

        return self.assertEqual(TestClass().method(), TestClass().method(), TestClass().method())

    def test_object(self):
        obj = TestClass()
        with open(DATA_DIR_PATH + 'test_object.json', 'w+') as file:
            json_serializer.dump(obj=obj, file=file)
        with open(DATA_DIR_PATH + 'test_object.json', 'r') as file:
            json_decoded = json_serializer.load(file=file)

        with open(DATA_DIR_PATH + 'test_object.xml', 'w+') as file:
            xml_encoded = xml_serializer.dump(obj=obj, file=file)
        with open(DATA_DIR_PATH + 'test_object.xml', 'r') as file:
            xml_decoded = xml_serializer.load(file=file)

        return self.assertEqual(obj.method(), json_decoded.method(), xml_decoded.method())

