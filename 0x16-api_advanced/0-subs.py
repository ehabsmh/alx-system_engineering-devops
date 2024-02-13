#!/usr/bin/python3
"""0. How many subs?"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.
    returns 0 if the subreddit is invalid.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'My User Agent 1.0'})
    response = requests.get(url, headers=headers).json()
    subscribers = response.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
