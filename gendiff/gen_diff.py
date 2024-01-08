import argparse

import argcomplete

from gendiff.formatters import format_difference
from gendiff.get_diff import get_diff
from gendiff.parser import parse

VERSION = "0.1.0"


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
        :param format: 'stylish', 'plain' или 'json' (по умолчанию 'stylish')
        :type format: str
        :return: Строковый тип данных
        :rtype: str
        """
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    diff = get_diff(file1, file2)
    return format_difference(diff, format)


def parse_command_line():
    """Возвращает аргументы после разбора параметров командной строки"""
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
                        version='%(prog)s {}'.format(VERSION)
                        )
    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
