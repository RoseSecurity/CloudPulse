#!/usr/bin/env python3

import praw


# Function to display subreddit posts
def subreddit_posts(reddit_client_id, reddit_client_secret, reddit_username, reddit_password):
    subreddits = ["hacking", "infosec", "redteamsec",
                  "cybersecurity", "netsec", "hackernews", "devops", "terraform", "ansible", "aws",
                  "github", "homelab", "homenetworking",
                  "kubernetes", "networking", "proxmox", "sysadmin", "vscode", "sre", "azure",
                  "docker", "linux", "bash", "ubuntu", "vim", "debian",
                  "freebsd", "fedora", "golang", "kde", "gnome", "opensource"]

    # Instantiate bot
    reddit = praw.Reddit(client_id=reddit_client_id,
                         client_secret=reddit_client_secret,
                         user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,'
                         ' like Gecko) Chrome/107.0.0.0 Safari/537.36',
                         username=reddit_username,
                         password=reddit_password)
    subreddit_list = []
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.hot(limit=10):
            title = submission.title
            text = submission.selftext
            subreddit_list.append({"title": title, "text": text})
        return subreddit_list
