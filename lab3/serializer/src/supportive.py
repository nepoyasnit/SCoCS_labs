import builtins
import inspect
from types import LambdaType, ModuleType, CodeType, WrapperDescriptorType, \
    MethodDescriptorType, BuiltinFunctionType, MappingProxyType, \
    GetSetDescriptorType, FunctionType

from constants import PRIMITIVE_TYPES, UNKNOWN_TYPE_ERROR


def convert(obj):
    if isinstance(obj, PRIMITIVE_TYPES + (list, tuple, dict, set)):
        return obj
    elif is_iterable(obj):
        return pack_iterable(obj)
    elif is_function(obj):
        a = pack_function(obj)
        return a
    elif inspect.isclass(obj):
        return pack_class(obj)
    elif inspect.iscode(obj):
        return pack_inner_function(obj)
    else:
        return pack_object(obj)


def pack_inner_function(obj):
    return pack_function(FunctionType(obj, {}))


def pack_object(obj):
    packed_object = {'__type__': 'object', '__class__': pack_class(obj.__class__), 'attr': {}}

    for key, value in inspect.getmembers(obj):
        if not key.startswith('__') and not is_function(value):
            packed_object['attr'][key] = convert(value)

    return packed_object


def pack_class(obj):
    packed_class = {'__type__': 'class', '__name__': obj.__name__}

    for attr in inspect.getmembers(obj):
        if attr[0] not in (
                '__mro__', '__base__', '__basicsize__',
                '__class__', '__dictoffset__', '__name__',
                '__qualname__', '__text_signature__', '__itemsize__',
                '__flags__', '__weakrefoffset__', '__objclass__'
        ) and type(attr[1]) not in (
                WrapperDescriptorType, MethodDescriptorType,
                BuiltinFunctionType, MappingProxyType,
                GetSetDescriptorType
        ):
            attr_value = getattr(obj, attr[0])

            packed_class[attr[0]] = convert(attr_value)

            packed_class['__bases__'] = [pack_class(base) for base in obj.__bases__ if base != object]
            return packed_class


def unpack_class(obj):
    class_bases = tuple(unpack_class(base) for base in obj['__bases__'])
    class_methods = {}

    for attr, value in obj.items():
        class_methods[attr] = deconvert(value)

    unpacked_class = type(obj['__name__'], class_bases, class_methods)

    for key, method in class_methods.items():
        if inspect.isfunction(method):
            method.__globals__.update({unpacked_class.__name__: unpacked_class})

    return unpacked_class


def pack_function(obj, cls=None):
    packed_func = {'__type__': 'function'}

    if inspect.ismethod(obj):
        obj = obj.__func__

    packed_func['__name__'] = obj.__name__
    globs = get_global_vars(obj, cls)
    packed_func['__globals__'] = pack_iterable(globs)

    args = {}
    for (key, values) in inspect.getmembers(obj.__code__):
        if key.startswith('co_') and key != 'co_lines':
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

    packed_func["__args__"] = args
    return packed_func


def unpack_function(obj):
    arguments = obj["__args__"]
    globs = obj["__globals__"]
    globs["__builtins__"] = builtins

    for key in obj["__globals__"]:
        if key in arguments["co_names"]:
            try:
                globs[key] = __import__(obj["__globals__"][key])
            except:
                if globs[key] != obj["__name__"]:
                    globs[key] = deconvert(obj["__globals__"][key])

    coded = CodeType(arguments['co_argcount'],
                     arguments['co_posonlyargcount'],
                     arguments['co_kwonlyargcount'],
                     arguments['co_nlocals'],
                     arguments['co_stacksize'],
                     arguments['co_flags'],
                     bytes(arguments['co_code']),
                     tuple(arguments['co_consts']),
                     tuple(arguments['co_names']),
                     tuple(arguments['co_varnames']),
                     arguments['co_filename'],
                     arguments['co_name'],
                     arguments['co_firstlineno'],
                     bytes(arguments['co_lnotab']),
                     tuple(arguments['co_freevars']),
                     tuple(arguments['co_cellvars']))

    func_result = FunctionType(coded, globs)
    func_result.__globals__.update({func_result.__name__: func_result})

    return func_result


def deconvert(obj):
    if isinstance(obj, PRIMITIVE_TYPES):
        return obj
    elif isinstance(obj, dict):
        if 'function' in obj.values():
            return unpack_function(obj)
        elif 'object' in obj.values():
            return unpack_object(obj)
        elif 'class' in obj.values():
            return unpack_class(obj)
    elif is_iterable(obj):
        return unpack_iterable(obj)
    else:
        raise Exception(UNKNOWN_TYPE_ERROR)


def unpack_object(obj):
    obj_class = deconvert(obj['__class__'])
    attrs = {}

    for key, value in obj['attr'].items():
        attrs[key] = deconvert(value)

    unpacked_obj = object.__new__(obj_class)
    unpacked_obj.__dict__ = attrs

    return unpacked_obj


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


def unpack_iterable(obj):
    if isinstance(obj, (list, tuple, set)):
        unpacked_iterable = []

        for value in obj:
            unpacked_iterable.append(deconvert(value))

        if isinstance(obj, tuple):
            return tuple(unpacked_iterable)
        if isinstance(obj, set):
            return set(unpacked_iterable)

        return unpacked_iterable


def get_global_vars(func, cls):
    globs = {}

    for global_var in func.__code__.co_names:
        if global_var in func.__globals__:
            if isinstance(func.__globals__[global_var], ModuleType):
                globs[global_var] = func.__globals__[global_var].__name__

            elif inspect.isclass(func.__globals__[global_var]):
                if cls and func.__globals__[global_var] != cls:
                    globs[global_var] = func.__globals__[global_var]

            elif global_var != func.__code__.co_name:
                globs[global_var] = func.__globals__[global_var]

            else:
                globs[global_var] = func.__name__

    return globs
