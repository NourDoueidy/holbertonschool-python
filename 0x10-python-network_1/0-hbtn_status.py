#!/usr/bin/python3
"""Fetching http://intranet.hbtn.io/status"""
import urllib.request
with urlib.request.urlopen("http://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
