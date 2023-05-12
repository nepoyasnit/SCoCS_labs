from src.factory import Factory
from src.constants import JSON_DATA_TYPE, XML_DATA_TYPE
import src.supportive as sup

serializer = Factory.create_serializer(JSON_DATA_TYPE)

numbers = [2, 3, 4, 6]
map_function = map
'../test.json'
with open('../test.json', 'w+') as file:
    json_encoded = serializer.dump(numbers, file=file)
with open('../test.json', 'r') as file:
    json_decoded = serializer.load(file=file)

