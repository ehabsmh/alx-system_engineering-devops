#!/usr/bin/python3
"""Query Reddit API for number of subscribers for a given subreddit"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})

    response = requests.get(url, headers=headers, params={"limit": 9}).json()
    posts = response.get('data', {}).get('children')

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get('data', {}).get('title'))
