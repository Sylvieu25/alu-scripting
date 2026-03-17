#!/usr/bin/python3
"""Module to recursively query the Reddit API and count keyword
occurrences in hot article titles for a given subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Recursively query the Reddit API and count occurrences of
    keywords in hot article titles. Prints results sorted by count
    descending, then alphabetically. Prints nothing if invalid.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count.
        after (str): Pagination token for next page.
        counts (dict): Accumulated keyword counts.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0 (by /u/api_advanced)"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    after = data.get("data", {}).get("after")

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            w = word.lower()
            for t in title:
                if t == w:
                    counts[w] = counts.get(w, 0) + 1

    if after is None:
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
        return

    return count_words(subreddit, word_list, after, counts)
