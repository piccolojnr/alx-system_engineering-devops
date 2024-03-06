#!/usr/bin/python3
"""_summary_
"""
import requests


def top_ten(subreddit):
    """_summary_"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(
        url, headers=headers, params={"limit": 10}, allow_redirects=False
    )
    if response.status_code == 404:
        print("None")

    data = response.json()
    res = data.get("data")
    for c in res.get("children"):
        print(c.get("data").get("title"))
