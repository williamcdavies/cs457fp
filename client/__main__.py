import requests

API_URL = "http://localhost:8000"

def list_lakes(offset=0, limit=10):
    resp = requests.get(f"{API_URL}/lakes", params={"offset": offset, "limit": limit})
    if resp.status_code != 200:
        print("Error:", resp.status_code)
        return
    lakes = resp.json()
    for lake in lakes:
        print(f"Hylak ID: {lake['hylak_id']}, Name: {lake.get('lake_name')}, Country: {lake.get('country')}")

def main():
    while True:
        print("\nCommands: list [offset] [limit], quit")
        cmd = input("> ").strip().split()
        if not cmd:
            continue
        if cmd[0] == "quit":
            break
        elif cmd[0] == "list":
            offset = int(cmd[1]) if len(cmd) > 1 else 0
            limit = int(cmd[2]) if len(cmd) > 2 else 10
            list_lakes(offset, limit)
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
