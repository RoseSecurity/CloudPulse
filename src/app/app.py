#!/usr/bin/env python3
import argparse
import time


# Variables
class Color:
    BLUE = '\033[34m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    GREEN = '\033[92m'
    END = '\x1b[0m'
    TAG = "@RoseSecurity"


# Banner
def print_banner():
    banner_cloud = """
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ░░░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓██  ░░░░░░░░░░░░░░░░░░██▓▓▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      ░░░░░░░░░░░░░░░░░░░░██▓▓▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ░░░░░░░░░░░░░░░░░░░░░░░░████████▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒████████  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒
        ▒▒▒▒██          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒
        ▒▒██  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒
        ▒▒██  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒
        ▒▒▓▓  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒
        ▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒
        ▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒██████████████████████████████████████████▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒CloudPulse▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

    """
    print(Color.WHITE + banner_cloud + Color.BLUE +
          "When it comes to the latest tech news, keep your head in the clouds\n" + Color.END)
    time.sleep(1)


# CLI Parser
def parse_arguments():
    parser = argparse.ArgumentParser(
        description='\nCloudPulse curates compelling news on cloud technologies and cybersecurity. '
                    'By aggregating information from RSS feeds, Reddit,'
                    'it identifies the most noteworthy and impactful updates in the tech industry.\t' + Color.GREEN + Color.TAG + Color.END)

    parser.add_argument('-o', '--output', choices=['stdout', 'file', 'streamlit'],
                        help='Modes of output: stdout - Output to terminal, file - Output to Markdown file, streamlit '
                             '- Output to Streamlit self-hosted application'
                        )
    return parser.parse_args()


# Main application function to gather arguments and begin collection
def app():
    args = parse_arguments()
    return args.output
