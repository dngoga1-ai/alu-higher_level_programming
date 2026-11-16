#!/usr/bin/python3
"""Displays the GitHub id of a user using Basic Authentication"""
import requests
import sys

if __name__ == "__main__":
    res = requests.get("https://api.github.com/user",
                       auth=(sys.argv[1], sys.argv[2]))
    print(res.json().get("id"))
