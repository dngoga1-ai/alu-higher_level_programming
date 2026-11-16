#!/usr/bin/python3
"""Sends a POST request to search_user with a letter as q"""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    res = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        data = res.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
