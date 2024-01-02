import json
import pathlib
from typing import Any

import yaml


def parse(path_to_file: str) -> Any:
    """
    Преобразует локальный JSON или YAML файл в объект Python.

    :param path_to_file: Путь к объекту
    :type path_to_file: str
    :return: Обьект Python
    :rtype: Any
    """
    extension = pathlib.Path(path_to_file).suffix
    return deserialize(open(path_to_file), extension)


def deserialize(data: Any, extension: str) -> Any:
    """
    Преобразует данные из JSON или YAML файла в обьект Python.

    :param data: Данные для преобразования
    :type data: Any
    :param extension: Расширение файла '.json' или '.yaml'
    :type extension: str
    :return: Преобразованный Python объект
    :rtype: Any
    :raises ValueError: Если расширение файла недопустимо
    """
    if extension == '.json':
        return json.load(data)
    elif extension in ('.yaml', '.yml'):
        return yaml.safe_load(data)
    else:
        raise ValueError('Invalid file extension')
