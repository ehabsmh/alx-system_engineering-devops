#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list"""
import requests


def recurse(subreddit, hot_list=[], after="", counter=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "My User Agent 1.0"
    }
    params = {
        "after": after,
        "counter": counter,
    }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 404:
        return None

    results = res.json().get("data")
    after = results.get("after")
    counter += results.get("dist")

    for child in results.get("children"):
        resulted_child = child.get("data").get("title")
        hot_list.append(resulted_child)

    if after is not None:
        return recurse(subreddit, hot_list, after, counter)
    return hot_list
