#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# PYTHON_ARGCOMPLETE_OK

from gendiff import generate_diff, parse_command_line


def main():
    file1, file2, format = parse_command_line()
    print(generate_diff(file1, file2, format))


if __name__ == '__main__':
    main()
