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
    'plain_diff.txt',
    'nested_diff.txt'
]

plain1_json, plain2_json, plain1_yml, plain2_yml, \
    nested1_json, nested2_json, nested1_yml, nested2_yml, \
    plain_diff, nested_diff = map(get_fixtures_path, files)


@pytest.mark.parametrize('file1, file2, expected_diff', [
    (plain1_json, plain2_json, read(plain_diff)),
    (plain1_yml, plain2_yml, read(plain_diff)),
    (nested1_yml, nested2_yml, read(nested_diff)),
    (nested1_yml, nested2_yml, read(nested_diff))
])
def test_generate_diff(file1, file2, expected_diff):
    diff = generate_diff(file1, file2)
    assert diff == expected_diff
