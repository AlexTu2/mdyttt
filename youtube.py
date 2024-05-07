# -*- coding: utf-8 -*-
# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import pickle  # Import the pickle module to serialize credentials

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

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

    print(response['items'][0]['snippet']['publishedAt'])

if __name__ == "__main__":
    main()
