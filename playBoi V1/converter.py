import os
import subprocess
def convert(path,name):
    # subprocess.call(['ffmpeg', '-i' ,path, '-ac', '2', '-f', 'mp3', f'{name}.mp3'])
    subprocess.call(['ffmpeg', '-i', path, '-b:a', '192K', '-vn', f'{name}.mp3'],shell=True)
    os.remove(path)
    # os.system('cls')
