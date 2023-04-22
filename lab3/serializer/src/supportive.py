import inspect
from types import LambdaType

from constants import PRIMITIVE_TYPES


def convert(obj):
    if isinstance(obj, PRIMITIVE_TYPES + (list, tuple, dict, set)):
        return obj
    elif is_iterable(obj):
        return pack_iterable(obj)
    elif is_function(obj):
        pass
    elif inspect.isclass(obj):
        pass
    elif inspect.iscode(obj):
        pass
    else:
        pass


def is_function(obj):
    return inspect.isfunction(obj) or inspect.ismethod(obj) or isinstance(obj, LambdaType)


def is_iterable(obj):
    return bool(getattr(obj, '__iter__', None))


def pack_iterable(obj):
    if isinstance(obj, (list, tuple, set)):
        packed_iterable = []

        for value in obj:
            packed_iterable.append(convert(value))

        if isinstance(obj, tuple):
            return tuple(packed_iterable)
        if isinstance(obj, set):
            return set(packed_iterable)
        return packed_iterable

    elif isinstance(obj, dict):
        packed_dict = {}

        for key, value in obj.items():
            packed_dict[key] = convert(value)
        return packed_dict

