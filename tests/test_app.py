
from app import index, new_function


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

resp = requests.post('http://10.1.0.4:4000/test_service_on_db', json=params)
print(resp)
print(resp.json())

