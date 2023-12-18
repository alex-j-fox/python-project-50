import os

import pytest

from gendiff.gen_diff import generate_diff


def get_fixtures_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


files = [
    'plain1.json',
    'plain2.json',
    'plain1.yml',
    'plain2.yml',
    'nested1.json',
    'nested2.json',
    'nested1.yml',
    'nested2.yml',
    'plain_diff_stylish_format.txt',
    'nested_diff_stylish_format.txt',
    'nested_diff_plain_format.txt'
]

plain1_json, plain2_json, plain1_yml, plain2_yml, \
    nested1_json, nested2_json, nested1_yml, nested2_yml, \
    stylish_plain, stylish_nested, plain_diff = map(get_fixtures_path, files)


@pytest.mark.parametrize('file1, file2, expected_diff, format', [
    (plain1_json, plain2_json, read(stylish_plain), 'stylish'),
    (plain1_yml, plain2_yml, read(stylish_plain), 'stylish'),
    (nested1_yml, nested2_yml, read(stylish_nested), 'stylish'),
    (nested1_yml, nested2_yml, read(stylish_nested), 'stylish'),
    (nested1_yml, nested2_json, read(plain_diff), 'plain'),
])
def test_generate_diff(file1, file2, expected_diff, format):
    diff = generate_diff(file1, file2, format)
    assert diff == expected_diff
