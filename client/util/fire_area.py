import json
import requests


HOST = "http://localhost:8000"


def get_fire_areas(offset, limit):
    resp = requests.get(f"{HOST}/fire_areas", params={"offset": offset, "limit": limit})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))


def get_fire_area(year, id):
    resp = requests.get(f"{HOST}/fire_areas/{id}", params={"year": year, "id": id})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))