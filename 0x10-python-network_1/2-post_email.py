#!/usr/bin/python3
"""sends post request to URL with email and displays the body of the response"""

import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    values = {"email" : sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode("utf-8")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
