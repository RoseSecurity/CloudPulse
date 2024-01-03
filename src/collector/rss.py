#!/usr/bin/env python3

import feedparser


def fetch_rss_data():
    # Feeds to monitor
    aws_feeds = ["https://aws.amazon.com/blogs/architecture/feed/",
                 "https://aws.amazon.com/blogs/aws/feed/",
                 "https://aws.amazon.com/blogs/compute/feed/",
                 "https://aws.amazon.com/blogs/containers/feed/", "https://aws.amazon.com/blogs/devops/feed/",
                 "https://aws.amazon.com/blogs/database/feed/",
                 "https://aws.amazon.com/blogs/infrastructure-and-automation/feed/",
                 "https://aws.amazon.com/blogs/opensource/feed/",
                 "https://aws.amazon.com/blogs/opensource/feed/",
                 ]

    breach_feeds = [
        "https://feeds.feedburner.com/HaveIBeenPwnedLatestBreaches"]

    devops_feeds = ["https://github.com/opentofu/opentofu/releases.atom",
                    "https://github.com/hashicorp/terraform/releases.atom",
                    "https://github.com/kubernetes/kubernetes/releases.atom"
                    ]

    # Fetch data from RSS feeds
    final_feed = aws_feeds + breach_feeds + devops_feeds
    rss_feed_list = []
    for url in final_feed:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            rss_title = entry.title
            rss_summary = entry.summary
            rss_feed_list.append({"title": rss_title, "text": rss_summary})
    return rss_feed_list
