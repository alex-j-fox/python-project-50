import argparse
from typing import Dict, Any

import argcomplete

from .formatters.json import make_json
from .formatters.plain import make_plain
from .formatters.stylish import make_stylish
from .get_diff import get_diff
from .parser import parse


def choose_output_format(difference: Dict[str, Any], format: str) -> str:
    """В зависимости от формата вызывает необходимый форматер

    В случае несоответствия формата выбрасывает исключение ValueError
    :param difference: Форматированный словарь
    :type difference: Dict[str, Any]
    :param format: Обьёмный, плоский или JSON
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


def generate_diff(file_path1: str, file_path2: str,
                  format: str = 'stylish') -> str:
    """ Генерирует строку с результатом сравнения двух файлов .json или .yaml

        Возможные варианты вывода:
        stylish - обьемная строка,
        plain - плоский формат вывода,
        JSON формат

        :param file_path1: Путь до файла 1
        :type file_path1: str
        :param file_path2: Путь до файла 2
        :type file_path2: str
        :param format: Обьемный, плоский или JSON (по умолчанию 'stylish')
        :type format: str
        :return: Строковый тип данных
        :rtype: str
        """
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    diff = get_diff(file1, file2)
    return choose_output_format(diff, format)


def parse_command_line():
    """Возвращает аргументы после разбора параметров командной строки"""
    version = "0.1.0"
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two configuration '
                                                 'files and shows a difference.'
                                     )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output: %(choices)s.',
                        choices=['stylish', 'plain', 'json'],
                        default='stylish',
                        metavar='FORMAT')
    parser.add_argument('--version',
                        action='version',
                        help='show %(prog)s version',
                        version='%(prog)s {}'.format(version)
                        )
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
