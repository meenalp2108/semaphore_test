
from src.app import index, new_function


def test_index():
    assert index() == "Hello world !"
    
def test_new_function():
    assert new_function() == 5

import requests

params = {
        "a" : 5,
        "b" : 7,
        "n" : 120
    }

resp = requests.post('http://172.16.55.142:4000/get_data_test_val', json=params)
print(resp)

