#!/usr/bin/python3
"""Recursive function that queries the Reddit API and returns a list"""
import requests
import sys


def append_title(hot_list, hot_posts):
    """ Adds item into a list """
    if not len(hot_posts):
        return

    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    append_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """ Queries to Reddit API """
    headers = {'User-Agent': 'My User Agent 1.0'}

    params = {'after': after}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if not res:
        return None

    post = res.json()
    hot_posts = post['data']['children']
    append_title(hot_list, hot_posts)
    after = post['data']['after']

    if not after:
        return hot_list

    return recurse(subreddit, hot_list=hot_list, after=after)
