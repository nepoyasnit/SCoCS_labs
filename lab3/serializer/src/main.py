from controller import Controller
from constants import JSON_DATA_TYPE

controller = Controller(JSON_DATA_TYPE)
print(controller.serializer._serialize_dict({'1': 1, '2': 2, '3': 3}))
