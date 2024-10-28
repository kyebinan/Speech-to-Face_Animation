#!/home/joyboy/Documents/myenv/bin/python

import sys
import os
import time
from yt_dlp import YoutubeDL

def download_videos(link_list, download_path='.'):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    ydl_opts = {
        'format': 'best',  # Download the best quality
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Specify download path and filename
        'noplaylist': True,  # Do not download playlists
        'retries': 3,  # Retry 3 times if download fails
        'verbose': True,  # Enable verbose logging for error tracking
        'age-limit': 18  # Bypass age-restricted content if necessary
    }

    with YoutubeDL(ydl_opts) as ydl:
        for index, link in enumerate(link_list, start=1):
            try:
                print(f"Downloading {index}/{len(link_list)} from {link}...")
                info_dict = ydl.extract_info(link, download=True)  # Use extract_info for better error handling
                print(f"Downloaded {info_dict.get('title', 'Unknown Title')} successfully!")
            except Exception as e:
                print(f"Failed to download {link}. Skipping... Error: {e}")
                continue  # Skip to the next video and continue the process

            # Pause for 10 seconds between downloads to avoid rate-limiting
            time.sleep(10)

def read_links_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./download_youtube_videos.py <link_file> [<download_folder>]")
        sys.exit(1)

    link_file = sys.argv[1]
    download_folder = sys.argv[2] if len(sys.argv) > 2 else './downloads'

    if not os.path.isfile(link_file):
        print(f"Error: File '{link_file}' not found!")
        sys.exit(1)

    video_links = read_links_from_file(link_file)

    if not video_links:
        print(f"No links found in '{link_file}'")
        sys.exit(1)

    download_videos(video_links, download_folder)
