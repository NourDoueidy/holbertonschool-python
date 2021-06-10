#!/usr/bin/python3
"""Display the value of the variable X-Request-Id"""

import requests
import sys.argv


if __name__ == "__main__":
    resp = requests.get(argv[1])
    print(resp.headers.get("X-Request-Id"))
