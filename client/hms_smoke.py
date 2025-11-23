import json
import requests


HOST = "http://localhost:8000"


def get_hms_smokes(offset, limit):
    resp = requests.get(f"{HOST}/hms_smokes", params={"offset": offset, "limit": limit})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))


def get_hms_smoke(year, id):
    resp = requests.get(f"{HOST}/hms_smoke/{id}", params={"year": year, "id": id})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))