from shapely.geometry import shape


import json
import requests


HOST = "http://localhost:8000"


def intersects(
        path_a: str,
        col_a: str,
        id_a: int,
        path_b: str,
        col_b: str,
        id_b: int
):
    resp_a = requests.get(f"{HOST}/{path_a}/{id_a}", params={"id": id_a})
    if resp_a.status_code != 200:
        print("Error:", resp_a.status_code)
        return
    
    resp_b = requests.get(f"{HOST}/{path_b}/{id_b}", params={"id": id_b})
    if resp_b.status_code != 200:
        print("Error:", resp_b.status_code)
        return

    print(shape(json.loads(resp_a.json().get(f"{col_a}"))).intersects(shape(json.loads(resp_b.json().get(f"{col_b}")))))