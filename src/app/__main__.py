#!/usr/bin/env python3
import os
import ast
import configparser

from app.app import *
from collector.reddit import *
from collector.rss import *
from app.output import *
from app.streamlit_app import *

# CloudPulse curates compelling news on cloud technologies and cybersecurity.
# By aggregating information from RSS feeds, Reddit, and leveraging AI capabilities,
# it identifies the most noteworthy and impactful updates in the tech industry.


class Color:
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def read_config(filename='config.ini'):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"{Color.RED}{Color.BOLD}Error: Configuration file '{filename}' not found."
                                f" Please create the file with the required settings.")

    config = configparser.ConfigParser(allow_no_value=False)
    config.read(filename)
    return config


# Validate that the tokens, usernames, and keys needed to access the APIs are set
def validate_config(config) -> bool:

    credentials_section = 'Credentials'
    required_keys = ["REDDIT_CLIENT_ID",
                     "REDDIT_CLIENT_SECRET", "REDDIT_USERNAME", "REDDIT_PASSWORD"]

    for key in required_keys:
        if key not in config[credentials_section]:
            print(
                f"{Color.RED}{Color.BOLD}Error{Color.END}: The required configuration key '{key}' is missing.")
            return False
    return True


def cloudpulse():
    # Print CloudPulse banner and read configuration file
    print_banner()
    config = read_config()

    if not validate_config(config):
        print(
            f"{Color.RED}{Color.BOLD}Error{Color.END}: Could not validate configuration file.")

    # Parse the arguments and begin collection
    output_format = app()

    # Run collectors
    reddit_client_id = config.get('Credentials', 'REDDIT_CLIENT_ID')
    reddit_client_secret = config.get('Credentials', 'REDDIT_CLIENT_SECRET')
    reddit_username = config.get('Credentials', 'REDDIT_USERNAME')
    reddit_password = config.get('Credentials', 'REDDIT_PASSWORD')

    # Pass the Reddit and RSS Feeds to the collectors
    subreddits =  ast.literal_eval(config.get('Reddit', 'subreddits'))
    reddit_feeds = subreddit_posts(
        reddit_client_id, reddit_client_secret, reddit_username, reddit_password, subreddits)

    feeds = ast.literal_eval(config.get('RSS', 'feeds'))
    rss_feeds = fetch_rss_data(feeds)

    # Outputs
    if output_format is None:
        print(Color.RED + "\nUse -h for help menu\n" + Color.END)
    elif output_format == "stdout":
        for entry in rss_feeds + reddit_feeds:
            print('-' * 20)
            print(Color.BOLD + f"{entry['title']}\n" + Color.END)
            print(f"{entry['text']}")
    elif output_format == "file":
        output_file(rss_feeds, reddit_feeds)
    elif output_format == "streamlit":
        output_markdown_file = output_file(rss_feeds, reddit_feeds)
        output_streamlit(output_markdown_file)
    else:
        print(Color.RED + "\nInvalid output format. Use -h for help menu\n" + Color.END)
