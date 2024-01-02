import json
from typing import Any, Dict


def format_value_to_json(data: Any) -> str:
    """Преобразут обьект в формат JSON

    Если обьект - словарь или список, возвращает строку '[complex value]'

    :param data: Обьект Python
    :type data: Any
    :return: Форматированная строка
    :rtype: str
    """
    if isinstance(data, (dict, list)):
        return '[complex value]'
    return json.dumps(data).replace('"', "'")


def check_value_status(value: Dict[str, str]) -> None:
    """Проверяет соответствие статуса допустимому значению

    Если значение недопустимо - возбуждается исключение ValueError
    :param value: Словарь с информацией о значении
    :type value: dict
    :raises ValueError: Если статус не соответствует ожидаемым значениям
    """
    if value['status'] not in ('nested', 'removed', 'added', 'updated',
                               'unchanged'):
        raise ValueError('Unexpected "status" value')


def make_plain(data: Dict[str, Any], path: str = '') -> str:
    """
    Преобразует словарь в плоскую строку

    :param data: Словарь, который нужно преобразовать
    :type data: dict
    :param path: Путь к вложенному элементу (по умолчанию '')
    :type path: str
    :return: Плоская строка
    :rtype: str
    """
    plain = []
    for key, value in data.items():
        check_value_status(value)
        current_path = f"{path}{key}."
        if value['status'] == 'nested':
            plain.append(f"{make_plain(value['value'], current_path)}")
        elif value['status'] == 'removed':
            plain.append(f"Property '{path}{key}' was removed")
        elif value['status'] == 'added':
            plain.append(f"Property '{path}{key}' was added with value: "
                         f"{format_value_to_json(value['value'])}")
        elif value['status'] == 'updated':
            plain.append(f"Property '{path}{key}' was updated. "
                         f"From {format_value_to_json(value['value'])} "
                         f"to {format_value_to_json(value['value_upd'])}")
    return '\n'.join(plain)
