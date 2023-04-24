from controller import Controller
from constants import JSON_DATA_TYPE

serializer = Controller(JSON_DATA_TYPE).serializer

def simple_func(a):
    return a * a


print(serializer.dumps(simple_func))
