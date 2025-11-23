import json
import requests


HOST = "http://localhost:8000"


def get_lakes_polys(offset, limit):
    resp = requests.get(f"{HOST}/lakes_polys", params={"offset": offset, "limit": limit})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))


def get_lakes_poly(hylak_id):
    resp = requests.get(f"{HOST}/lakes_polys/{hylak_id}", params={"hylak_id": hylak_id})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))