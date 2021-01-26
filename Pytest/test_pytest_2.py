import pytest


def test_morning():
    print("Hello Raj")


@pytest.mark.smoke
def test_evening():
    print("Hello Gadha")