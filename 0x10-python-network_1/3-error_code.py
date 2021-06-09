#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as ex:
        print("Error code: {}".format(ex.code))
