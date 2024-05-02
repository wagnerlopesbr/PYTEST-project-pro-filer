import pytest


@pytest.fixture(scope="function")
def dir(tmp_path):
    dir = tmp_path / "sub"
    dir.mkdir()
    file = dir / "file.txt"
    file.write_text("GABIGOL VAI CRAVAR HOJE")
    return str(file)
