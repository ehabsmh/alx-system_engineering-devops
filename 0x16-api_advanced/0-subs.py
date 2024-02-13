#!/usr/bin/python3
"""0. How many subs?"""
from requests import get


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'script by Ehab Hussein'}
    response = get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    return 0
