from controller import Controller
from constants import JSON_DATA_TYPE, XML_DATA_TYPE
import math
import pickle
import cloudpickle
import json
import inspect
import dicttoxml

serializer = Controller(XML_DATA_TYPE).serializer

print(serializer.dumps(1))
xml = dicttoxml.dicttoxml(1)
print(xml)

