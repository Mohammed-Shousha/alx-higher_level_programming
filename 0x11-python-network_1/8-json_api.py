#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    value = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"

    r = requests.post(url, data=value)

    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except:
        print("Not a valid JSON")
