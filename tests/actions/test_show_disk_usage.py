from pro_filer.actions.main_actions import show_disk_usage  # NOQA


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

    test_file_1 = str(tmp_path / "test_file_1.txt")
    test_file_2 = str(tmp_path / "test_file_2.txt")
    test_file_3 = str(tmp_path / "test_file_3.txt")

    context = {
        "all_files": [
            test_file_1,
            test_file_2,
            test_file_3,
        ]
    }

    output_line_1 = (
        "'/tmp/pytest-of-marianaperei...est_file_list0/test_file_1.txt':"
        "        25 (40%)"
    )
    output_line_2 = (
        "'/tmp/pytest-of-marianaperei...est_file_list0/test_file_2.txt':"
        "        19 (30%)"
    )
    output_line_3 = (
        "'/tmp/pytest-of-marianaperei...est_file_list0/test_file_3.txt':"
        "        18 (29%)"
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
    assert expected_response == captured.out
