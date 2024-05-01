from pro_filer.actions.main_actions import show_preview # NOQA
import pytest
from typing import Dict, List, Tuple


@pytest.mark.parametrize(
    "context, expected_output",
    [
        (
            {
                "all_files": [
                    "src/__init__.py", "src/app.py", "src/utils/__init__.py"
                    ],
                "all_dirs": ["src", "src/utils"]
            },
            "First 5 files: ['src/__init__.py'" +
            ", 'src/app.py', 'src/utils/__init__.py']\n"
            "First 5 directories: ['src', 'src/utils']\n"
        ),
        (
            {"all_files": [], "all_dirs": []},
            "Found 0 files and 0 directories\n"
        ),
        (
            {"all_files": ["file1.txt"], "all_dirs": []},
            "First 5 files: ['file1.txt']\n"
        ),
        (
            {"all_files": [], "all_dirs": ["dir1", "dir2"]},
            "First 5 directories: ['dir1', 'dir2']\n"
        ),
        (
            {"all_files": [
                "file1.txt", "file2.txt", "file3.txt",
                "file4.txt", "file5.txt", "file6.txt"
                ],
             "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5", "dir6"]},
            "First 5 files: ['file1.txt'" +
            ", 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt']\n"
            "First 5 directories: ['dir1', 'dir2', 'dir3', 'dir4', 'dir5']\n"
        ),
    ]
)
def test_show_preview(
        context: Dict[str, List[str]],
        expected_output: str,
        capsys: Tuple[str, str],
        ) -> None:
    show_preview(context)
    captured = capsys.readouterr()
    assert expected_output.strip() in captured.out.strip()
