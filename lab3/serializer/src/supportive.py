import inspect
from types import LambdaType, ModuleType

from constants import PRIMITIVE_TYPES, UNKNOWN_TYPE_ERROR


def convert(obj):
    if isinstance(obj, PRIMITIVE_TYPES + (list, tuple, dict, set)):
        return obj
    elif is_iterable(obj):
        return pack_iterable(obj)
    elif is_function(obj):
        return pack_function(obj)
    elif inspect.isclass(obj):
        pass
    elif inspect.iscode(obj):
        pass
    else:
        pass


def pack_function(obj, cls=None):
    unpacked_func = {'__type__': 'function'}

    if inspect.ismethod(obj):
        obj = obj.__func__

    unpacked_func['__name__'] = obj.__name__
    globs = get_global_vars(obj, cls)
    unpacked_func['__globals__'] = pack_iterable(globs)

    args = {}

    for (key, values) in inspect.getmembers(obj.__code__):
        if key.startswith('co_'):
            if isinstance(values, bytes):
                values = list(values)

                if is_iterable(values) and not isinstance(values, str):
                    converted_vals = []

                    for value in values:
                        if value is not None:
                            converted_vals.append(convert(value))
                        else:
                            converted_vals.append(None)

                    args[key] = converted_vals
                    continue
                args[key] = values

    unpacked_func["__args__"] = args

    return unpacked_func


def deconvert(obj):
    if isinstance(obj, PRIMITIVE_TYPES):
        return obj
    elif isinstance(obj, dict):
        if 'function' in obj.values():
            pass
        elif 'object' in obj.values():
            pass
        elif 'class' in obj.values():
            pass
    elif is_iterable(obj):
        return pack_iterable(obj)
    else:
        raise Exception(UNKNOWN_TYPE_ERROR)


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


def get_global_vars(func, cls):
    globs = {}

    for global_var in func.__code__.co_names:
        if global_var in func.__globals__:
            if isinstance(func.__globals__[global_var], types.ModuleType):
                globs[global_var] = func.__globals__[global_var].__name__

            elif inspect.isclass(func.__globals__[global_var]):
                if cls and func.__globals__[global_var] != cls:
                    globs[global_var] = func.__globals__[global_var]

            elif global_var != func.__code__.co_name:
                globs[global_var] = func.__globals__[global_var]

            else:
                globs[global_var] = func.__name__

    return globs
