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
    python tv.py
    ```

## Configuration

The HLS stream URL can be configured in the `tv.py` file:

```python
# HLS stream URL (tokenized .m3u8)
video_url = "YOUR_HLS_STREAM_URL_HERE"
```