import yt_dlp
from youtubesearchpython import VideosSearch
import os
import re

# Path to save the downloaded music
DOWNLOAD_DIR = 'music_downloads'

# Create a directory to store downloads if it doesn't exist
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# Function to sanitize track names for file saving
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)  # Remove special characters

# Function to search for a YouTube video based on the track name
def search_youtube(track):
    try:
        search = VideosSearch(track, limit=1)
        results = search.result()
        if 'result' in results and results['result']:
            return results['result'][0]['link']  # Return the first video URL
        else:
            return None
    except Exception as e:
        print(f"Error searching for {track}: {e}")
        return None

# Function to download a YouTube video using yt-dlp with 'audio-only' format 251 (usually .webm)
def download_video(video_url, track_name):
    try:
        ydl_opts = {
            'format': '251',  # Format 251 is usually the highest-quality audio-only (webm)
            'outtmpl': f'{DOWNLOAD_DIR}/{sanitize_filename(track_name)}.%(ext)s',  # Save as track_name in DOWNLOAD_DIR
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Downloaded: {track_name}")
    except Exception as e:
        print(f"Error downloading {track_name}: {e}")
        log_error(track_name)

# Function to log tracks that encountered an error
def log_error(track_name):
    with open('error_log.txt', 'a') as error_file:
        error_file.write(f"{track_name}\n")

# Read the tracks from 0.txt
with open('0.txt', 'r') as f:
    tracks = f.readlines()

# Iterate through the track names, search YouTube, and download
for track in tracks:
    track = track.strip()
    if not track:
        continue
    video_url = search_youtube(track)
    if video_url:
        download_video(video_url, track)
    else:
        print(f"No results for: {track}")
        log_error(track)
