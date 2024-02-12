#!/usr/bin/python3
"""
Module contains a script tat fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        data = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(data)))
        print("\t - content: {}".format(data))
        print("\t - utf8 content: {}".format(data.decode('utf-8')))
