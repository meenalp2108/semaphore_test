
from app import index, new_function, new_function2


def test_index():
    assert index() == "Hello world !"
    
def test_new_function():
    assert new_function() == 5
    
def test_new_function2():
    assert new_function2() == 5


