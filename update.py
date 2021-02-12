import uuid
import requests


host = "localhost"
port = "6800"
token = "123456"  # 没有token就注释掉这行
tracker_url = "https://cdn.jsdelivr.net/gh/XIU2/TrackersListCollection@master/all_aria2.txt"


def aria2_update_tracker():
    rpc_json = {
        "jsonrpc": "2.0",
        "method": "aria2.changeGlobalOption",
        "id": str(uuid.uuid4()),
        "params": [f"token:{token}", {"bt-tracker": requests.get(tracker_url).text}]
    }
    if not token:
        rpc_json["params"].pop(0)
    res = requests.post(
        "http://{}:{}/jsonrpc".format(host, port), json=rpc_json)
    print(res.json())


if __name__ == "__main__":
    aria2_update_tracker()
