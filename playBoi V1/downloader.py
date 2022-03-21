# importing packages
from pytube import YouTube
import os
import converter
from pytube.helpers import safe_filename


def DownloadMusic(link : str):
    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()
    destination = "music"
    name = safe_filename(yt.title)+".mp3"
    list = os.listdir(destination)

    if name in list:
        return [False,os.path.join(destination,name),name]
    else: 
        # print("nope")
        out_file = video.download(output_path=destination) #download of the video
        base, ext = os.path.splitext(out_file)
        base = base+".mp3"
        converter.convert(out_file,os.path.join(destination,base))
        os.system('cls')
        return [True,os.path.join(destination,base),name]

if __name__ == '__main__':
    linko = input("Give the link of the song u wanna downlaod it will be downlaoded in music folder :")
    DownloadMusic(linko)
