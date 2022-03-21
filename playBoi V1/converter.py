import ffmpeg
import os
import time
def convert(path,name,destination):
    video = ffmpeg.input(path)

    audio = video.audio

    stream = ffmpeg.output(audio, os.path.join(destination,name+".mp3"))

    ffmpeg.run(stream)
    os.remove(path)
