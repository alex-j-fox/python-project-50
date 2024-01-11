from itertools import chain
from typing import Dict, Any


def get_stylish_value(value: Any, depth: int, replacer: str = ' ',
                      spaces_count: int = 4) -> str:
    """
        Формирует строковое представление значения в JSON-подобном формате.

        :param value: Значение, которое нужно отформатировать
        :type value: Any
        :param depth: Текущая глубина рекурсии
        :type depth: int
        :param replacer: Символ-заполнитель перед строкой (по умолчанию ' ')
        :type replacer: str
        :param spaces_count: Количество повторений 'replacer' (по умолчанию 4)
        :type spaces_count: int
        :return: Строковое представление значения в JSON-подобном формате
        :rtype: str
        """
    if isinstance(value, dict):
        line = []
        indent = replacer * spaces_count
        for key, val in value.items():
            line.append(f'\n{indent * (depth + 1)}{key}: '
                        f'{get_stylish_value(val, depth + 1)}')
        stylish_value = chain('{', line, ['\n', indent * depth, '}'])
        return ''.join(stylish_value)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


def make_line(data: Dict[str, Any], depth: int, prefix: str = '  ',
              key: str = 'value', indent: str = '  ') -> str:
    """
    Формирует строку для отображения значения в структуре диффа.

    :param data: Словарь с данными
    :type data: dict
    :param depth: Текущая глубина рекурсии
    :type depth: int
    :param prefix: Префикс для строки (по умолчанию '  ')
    :type prefix: str
    :param key: Ключ для получения значения из словаря (по умолчанию 'value')
    :type key: str
    :param indent: Строка с отступом (по умолчанию '  ')
    :type indent: str
    :return: Строка для отображения значения в структуре диффа
    :rtype: str
    """
    line = f'{indent * depth}{prefix}{data["key"]}: ' \
           f'{get_stylish_value(data[key], depth + 1)}'
    return line


def get_volumetric_line(data: Dict[str, Any], depth: int, indent: str) -> str:
    """
    В зависимости от статуса изменений формирует строку для отображения
    значения в структуре диффа.

    :param data: Словарь с данными
    :type data: dict
    :param depth: Текущая глубина рекурсии
    :type depth: int
    :param indent: Строка с отступом
    :type indent: str
    :return: Строка для отображения значения в структуре диффа
    :rtype: str
    """
    status = data['status']
    if status == 'removed':
        return f'{indent}{make_line(data, depth, "- ")}'
    elif status == 'added':
        return f'{indent}{make_line(data, depth, "+ ")}'
    elif status == 'updated':
        return f'{indent}{make_line(data, depth, "- ")}\n' \
               f'{indent}{make_line(data, depth, "+ ", "value_upd")}'
    elif status == 'unchanged':
        return f'{indent}{make_line(data, depth)}'
    else:
        raise ValueError('Unexpected "status" value')


def make_stylish(data: Dict[str, Any], replacer: str = ' ',
                 spaces_count: int = 2) -> str:
    """Преобразует словарь в обьемную строку.

    :param data: Словарь
    :type data: Dict[str, Any]
    :param replacer: Символ-заполнитель перед строкой (по умолчанию ' ')
    :type replacer: str
    :param spaces_count: Количество повторов 'replacer' (по умолчанию 2)
    :type spaces_count: int
    :return: Обьемная строка
    :rtype: str
    """

    def walk(node, depth):
        indent = replacer * spaces_count * (depth + 1)
        shifted_indent = indent * spaces_count
        lines = []
        for k, v in node.items():
            status = v['status']
            value = v['value']
            if status == 'nested':
                lines.append(f'{shifted_indent}{k}: {walk(value, depth + 1)}')
            else:
                lines.append(get_volumetric_line(v, depth, indent))
        stylish = chain('{', lines, ["    " * depth + '}'])
        return '\n'.join(stylish)

    return walk(data, 0)
