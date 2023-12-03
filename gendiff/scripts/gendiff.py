#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json
import argparse


def encode_boolean_value_in_dict(dictionary: dict) -> None:
    for key, value in dictionary.items():
        if type(value) is bool:
            dictionary[key] = json.dumps(value)


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    encode_boolean_value_in_dict(file1)
    encode_boolean_value_in_dict(file2)
    sorted_unique_keys = sorted({*file1.keys(), *file2.keys()})
    diff_list = ['{']
    for key in sorted_unique_keys:
        if key in file1 and key not in file2:
            diff_list.append(f'  - {key}: {file1[key]}')
        elif key in file2 and key not in file1:
            diff_list.append(f'  + {key}: {file2[key]}')
        else:
            if file1[key] != file2[key]:
                diff_list.append(f'  - {key}: {file1[key]}')
                diff_list.append(f'  + {key}: {file2[key]}')
            else:
                diff_list.append(f'    {key}: {file1[key]}')
    diff_list.append('}')
    diff = '\n'.join(diff_list)
    return diff


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
