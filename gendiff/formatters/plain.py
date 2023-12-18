import json


def format_value_to_json(data: any) -> str:
    """Преобразут обьект в json формат

    Если обьект - словарь или список, возвращает строку '[complex value]'

    :param data: Обьект Python
    :type data: any
    :return: Форматированная строка
    :rtype: str
    """
    if isinstance(data, (dict, list)):
        return '[complex value]'
    return json.dumps(data).replace('"', "'")


def make_plain(data: [dict, any], path: str = '') -> str:
    """
    Преобразует словарь в обьемную строку

    :param data: Словарь
    :param path: Путь к вложенному элементу
    :return: Обьемная строка
    """
    plain = []
    for key, value in data.items():
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
