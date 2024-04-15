import pytest
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
      "all_files": ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
      "all_dirs": ["src", "src/utils"]
  }

  response_line_1 = "Found 3 files and 2 directories"
  response_line_2 = "First 5 files: ['src/__init__.py', 'src/app.py', 'src/utils/__init__.py']"
  response_line_3 = "First 5 directories: ['src', 'src/utils']"

  show_preview(context)
  captured = capsys.readouterr()
  assert captured.out == f"{response_line_1}\n{response_line_2}\n{response_line_3}\n"

def test_correct_output_length(capsys):
  context = {
      "all_files": ["src/file1.py", "src/file2.py", "src/file3.py", "src/file4.py", "src/file5.py", "src/file6.py",],
      "all_dirs": ["src", "src/utils", "src/tests", "src/actions", "src/trybe", "src/git"]
  }

  response_line_1 = "Found 6 files and 6 directories"
  response_line_2 = "First 5 files: ['src/file1.py', 'src/file2.py', 'src/file3.py', 'src/file4.py', 'src/file5.py']"
  response_line_3 = "First 5 directories: ['src', 'src/utils', 'src/tests', 'src/actions', 'src/trybe']"

  show_preview(context)
  captured = capsys.readouterr()
  assert captured.out == f"{response_line_1}\n{response_line_2}\n{response_line_3}\n"