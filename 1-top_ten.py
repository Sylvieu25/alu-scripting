#!/usr/bin/python3
"""Module to query the Reddit API and print the top 10 hot posts
for a given subreddit."""
import requests


def top_ten(subreddit):
    """Query the Reddit API and print the top 10 hot posts
    for a given subreddit. Prints None if invalid subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/api_advanced)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    for post in posts:
        print(post.get("data", {}).get("title"))
