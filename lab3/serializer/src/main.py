from controller import Controller
from constants import JSON_DATA_TYPE

serializer = Controller(JSON_DATA_TYPE).serializer

print(serializer.loads(serializer.dumps({1: '1', 2: '2'})))
