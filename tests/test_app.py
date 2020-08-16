
from app import index


def test_index():
    assert index() == "Hello world !"
    
def test_new_function():
    assert new_function() == 5


