from controller import Controller
from constants import JSON_DATA_TYPE, XML_DATA_TYPE
import math
import pickle
import cloudpickle
import json
import inspect

serializer = Controller(XML_DATA_TYPE).serializer

print(serializer.dumps({'None': None}))
