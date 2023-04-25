from controller import Controller
from constants import JSON_DATA_TYPE

serializer = Controller(JSON_DATA_TYPE).serializer


def func(a):
    return a*a


f = serializer.loads(serializer.dumps(func))
print(f(2))
