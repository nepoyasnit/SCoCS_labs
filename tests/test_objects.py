import math
import unittest
from lab3.serializer.src.factory import Factory

JSON_DATATYPE = '.json'
XML_DATATYPE = '.xml'

json_serializer = Factory.create_serializer(JSON_DATATYPE)
xml_serializer = Factory.create_serializer(XML_DATATYPE)

iterator = iter([11, 22, 33, 44])

VALUE = -12
VALUES_LIST = [11, 22, 33, 44]
VALUES_TUPLE = (11, 22, 33, 44)
VALUES_DICT = {'11': 11, '22': 22, '33': 33}
BYTE_VALUE = bytes(3)
PI = math.pi


def generator():
    yield 11
    yield 22
    yield 33
    yield 44
    

class TestIterator(unittest.TestCase):
    def test_iterator(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(iterator))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(iterator))

        result = [11, 22, 33, 44]
        json_result = list(json_decoded)
        xml_result = list(xml_decoded)

        return self.assertSequenceEqual(result, json_result, xml_result)

    def test_generator(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(generator))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(generator))

        result = [11, 22, 33, 44]
        json_result = list(json_decoded())
        xml_result = list(xml_decoded())

        return self.assertSequenceEqual(result, json_result, xml_result)


class TestSimpleObjects(unittest.TestCase):
    def test_value(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(VALUE))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(VALUE))

        return self.assertEqual(VALUE, json_decoded, xml_decoded)

    def test_list(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(VALUES_LIST))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(VALUES_LIST))

        return self.assertEqual(VALUES_LIST, json_decoded, xml_decoded)

    def test_tuple(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(VALUES_TUPLE))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(VALUES_TUPLE))

        return self.assertEqual(VALUES_TUPLE, json_decoded, xml_decoded)

    def test_dict(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(VALUES_TUPLE))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(VALUES_TUPLE))

        return self.assertEqual(VALUES_TUPLE, json_decoded, xml_decoded)

    def test_bytes(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(BYTE_VALUE))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(BYTE_VALUE))

        return self.assertEqual(BYTE_VALUE, json_decoded, xml_decoded)

    def test_PI(self):
        json_decoded = json_serializer.loads(json_serializer.dumps(PI))
        xml_decoded = xml_serializer.loads(xml_serializer.dumps(PI))

        return self.assertEqual(PI, json_decoded, xml_decoded)
