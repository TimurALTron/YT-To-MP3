##############################
#### YOUTUBE VIDEO > MP3 #####
##############################

import pytube
from moviepy.editor import *

url_ = input("URL: ")
youtube = pytube.YouTube(url_)
video_name = youtube.title
print(f"Name:  {video_name}")

stream = youtube.streams.first()
stream.download()

cnvmp3 = input("Convert to mp3? Y/n ")

if cnvmp3 == "Y" or cnvmp3 == "y":
    print("Converting to mp3")
    mp4_file = f"{video_name}.mp4"
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    mp3_file = f"{video_name}.mp3"
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()
    print("Done")
elif cnvmp3 == "n" or cnvmp3 == "N": print("MP4 Downloaded")