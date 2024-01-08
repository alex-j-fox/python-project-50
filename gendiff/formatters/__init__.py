from typing import Dict, Any

from gendiff.formatters.json import make_json
from gendiff.formatters.plain import make_plain
from gendiff.formatters.stylish import make_stylish


def format_difference(difference: Dict[str, Any], format: str) -> str:
    """В зависимости от формата вызывает необходимый форматер

    В случае несоответствия формата выбрасывает исключение ValueError
    :param difference: Форматированный словарь
    :type difference: Dict[str, Any]
    :param format: 'stylish', 'plain', 'json'
    :type format: str
    :return: Строковый тип данных
    :rtype: str
    :raises ValueError: Если формат не соответствует ожидаемому
    """
    if format == 'stylish':
        return make_stylish(difference)
    elif format == 'plain':
        return make_plain(difference)
    elif format == 'json':
        return make_json(difference)
    else:
        raise ValueError('Incorrect argument value')
