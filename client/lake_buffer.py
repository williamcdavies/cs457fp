import json
import requests


HOST = "http://localhost:8000"


def get_lakes_buffers(offset, limit):
    resp = requests.get(f"{HOST}/lakes_buffers", params={"offset": offset, "limit": limit})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))


def get_lakes_buffer(hylak_id):
    resp = requests.get(f"{HOST}/lakes_buffer/{hylak_id}", params={"hylak_id": hylak_id})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))