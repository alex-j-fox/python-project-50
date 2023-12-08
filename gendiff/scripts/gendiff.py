#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import argparse
from typing import List
from .parser import parse


def encode_boolean_and_none_value_in_dict(dictionary: dict) -> None:
    """
        Encodes Boolean and None dictionary values into JSON format.

        :param dictionary:
        :type dictionary: dict
        :return: None
        """
    for key, value in dictionary.items():
        if type(value) is bool or value is None:
            dictionary[key] = json.dumps(value)


def generate_diff_list(file1, file2, keys_list: List[str]) -> List[str]:
    """
    Сравнивает пары "ключ-значение" в двух словарях и возвращает сравнения в
    списке строк в формате
    ['{',
    '  - key1: value1',
    '  + key2: value2',
    '    key3: value3',
    ...,
    '}']
        где
    '-' - ключ отсутствует во втором словаре либо имеет другое значение,
    '+' - ключ отсутствует в первом словаре либо имеет другое значение,
    ' ' - ключ с идентичным значением есть в обоих словарях.

    :param file1: Словарь 1
    :type file1: dict
    :param file2: Словарь 2
    :type file2: dict
    :param keys_list: Список уникальных ключей обоих словарей
    :type keys_list: list[str]
    :return: Список строк
    :rtype: list[str]
    """

    diff_list = ['{']
    for key in keys_list:
        if key not in file2:
            diff_list.append(f'  - {key}: {file1[key]}')
        elif key not in file1:
            diff_list.append(f'  + {key}: {file2[key]}')
        elif file1[key] != file2[key]:
            diff_list.append(f'  - {key}: {file1[key]}')
            diff_list.append(f'  + {key}: {file2[key]}')
        else:
            diff_list.append(f'    {key}: {file1[key]}')
    diff_list.append('}')

    return diff_list


def generate_diff(file_path1, file_path2):
    """
        Генерирует обьемную строку с результатом сравнения двух файлов .json
        или .yaml

        :param file_path1: Путь до файла 1
        :type file_path1: str
        :param file_path2: Путь до файла 2
        :type file_path2: str
        :return:
        :rtype: str
        """
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    encode_boolean_and_none_value_in_dict(file1)
    encode_boolean_and_none_value_in_dict(file2)
    sorted_unique_keys = sorted({*file1.keys(), *file2.keys()})
    diff_list = generate_diff_list(file1, file2, sorted_unique_keys)
    return '\n'.join(diff_list)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file,
                        args.second_file
                        ))


if __name__ == '__main__':
    main()
