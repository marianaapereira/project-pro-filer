from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path


def test_no_files(capsys):
    context = {
        "all_files": []
    }

    expected_response = "Total size: 0\n"

    show_disk_usage(context)
    captured = capsys.readouterr()
    assert captured.out == expected_response


def test_file_list(capsys, tmp_path):
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

    formatted_file_path_1 = f"'{_get_printable_file_path(test_file_1)}':"
    formatted_file_path_2 = f"'{_get_printable_file_path(test_file_2)}':"
    formatted_file_path_3 = f"'{_get_printable_file_path(test_file_3)}':"

    output_line_1 = (
        f"{formatted_file_path_1}"
        "25 (40%)"
    )
    output_line_2 = (
        f"{formatted_file_path_2}"
        "19 (30%)"
    )
    output_line_3 = (
        f"{formatted_file_path_3}"
        "18 (29%)"
    )
    output_line_4 = "Total size: 62"

    expected_response = (
        f"{output_line_1}\n"
        f"{output_line_2}\n"
        f"{output_line_3}\n"
        f"{output_line_4}\n"
    )

    show_disk_usage(context)
    captured = capsys.readouterr()
    assert expected_response.replace(' ', '') == captured.out.replace(' ', '')
