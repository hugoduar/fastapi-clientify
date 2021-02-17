
from fastapi_clientify import *

def test_hash_object():
    h = Hash('request')
    assert h.hash_object() == hash('request')
