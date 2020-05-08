#!/usr/bin/python3
"""aprints the titles of the first 10 hot posts"""
from requests import get


def top_ten(subreddit):
    """10 hot posts listed for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    user_agent = {"User-Agent": "android:com.example.myredditapp:v1.2.3"}
    hot_dict = get(url, headers=user_agent, allow_redirects=False)

    if hot_dict.status_code != 200:
        return 0

    hot_dict = hot_dict.json()
    data = hot_dict.get("data")
    children = data.get("children")
    list_of_post = []
    for i in children:
        post = i.get("data")
        title = post.get("title")
        list_of_post.append(title)
    for i in list_of_post:
        print(i)
