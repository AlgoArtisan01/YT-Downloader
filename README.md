# YouTube Downloader

A simple Python script that uses the `pytube` library to download YouTube videos. This script allows you to download videos in the highest available resolution and handles errors gracefully by attempting to download in lower resolutions if necessary.

## Features

- **Download Videos**: Download YouTube videos in the highest available resolution.
- **Error Handling**: Attempts to download in lower resolutions if the highest resolution is unavailable.
- **JSON Logging**: Logs video details to a JSON file after successful download.

## Install Dependencies
Install the required Python packages using:

`pip` pytube==12.1.1

## Install <b>FFmpeg<b> : 
<br>Link : https://ffmpeg.org/download.html</br><br><br>
<i>FFmpeg is required for merging video formats. Install it based on your operating system:</i><br>

<br><b>Windows</b>: Download from FFmpeg official website and add it to your PATH.</br>
<br><b>MacOS</b>: `brew` install ffmpeg</br>
<br><b>Linux</b>: `sudo apt-get` install ffmpeg<br>
