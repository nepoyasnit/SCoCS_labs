import numbers
from collections.abc import Iterable
from xml.dom.minidom import parseString


class XmlSerializer:
    @classmethod
    def dumps(cls, obj):
        return cls._convert_to_xml_string(obj)

    @classmethod
    def dump(cls, file, obj):
        file.write(cls.dumps(obj))

    @classmethod
    def loads(cls, obj):
        pass

    @classmethod
    def load(cls, file, obj):
        pass

    @classmethod
    def _convert_to_xml_string(cls, obj, root=True, xml_declaration=True, include_encoding=True,
                               encoding='UTF-8', custom_root='root', return_bytes=True,
                               ids=False, cdata=False, attr_type=True):
        xml_string = []
        addline = xml_string.append
        if root:
            if xml_declaration:
                if not include_encoding:
                    addline('<?xml version="1.0" ?>')
                else:
                    addline('<?xml version="1.0" encoding="%s" ?>' % encoding)
            addline('<%s>%s</%s>' % (
                custom_root,
                cls._convert(obj, ids, attr_type, cdata, parent=custom_root),
                custom_root
            ))
        else:
            addline(cls._convert(obj, ids, attr_type, cdata, parent=''))

        if not return_bytes:
            return ''.join(xml_string)
        return ''.join(xml_string).encode('utf-8')

    @classmethod
    def _convert(cls, obj, ids, attr_type, cdata, parent):
        item_name = 'item'

        if obj is None:
            return cls._convert_none(item_name, obj, attr_type, cdata)
        if type(obj) == bool:
            return cls._convert_bool(item_name, obj, attr_type, cdata)
        if isinstance(obj, numbers.Number) or type(obj) == str:
            return cls._convert_kv(item_name, obj, attr_type, cdata)
        if hasattr(obj, 'isoformat'):
            return cls._convert_kv(item_name, obj.isoformat(), attr_type, cdata)
        if isinstance(obj, dict):
            return cls._convert_dict(obj, ids, parent, attr_type, item_name, cdata)
        if isinstance(obj, Iterable):
            return cls._convert_iterable(obj, ids, parent, attr_type, item_name, cdata)
        raise TypeError('Unsupported data type: %s (%s)' % (obj, type(obj).__name__))

    @classmethod
    def _convert_bool(cls, key, value, attr_type, cdata=False, attr=None):
        pass

    @classmethod
    def _convert_kv(cls, key, value, attr_type, cdata=False, attr=None):
        pass

    @classmethod
    def _convert_dict(cls, obj, ids, parent, attr_type, item_func, cdata):
        pass

    @classmethod
    def _convert_iterable(cls, items, ids, parent, attr_type, item_func, cdata):
        pass

    @classmethod
    def _convert_none(cls, key, value, attr_type, cdata=False, attr=None):
        if attr is None:
            attr = {}

        key, attr = cls._make_valid_xml_name(key, attr)

        if attr_type:
            attr['type'] = cls._get_xml_type(value)
        attr_string = cls._make_attr_string(attr)
        return '<%s%s></%s>' % (key, attr_string, key)

    @classmethod
    def _make_valid_xml_name(cls, key, attr):
        key = cls._escape_xml(key)
        attr = cls._escape_xml(attr)

        if cls._key_is_valid_xml(key):
            return key, attr
        if str(key).isdigit():
            return 'n%s' % key, attr

        try:
            return 'n%s' % (float(str(key))), attr
        except ValueError:
            pass

        if cls._key_is_valid_xml(key.replace(' ', '_')):
            return key.replace(' ', '_'), attr

        attr['name'] = key
        key = 'key'
        return key, attr

    @staticmethod
    def _key_is_valid_xml(key):
        test_xml = '<?xml version="1.0" encoding="UTF-8" ?><%s>foo</%s>' % (key, key)
        try:
            parseString(test_xml)
            return True
        except Exception:
            return False

    @classmethod
    def _escape_xml(cls, string):
        if type(string) in str:
            string = cls._unicode_me(string)
            string = string.replace('&', '&amp;')
            string = string.replace('"', '&quot;')
            string = string.replace('\'', '&apos;')
            string = string.replace('<', '&lt;')
            string = string.replace('>', '&gt;')
        return string

    @staticmethod
    def _unicode_me(val):
        try:
            return str(val, 'utf-8')
        except:
            return str(val)

    @staticmethod
    def _get_xml_type(val):
        if type(val).__name__ == 'NoneType':
            return 'null'
        elif type(val).__name__ == 'bool':
            return 'bool'
        elif type(val).__name__ == 'str':
            return 'str'
        elif type(val).__name__ == 'int':
            return 'int'
        elif type(val).__name__ == 'float':
            return 'float'
        elif isinstance(val, numbers.Number):
            return 'number'
        elif isinstance(val, dict):
            return 'dict'
        elif isinstance(val, Iterable):
            return 'list'

        return type(val).__name__

    @staticmethod
    def _make_attr_string(attr):
        attr_string = ' '.join(['%s="%s"' % (k, v) for k, v in attr.items()])
        return '%s%s' % (' ' if attr_string != '' else '', attr_string)



