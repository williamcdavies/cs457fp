import json
import requests


HOST = "http://localhost:8000"


def get_populated_places(offset, limit):
    resp = requests.get(f"{HOST}/populated_places", params={"offset": offset, "limit": limit})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))


def get_populated_place(id):
    resp = requests.get(f"{HOST}/populated_places/{id}", params={"id": id})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))