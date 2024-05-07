# -*- coding: utf-8 -*-
# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import pickle  # Import the pickle module to serialize credentials

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from pprint import pprint
from datetime import datetime
import locale

import re
md_yt_link_pattern = re.compile(r"(?=\[(!\[.+?\]\(.+?\)|.+?)]\((https:\/\/[^\)]+)\))")
yt_tooltip_pattern = re.compile(r"^(https?://[^\s\"]+)(?:\s+\"(.+)\")?$")
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def process_md_file(file_path):
    # Read the contents of the Markdown file
    with open(file_path, 'r') as file:
        markdown_content = file.read()

    # Define a regular expression pattern to match YouTube links
    youtube_pattern = r'\[(.*?)\]\((https?://)?(www\.)?youtu(\.be/|be\.com/watch\?v=)([\w-]+)\)'
    md_yt_link_pattern = re.compile(r"(?=\[(!\[.+?\]\(.+?\)|.+?)]\((https:\/\/[^\)]+)\))")
    yt_tooltip_pattern = re.compile(r"^(https?://[^\s\"]+)(?:\s+\"(.+)\")?$")

    # Find all YouTube links in the Markdown content
    youtube_links = re.findall(md_yt_link_pattern, markdown_content)

    for link_tuple in youtube_links:
        original_link = yt_tooltip_pattern.findall(link_tuple[1])[0]
        print(original_link)
        print(f'link is {original_link[0]} tooltip is {original_link[1]}')


def get_credentials():
    # Check if credentials file exists
    if os.path.exists("youtube_credentials.pickle"):
        # Load credentials from file
        with open("youtube_credentials.pickle", "rb") as token:
            credentials = pickle.load(token)
    else:
        # If credentials file does not exist, run the authentication flow
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            "YOUR_CLIENT_SECRET_FILE.json", scopes)
        credentials = flow.run_local_server(port=0)
        # Save credentials to file
        with open("youtube_credentials.pickle", "wb") as token:
            pickle.dump(credentials, token)
    return credentials

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials
    credentials = get_credentials()

    # Create an API client using the stored credentials
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.videos().list(
        part="snippet",
        id="dQw4w9WgXcQ"
    )
    response = request.execute()
    pprint(response['items'][0])
    yt_pub_at = response['items'][0]['snippet']['publishedAt']

    request = youtube.videos().list(
        part="statistics",
        id="dQw4w9WgXcQ"
    )
    response = request.execute()
    pprint(response['items'][0])
    yt_view_count = response['items'][0]['statistics']['viewCount']


    # Set the locale to the user's default (e.g., en_US)
    locale.setlocale(locale.LC_ALL, '')
    yt_pub_at = datetime.strptime(yt_pub_at, '%Y-%m-%dT%H:%M:%SZ').strftime('%B %d, %Y')
    yt_view_count = locale.format_string('%d', int(yt_view_count), grouping=True)
    print(f'Video published {yt_pub_at} and has {yt_view_count} views')

if __name__ == "__main__":
    main()
