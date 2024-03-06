#!/usr/bin/python3
"""_summary_
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """_summary_"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(
        url,
        headers=headers,
        params={"limit": 100, "after": after},
        allow_redirects=False,
    )
    if response.status_code == 200:

        data = response.json()
        results = data.get("data")
        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after=results.get("after"))
        return hot_list
    else:
        return None
