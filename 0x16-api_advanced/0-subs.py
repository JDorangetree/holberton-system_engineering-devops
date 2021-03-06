#!/usr/bin/python3
"""and returns the number of subscribers of a subreddit"""
from requests import get


def number_of_subscribers(subreddit):
    """ Returns subscriber count of subreddit"""

    url = 'https://www.reddit.com//r/{}/about.json'.format(subreddit)
    user_agent = {"User-Agent": "myredditapp:v1.2.3"}
    subreddit_dict = get(url, headers=user_agent, allow_redirects=False)

    if subreddit_dict.status_code != 200:
        return 0

    subreddit_dict = subreddit_dict.json()

    data = subreddit_dict.get("data")
    subscribers = data["subscribers"]
    return subscribers
