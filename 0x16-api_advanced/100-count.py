#!/usr/bin/python3
"""_summary_
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """_summary_"""
    if not word_count:
        word_count = {w.lower(): 0 for w in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}
    response = requests.get(
        url,
        headers=headers,
        params={"limit": 100, "after": after},
        allow_redirects=False,
    )
    try:
        if response.status_code == 200:
            data = response.json()
            for child in data.get("data").get("children"):
                titles = child.get("data").get("title").split(" ")
                for k in word_count.keys():
                    word_count[k] += titles.count(k)

            after = data.get("data").get("after")

            if after is None:
                wc = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for w in wc:
                    if w[1]:
                        print("{}: {}".format(w[0], w[1]))
                return None
            else:
                print(after)
                count_words(subreddit, word_list, after, word_count)

        else:
            return None
    except Exception:
        return None
