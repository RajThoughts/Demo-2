
import pytest
@pytest.fixture()
def danger():
    print("1st step will be printed")
    yield
    print("last step")