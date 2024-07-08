#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    """Python script that fetches https://alx-intranet.hbtn.io/status"""
    fetcher = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(fetcher.text)))
    print("\t- content: {}".format(fetcher.text))