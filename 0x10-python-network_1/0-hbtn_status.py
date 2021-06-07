#!/usr/bin/python3
"""Fetching a URL"""
import urllib.request
with urlib.request.urlopen("http://intranet.hbtn.io/status") as response:
    html = response.read

