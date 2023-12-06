from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    with open(
            './gendiff/tests/fixtures/output.txt'
    ) as output:
        diff = generate_diff(
            './gendiff/tests/fixtures/file1.json',
            './gendiff/tests/fixtures/file2.json'
        )
        assert diff == output.read()
