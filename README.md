# Python HLS Video Player

This is a simple video player built with Python's tkinter library and VLC to stream HLS (HTTP Live Streaming) content.

## Features

*   Plays HLS video streams.
*   Basic playback controls: Play, Pause, Stop.
*   Embeds the video within a tkinter GUI window.

## Requirements

*   Python 3
*   tkinter (usually included with Python)
*   python-vlc

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Install the required libraries:**
    ```bash
    pip install python-vlc
    ```
3.  **Run the application:**
    ```bash
    python test.py
    ```

## Configuration

The HLS stream URL can be configured in the `test.py` file:

```python
# HLS stream URL (tokenized .m3u8)
video_url = "https://myuhlsv2.hls-video.net/media2/token/a3f0c81db39d64f85b6f6a5cfaa1b2ce/stream.m3u8?token=f148eccea160313be734dd7c2bd5c574"
```
