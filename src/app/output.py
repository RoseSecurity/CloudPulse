#!/usr/bin/env python3
import subprocess
import os

from datetime import datetime
import sys
from pathlib import Path
from app.streamlit_app import *


class Color:
    BLUE = '\033[34m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\x1b[0m'


today = str(datetime.now().date())


# Create a markdown file of the curated Reddit and RSS feeds and return the file name
def output_file(rss_feeds, reddit_feeds):
    with open("cloudpulse_" + today + ".md", "a") as output_markdown_file:
        output_markdown_file.write("# CloudPulse News" + "\n")
        for entry in rss_feeds + reddit_feeds:
            output_markdown_file.write(f"<details open>\n<summary>" +
                                       f"{entry['title']}" + "</summary>\n" + f"{entry['text']}\n" + "</details>")
            output_markdown_file.write("\n\n---\n\n")
    print(Color.BOLD + Color.BLUE + "CloudPulse file created!" + Color.END)
    return output_markdown_file.name


# Start the Streamlit application
def output_streamlit(output_markdown_file):
    process = subprocess.Popen(
        ["streamlit", "run", "app/streamlit_app.py", "--", "--file", output_markdown_file])
