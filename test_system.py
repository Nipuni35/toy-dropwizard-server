import json
import requests

def test_code():
    r = requests.get("http://localhost:8085/")
    json_response = r.json
    assert(json_response["code"] == "404")