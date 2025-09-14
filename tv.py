import tkinter as tk
from tkinter import ttk
import vlc

# -------------------------------
# CONFIGURATION
# -------------------------------
# HLS stream URL (tokenized .m3u8)
video_url = "YOUR_HLS_STREAM_URL_HERE"

# VLC instance (no headers required on Windows; VLC handles HLS)
vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()
media = vlc_instance.media_new(video_url)
player.set_media(media)

# -------------------------------
# GUI SETUP
# -------------------------------
root = tk.Tk()
root.title("Python HLS Video Player")
root.geometry("900x500")

video_frame = tk.Frame(root, bg="black")
video_frame.pack(fill=tk.BOTH, expand=1)

# Assign VLC video output to the Tkinter frame
root.update()
if hasattr(player, 'set_hwnd'):  # Windows
    player.set_hwnd(video_frame.winfo_id())
else:  # Linux / Mac
    player.set_xwindow(video_frame.winfo_id())

# -------------------------------
# CONTROL BUTTONS
# -------------------------------
control_frame = ttk.Frame(root)
control_frame.pack(fill=tk.X)

def play_video():
    player.play()

def pause_video():
    player.pause()

def stop_video():
    player.stop()

play_btn = ttk.Button(control_frame, text="Play", command=play_video)
play_btn.pack(side=tk.LEFT, padx=5, pady=5)

pause_btn = ttk.Button(control_frame, text="Pause", command=pause_video)
pause_btn.pack(side=tk.LEFT, padx=5, pady=5)

stop_btn = ttk.Button(control_frame, text="Stop", command=stop_video)
stop_btn.pack(side=tk.LEFT, padx=5, pady=5)

# -------------------------------
# RUN GUI
# -------------------------------
root.mainloop()