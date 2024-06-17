#!/usr/bin/env python3

import feedparser

def fetch_rss_data(feeds):
    # Fetch data from RSS feeds
    rss_feed_list = []
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            rss_title = entry.title
            rss_summary = entry.summary
            rss_feed_list.append({"title": rss_title, "text": rss_summary})
    return rss_feed_list
