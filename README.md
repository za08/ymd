# YouTube Music Downloader

This Python code allows you to search for music tracks on YouTube and download them in high-quality audio-only format using `yt-dlp` and `youtubesearchpython` libraries. It is intended to be a simple way to automate the downloading of audio tracks based on text input.

## Features
- Searches YouTube for tracks based on names provided in a text file.
- Downloads audio-only files in `.webm` format using `yt-dlp`.
- Automatically sanitizes filenames to ensure valid file paths.
- Logs errors for failed downloads in `error_log.txt`.

## Installation

### Requirements
- Python 3.x
- yt-dlp
- youtubesearchpython
- ffmpeg (required by yt-dlp for processing audio files)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/youtube-audio-downloader.git
   cd youtube-audio-downloader
