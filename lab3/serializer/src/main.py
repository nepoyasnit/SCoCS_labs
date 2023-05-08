from controller import Controller
from constants import JSON_DATA_TYPE, XML_DATA_TYPE
import supportive as sup
from json_serializer import JsonSerializer
from xml_serializer import XmlSerializer
import yaml


def method():
    class A:
        @staticmethod
        def m(x):
            return x * x
    obj = A()
    return obj


data = {
    'Name':'John Doe',
    'Position':'DevOps Engineer',
    'Location':'England',
    'Age':'26',
    'Experience': {'GitHub':'Software Engineer',\
    'Google':'Technical Engineer', 'Linkedin':'Data Analyst'},
    'Languages': {'Markup':['HTML'], 'Programming'\
    :['Python', 'JavaScript','Golang']}
}

def a(x):
    return x*x

converter = XmlSerializer()._converter
print(yaml.dump(converter.convert(a)))
