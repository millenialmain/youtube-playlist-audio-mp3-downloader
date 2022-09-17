from pytube.contrib.playlist import Playlist
from pytube import YouTube
from pytube.cli import on_progress
import os

url = input("Enter Playlist URL: ")
playlist = Playlist(url)
print("Total Videos: ",len(playlist.video_urls))
print("Enter the destination address (leave blank to save in current directory)")
destination = str(input(" ")) or '.'

for video_url in playlist.video_urls:
    yt=YouTube(video_url,on_progress_callback=on_progress)
    stream=yt.streams.filter(only_audio=True).first()
    print(yt.title)
#   stream.download(filename=yt.title+".mp3")
    out_file = stream.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " has been successfully downloaded.")