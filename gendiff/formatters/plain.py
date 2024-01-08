from typing import Any, Dict


def format_value(data: Any) -> str:
    """Преобразут обьект в строку JSON-подобного формата.

    Если обьект - словарь, возвращает строку '[complex value]'
    Если обьект - True или False, возвращает строку 'true' или 'false'
    Если обьект - None, возвращает строку 'null'
    Если обьект - строка, возвращает объект (строку) в одинарных кавычках

    :param data: Обьект Python
    :type data: Any
    :return: Форматированная строка
    :rtype: str
    """
    if isinstance(data, dict):
        return '[complex value]'
    elif isinstance(data, bool):
        return str(data).lower()
    elif data is None:
        return 'null'
    elif isinstance(data, str):
        return f"'{data}'"
    return data


def get_property_change_message(data: Dict[str, Any], path: str) -> str:
    """
    Возвращает строку с сообщением об изменении свойства 'status' элемента

    :param data: Словарь с данными об изменении свойства элемента
    :type data: Dict[str, Any]
    :param path: Путь к свойству элемента в словаре
    :type path: str
    :return: Сообщение об изменении свойства элемента в словаре
    :rtype: str
    """
    key = data['key']
    status = data['status']
    value = data['value']
    if status == 'removed':
        return f"Property '{path}{key}' was removed"
    elif status == 'added':
        return f"Property '{path}{key}' was added with value: " \
               f"{format_value(value)}"
    elif status == 'updated':
        new_value = data['value_upd']
        return f"Property '{path}{key}' was updated. " \
               f"From {format_value(value)} " \
               f"to {format_value(new_value)}"


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
        current_path = f"{path}{key}."
        status = value['status']
        if status == 'nested':
            plain.append(f"{make_plain(value['value'], current_path)}")
        elif status == 'unchanged':
            continue
        elif status != 'unchanged':
            plain.append(get_property_change_message(value, path))
        else:
            raise ValueError('Unexpected "status" value')
    return '\n'.join(plain)
