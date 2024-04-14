import pytest


@pytest.fixture()
def setup():
    print("I M FIRST")
    yield
    print("I m last")