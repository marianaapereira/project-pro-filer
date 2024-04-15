from pro_filer.actions.main_actions import show_preview  # NOQA


def test_empty_context_keys(capsys):
    context = {
        "all_files": [],
        "all_dirs": []
    }

    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == "Found 0 files and 0 directories\n"


def test_correct_context_keys(capsys):
    context = {
        "all_files": [
            "src/__init__.py", "src/app.py", "src/utils/__init__.py"
        ],
        "all_dirs": ["src", "src/utils"]
    }

    output_line_1 = "Found 3 files and 2 directories"
    output_line_2 = f"First 5 files: {context['all_files']}"
    output_line_3 = f"First 5 directories: {context['all_dirs']}"

    expected_response = f"{output_line_1}\n{output_line_2}\n{output_line_3}\n"

    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_response


def test_correct_output_length(capsys):
    context = {
        "all_files": [
            "src/file1.py", "src/file2.py", "src/file3.py",
            "src/file4.py", "src/file5.py", "src/file6.py"
        ],
        "all_dirs": [
            "src", "src/utils", "src/tests",
            "src/actions", "src/trybe", "src/git"
        ]
    }

    response_context = {
        "all_files": [
            "src/file1.py", "src/file2.py", "src/file3.py",
            "src/file4.py", "src/file5.py"
        ],
        "all_dirs": [
            "src", "src/utils", "src/tests",
            "src/actions", "src/trybe"
        ]
    }

    output_line_1 = "Found 6 files and 6 directories"
    output_line_2 = f"First 5 files: {response_context['all_files']}"
    output_line_3 = f"First 5 directories: {response_context['all_dirs']}"

    expected_response = f"{output_line_1}\n{output_line_2}\n{output_line_3}\n"

    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_response
