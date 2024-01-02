import json
from typing import Dict, Any


def encode_boolean_and_none_value_in_dict(dictionary: Dict[str, Any]) -> None:
    """
        Encodes Boolean and None dictionary values into JSON format.

        :param dictionary:
        :type dictionary: Dict[str, Any]
        :return: None
        """
    for key, value in dictionary.items():
        if isinstance(value, bool) or value is None:
            dictionary[key] = json.dumps(value)


def get_value(dictionary: Dict[str, Any]) -> Dict[str, Any]:
    """Получает из словаря значения с заданным ключом.

    :param dictionary: Словарь
    :type dictionary: Dict[str, Any]
    :return:
    :rtype: Dict[str, Any]
    """
    key = dictionary['key']
    status = dictionary['status']
    value = dictionary['value']
    if status == 'removed':
        return {f'- {key}': value}
    elif status == 'added':
        return {f'+ {key}': value}
    elif status == 'updated':
        new_value = dictionary['value_upd']
        return {f'- {key}': value, f'+ {key}': new_value}
    elif status == 'unchanged':
        return {f'  {key}': value}


def get_stylish_dict(diff: Dict[str, Any]) -> Dict[str, Any]:
    """Преобразует сортированный обьединенный словарь двух исходных словарей.

        {
          "- key1": "value1",
          "+ key2": None,
          "  key3": 23,
          "  key4": {
            ...,
            }
        }
    где
    '-' - ключ отсутствует во втором исходном словаре или имеет другое значение,
    '+' - ключ отсутствует в первом исходном словаре или имеет другое значение,
    ' ' - ключ с идентичным значением есть в обоих словарях или имеет вложенный
    обьект словаря с различиями

    :param diff: Словарь
    :type diff: Dict[str, Any]
    :return: Форматированный словарь
    :rtype: Dict[str, Any]
    """
    stylish_dict = {}
    for v in diff.values():
        if v['status'] not in ('nested', 'removed', 'added', 'updated',
                               'unchanged'):
            raise ValueError('Unexpected "status" value')
        if v["status"] == 'nested':
            stylish_dict[f'  {v["key"]}'] = get_stylish_dict(v["value"])
        else:
            stylish_dict.update(get_value(v))
    encode_boolean_and_none_value_in_dict(stylish_dict)
    return stylish_dict


def make_stylish(data: Dict[str, Any], replacer: str = ' ',
                 spaces_count: int = 4) -> str:
    """Преобразует словарь в обьемную строку.

    :param data: Словарь
    :type data: Dict[str, Any]
    :param replacer: Символ-заполнитель перед строкой (по умолчанию ' ')
    :type replacer: str
    :param spaces_count: Количество повторов 'replacer' (по умолчанию 4)
    :type spaces_count: int
    :return: Обьемная строка
    :rtype: str
    """
    stylish = ['{']

    def walk(sub: Dict[str, Any], depth: int) -> None:
        indent = spaces_count * depth
        shifted_indent = indent - 2
        for key, value in sub.items():
            if key.startswith((' ', '-', '+')):
                indent = shifted_indent
            if not isinstance(value, dict):
                stylish.append(f'{replacer * indent}{key}: {str(value)}')
            else:
                stylish.append(f'{replacer * indent}{key}: {"{"}')
                walk(value, depth + 1)
                stylish.append(f'{replacer * (shifted_indent + 2)}{"}"}')

    walk(get_stylish_dict(data), 1)
    stylish.append('}')
    return '\n'.join(stylish)
