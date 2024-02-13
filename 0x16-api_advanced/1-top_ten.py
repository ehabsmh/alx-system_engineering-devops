#!/usr/bin/python3
"""Queries the Reddit API and prints the titles"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    response = requests.get(url, headers=headers, params={"limit": 10}).json()
    top_ten_posts = response.get('data', {}).get('children', [])

    if not top_ten_posts:
        print(None)
        return

    for post in top_ten_posts:
        print(post.get('data', {}).get('title'))
