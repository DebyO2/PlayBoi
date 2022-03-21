from moviepy.editor import *
import os
def convert(mp4, mp3):
    mp4_without_frames = AudioFileClip(mp4)     
    mp4_without_frames.write_audiofile(mp3)    
    mp4_without_frames.close() # function call mp4_to_mp3("my_mp4_path.mp4", "audio.mp3")
    os.remove(mp4)
