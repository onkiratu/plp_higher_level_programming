#!/usr/bin/python3

"""
Module contains a script tat fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen

url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as response:
    data = response.read()

print(f"- type: {type(data)}")
print(f"- content: {data}")
print(f"- utf8 content: {data.decode('utf-8')}")
