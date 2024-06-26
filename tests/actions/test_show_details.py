from pro_filer.actions.main_actions import show_details  # NOQA
from unittest.mock import patch
from datetime import date


def test_invalid_file(capsys):
    context = {
        "base_path": "/home/trybe/????"
    }

    expected_response = "File '????' does not exist\n"

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == expected_response


def test_no_extension_file(capsys):
    fixed_timestamp = 1609459200

    with patch('os.path.getmtime', return_value=fixed_timestamp):
        context = {
            "base_path": "tests/actions/test_show_details_mock"
        }

        output_line_1 = "File name: test_show_details_mock"
        output_line_2 = "File size in bytes: 681"
        output_line_3 = "File type: file"
        output_line_4 = "File extension: [no extension]"
        output_line_5 = (
            f"Last modified date: {date.fromtimestamp(fixed_timestamp)}"
        )

        expected_response = (
            f"{output_line_1}\n"
            f"{output_line_2}\n"
            f"{output_line_3}\n"
            f"{output_line_4}\n"
            f"{output_line_5}\n"
        )

        show_details(context)
        captured = capsys.readouterr()
        assert captured.out == expected_response


def test_valid_file(capsys):
    fixed_timestamp = 1609459200

    with patch('os.path.getmtime', return_value=fixed_timestamp):
        context = {
            "base_path": "images/pro-filer-preview.gif"
        }

        output_line_1 = "File name: pro-filer-preview.gif"
        output_line_2 = "File size in bytes: 270824"
        output_line_3 = "File type: file"
        output_line_4 = "File extension: .gif"
        output_line_5 = (
            f"Last modified date: {date.fromtimestamp(fixed_timestamp)}"
        )

        expected_response = (
            f"{output_line_1}\n"
            f"{output_line_2}\n"
            f"{output_line_3}\n"
            f"{output_line_4}\n"
            f"{output_line_5}\n"
        )

        show_details(context)
        captured = capsys.readouterr()
        assert captured.out == expected_response
