import pytest


@pytest.mark.xfail
def test_morning():
    print("Hello Raj")


@pytest.mark.smoke
def test_evening():
    q = 5
    z = 8
    print(q+z)
