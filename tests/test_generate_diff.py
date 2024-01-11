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


@pytest.mark.parametrize('file1, file2, expected_diff, format', [
    ('plain1.json', 'plain2.json', 'plain_diff_stylish_format.txt', 'stylish'),
    ('plain1.yml', 'plain2.yml', 'plain_diff_stylish_format.txt', 'stylish'),
    ('nested1.yml', 'nested2.yml', 'nested_diff_stylish_format.txt', 'stylish'),
    ('nested1.yml', 'nested2.yml', 'nested_diff_stylish_format.txt', 'stylish'),
    ('nested1.yml', 'nested2.json', 'nested_diff_plain_format.txt', 'plain'),
    ('nested1.yml', 'nested2.json', 'nested_diff_json_format.txt', 'json'),
])
def test_generate_diff(file1, file2, expected_diff, format):
    file1_data = get_fixtures_path(file1)
    file2_data = get_fixtures_path(file2)
    expected_diff_data = read(get_fixtures_path(expected_diff))

    diff = generate_diff(file1_data, file2_data, format)
    assert diff == expected_diff_data
