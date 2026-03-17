#!/usr/bin/python3
"""Module to recursively query the Reddit API and return a list
of titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively query the Reddit API and return a list of titles
    of all hot articles for a given subreddit.
    Returns None if invalid subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): Accumulated list of hot article titles.
        after (str): Pagination token for next page.

    Returns:
        list: List of hot article titles, or None if invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:api_advanced:v1.0 (by /u/api_advanced_user)"
    }
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    after = data.get("data", {}).get("after")

    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
