#!/usr/bin/python3

import requests

def count_words(subreddit, word_list):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("data", {}).get("children", [])

        if not articles:
            return

        title_list = [article["data"]["title"].lower() for article in articles]
        word_count = {}

        for title in title_list:
            for word in word_list:
                if word.lower() in title.split():
                    word_count[word] = word_count.get(word, 0) + 1

        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print(f"{word.lower()}: {count}")
    else:
        return

    # Recursive call to fetch more articles
    count_words(subreddit, word_list)
