#!/usr/bin/python3
from requests import get
"""and returns the number of subscribers of a subreddit"""


def number_of_subscribers(subreddit):
    """ Returns subscriber count of subreddit"""

    url = 'https://www.reddit.com//r/{}/about.json'.format(subreddit)
    user_agent = {"User-Agent": "android:com.example.myredditapp:v1.2.3"}
    subreddit_dict = get(url, headers=user_agent, allow_redirects=False)

    if subreddit_dict.status_code != 200:
        return 0

    try:
        subreddit_dict = subreddit_dict.json()
    except:
        return 0
    data = subreddit_dict.get("data")
    number_of_subscribers = data["subscribers"]
    return number_of_subscribers
