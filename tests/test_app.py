
from app import index, new_function


def test_index():
    assert index() == "Hello world !"
    
def test_new_function():
    assert new_function() == 5
    
def test_new_function2():
    assert new_function2() == new_function()


