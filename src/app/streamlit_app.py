#!/usr/bin/env python3
import subprocess
import os
import argparse

import streamlit as st
from PIL import Image
from pathlib import Path


def streamlit_app(output_markdown_file):
    st.set_page_config(
        page_title="CloudPulse News",
        page_icon="🌩️",
    )
    image = Image.open('../docs/img/CloudPulse_Logo.png')
    st.image(image, width=500)

    feeds_markdown = Path(output_markdown_file).read_text()
    st.markdown(feeds_markdown, unsafe_allow_html=True)


if __name__ == '__main__':
    # Argument Parser
    parser = argparse.ArgumentParser(description='Command line options')
    parser.add_argument('--file', action='append', default=[],
                        help="Markdown file for creating visualized dashboard")
    try:
        args = parser.parse_args()
    except SystemExit as e:
        # This exception will be raised if invalid command line arguments
        # are used. Currently streamlit prevents the program from exiting normally
        # so we have to do a hard exit.
        os._exit(e.code)

    output_markdown_file = args.file[0]
    streamlit_app(output_markdown_file)
