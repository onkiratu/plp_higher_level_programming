#!/usr/bin/python3
"Module contains a script tat fetches https://alx-intranet.hbtn.io/status"
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print(f"- type: {type(data)}")
        print(f"- content: {data}")
        print(f"- utf8 content: {data.decode('utf-8')}")