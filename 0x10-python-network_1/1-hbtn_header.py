#!.usr/bin/python3
"""Sends a request to the URL and displays the value of X_Request-Id"""

import sys
import urllib.request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
