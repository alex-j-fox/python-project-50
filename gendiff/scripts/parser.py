import json
import yaml


def parse(file: str):
    """
    Извлекает данные из JSON или YAML файла и преобразует в обьект Python,
    сохраняя булевые значения и None в формате исходного файла.

    :param file: JSON or YAML file
    :type file: str
    :return: Python object
    """
    if file.endswith('.json'):
        return json.load(open(file))
    elif file.endswith(('.yaml', '.yml')):
        return yaml.load(open(file), yaml.Loader)
