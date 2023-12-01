#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests

if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"

    r = requests.get(url)
    commits = r.json()

    for commit in commits[:10]:
        print(
            f"{commit.get('sha')}:\
 {commit.get('commit').get('author').get('name')}")
