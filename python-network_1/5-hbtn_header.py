#!/usr/bin/python3
"""Displays the X-Request-Id header of a URL response using requests"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
