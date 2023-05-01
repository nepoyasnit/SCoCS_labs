from controller import Controller
from constants import JSON_DATA_TYPE, XML_DATA_TYPE
import supportive as sup
from json_serializer import JsonSerializer
import dicttoxml


def a(x):
    return x * x


serializer = JsonSerializer()
f = serializer.loads(serializer.dumps(a))

