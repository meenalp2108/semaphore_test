
from app import index, new_function


def test_index():
    assert index() == "Hello world !"
    
def test_new_function():
    assert new_function() == 5


