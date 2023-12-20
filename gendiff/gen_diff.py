import argparse

import argcomplete

from .formatters.json import make_json
from .formatters.plain import make_plain
from .formatters.stylish import get_stylish_dict
from .formatters.stylish import make_stylish
from .get_diff import get_diff
from .parser import parse


def generate_diff(file_path1, file_path2, format: str = 'stylish') -> str:
    """
        Генерирует обьемную строку с результатом сравнения двух файлов .json
        или .yaml в заданном формате (stylish, plain, json).

        :param file_path1: Путь до файла 1
        :type file_path1: str
        :param file_path2: Путь до файла 2
        :type file_path2: str
        :param format: Обьемный, плоский или JSON
        :type format: str
        :return:
        :rtype: str
        """
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    diff = get_diff(file1, file2)
    if format == 'stylish':
        return make_stylish(get_stylish_dict(diff))
    elif format == 'plain':
        return make_plain(diff)
    elif format == 'json':
        return make_json(diff)


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
