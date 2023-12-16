import json
import yaml


def parse(file: [json, yaml]) -> dict:
    """
    Преобразует данные из JSON или YAML файла в обьект Python.

    :param file: JSON or YAML file
    :type file: str
    :return: Python object
    """
    if file.endswith('.json'):
        return json.load(open(file))
    elif file.endswith(('.yaml', '.yml')):
        return yaml.safe_load(open(file))
