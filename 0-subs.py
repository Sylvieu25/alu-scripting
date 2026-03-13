#!/usr/bin/python3
"""Module to query the Reddit API and return the number of subscribers
for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Query the Reddit API and return the total number of subscribers
    for a given subreddit. Returns 0 if the subreddit is invalid.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Total number of subscribers, or 0 if invalid subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "python:api_advanced:v1.0 (by /u/api_advanced_user)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data.get("data", {}).get("subscribers", 0)
