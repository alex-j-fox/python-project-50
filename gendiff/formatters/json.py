import json
from typing import Dict, Any


def make_json(data: Dict[str, Any]) -> str:
    """
    Преобразует словарь в форматированную строку JSON.

    :param data: Словарь, который нужно преобразовать в JSON
    :type data: Dict[str, any]
    :return: Форматированная строка JSON
    :rtype: str
    """
    return json.dumps(data, indent=4)
