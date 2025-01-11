import pytest
import src.main.main


def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    # Check if the test script runs without any errors
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()

@pytest.fixture
def myname():
    return "John"
def test_print_hi(myname):
    # Check if the main script runs without any errors
    sentance = src.main.main.print_hi(myname)
    assert "Hi, John, it is currently" in sentance