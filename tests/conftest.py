import pytest


@pytest.fixture
def tmpdir(tmpdir):
    return str(tmpdir)
