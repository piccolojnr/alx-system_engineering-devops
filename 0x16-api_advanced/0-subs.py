#!/usr/bin/python3
"""_summary_
"""
import requests


def number_of_subscribers(subreddit):
    """_summary_"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    data = response.json()
    subs = data.get("data", {}).get("subscribers", 0)
    return subs
