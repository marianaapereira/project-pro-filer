from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_no_duplicate_files(tmp_path):
    test_file_1 = tmp_path / "test_file_1.txt"
    test_file_2 = tmp_path / "test_file_2.txt"
    test_file_3 = tmp_path / "test_file_3.txt"

    test_file_1.write_text("Test file 1: Hello world!")
    test_file_2.write_text("Test file 2: Hello!")
    test_file_3.write_text("test file 3: world")

    test_file_1 = str(test_file_1)
    test_file_2 = str(test_file_2)
    test_file_3 = str(test_file_3)

    context = {
        "all_files": [
            test_file_1,
            test_file_2,
            test_file_3,
        ]
    }

    expected_response = []
    output = find_duplicate_files(context)
    assert output == expected_response


def test_duplicate_files(tmp_path):
    test_file_1 = tmp_path / "test_file_1.txt"
    test_file_2 = tmp_path / "test_file_2.txt"
    test_file_3 = tmp_path / "test_file_3.txt"

    test_file_1.write_text("Hello world!")
    test_file_2.write_text("Hello world!")
    test_file_3.write_text("Hello world!")

    test_file_1 = str(test_file_1)
    test_file_2 = str(test_file_2)
    test_file_3 = str(test_file_3)

    context = {
        "all_files": [
            test_file_1,
            test_file_2,
            test_file_3,
        ]
    }

    expected_response = [
        (test_file_1, test_file_2),
        (test_file_1, test_file_3),
        (test_file_2, test_file_3),
    ]
    output = find_duplicate_files(context)
    assert output == expected_response


def test_raise_value_error():
    with pytest.raises(ValueError) as raisedError:

        context = {
            "all_files": [
                '/tmp/non/existent/file1.py',
                '/tmp/non/existent/file2.py',
            ]
        }

        expected_error_message = "All files must exist"

        find_duplicate_files(context)
    assert str(raisedError.value) == expected_error_message
