#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.
listing 10 commits (from the most recent to oldest) of the repository 
by the user “rails”
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Python script that takes 2 arguments in order to solve this challenge.
    listing 10 commits (from the most recent to oldest) of the repository 
    by the user “rails””
    """
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    req = requests.get(url)
    request_list = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(request_list[i].get('sha'), request_list[i].
                                  get('commit').get('author').get('name')))
    except:
        pass