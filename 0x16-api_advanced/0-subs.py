#!/usr/bin/python3
from requests import get
from sys import argv
"""and returns the number of subscribers of a subreddit"""


def number_of_subscribers(subreddit):
    """ Returns subscriber count of subreddit"""

    url = 'https://www.reddit.com//r/{}/about.json'.format(argv[1])
    user_agent = {"User-Agent": "android:com.example.myredditapp:v1.2.3"}
    user_dict = get(url, headers=user_agent, allow_redirects=False)

    if user_dict.status_code != 200:
        return 0

    user_dict = user_dict.json()
    data = user_dict.get("data")
    number_of_subscribers = data["subscribers"]
    return number_of_subscribers
