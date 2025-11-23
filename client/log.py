import json
import requests


HOST = "http://localhost:8000"


def get_logs(offset, limit):
    resp = requests.get(f"{HOST}/logs", params={"offset": offset, "limit": limit})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))


def get_log(id):
    resp = requests.get(f"{HOST}/logs/{id}", params={"id": id})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return

    print(json.dumps(resp.json(), indent=4))