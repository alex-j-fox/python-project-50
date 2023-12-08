from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_json():
    with open(
            './gendiff/tests/fixtures/output.txt'
    ) as output:
        diff = generate_diff(
            './gendiff/tests/fixtures/file1.json',
            './gendiff/tests/fixtures/file2.json'
        )
        assert diff == output.read()


def test_generate_diff_yaml():
    with open(
            './gendiff/tests/fixtures/output.txt'
    ) as output:
        diff = generate_diff(
            './gendiff/tests/fixtures/file1.yml',
            './gendiff/tests/fixtures/file2.yml'
        )
        assert diff == output.read()
