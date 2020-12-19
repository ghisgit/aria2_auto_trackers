import uuid
import json
import re
import urllib.request

from conf import host, port, token, bt_url

aria2_url = f"http://{host}:{port}/jsonrpc"

def get_url_proxy(url, proxy: dict, **kwargs):
    handler = urllib.request.ProxyHandler(proxy)
    openr = urllib.request.build_opener(handler)
    req = urllib.request.Request(url, **kwargs)
    res = openr.open(req)
    if res.status in [200, 201]:
        return res.read().decode("UTF-8")


def get_url(url, **kwargs):
    req = urllib.request.Request(url, **kwargs)
    res = urllib.request.urlopen(req)
    if res.status in [200, 201]:
        return res.read().decode("UTF-8")


def parse(s: str):
    code_bt = re.findall(r"\w+.*", s)
    return ",".join(code_bt)


def update_aria2_bt():
    rpc_json = {
        "jsonrpc": "2.0",
        "method": "aria2.changeGlobalOption",
        "id": str(uuid.uuid4()),
        "params": [f"token:{token}", {"bt-tracker": "parse(get_url(bt_url))"}]
    }
    if token:
        rpc_json["params"].pop(0)
    jsonreq = json.dumps(rpc_json).encode("UTF-8")
    res = get_url(aria2_url, data=jsonreq)
    print(res)


if __name__ == "__main__":
    update_aria2_bt()
