import asyncio
from youtubesearchpython.__future__ import VideosSearch
import os
import downloader
import player

# current_path = os.getcwd()

#Global
SongLink = ""

# destiny = os.path.join(current_path,"music")
destiny = "music"

async def search(query):

    videosSearch = VideosSearch(query, limit = 3)
    videosResult = await videosSearch.next()
    
    result = videosResult["result"]

    Songs = {}

    for i in result:
        print("\n")
        print(f'({list(result).index(i)+1}) By: {i["channel"]["name"]} ||\nTitle: "{i["title"]}" ||\nLink : "{i["link"]}"')

        Songs.update({i["title"] : i["link"]})
    
    songIndex = int(input("\nWhich song do u want to play(1 || 2 || 3): ")) - 1

    SongLink = Songs[list(Songs)[songIndex]]
    
    sung = downloader.DownloadMusic(SongLink)

    print(f"playing: {sung[2]} ....")

    if sung[0] == True:
        volume = int(input("Volume(1-100): "))/10
        loopTo = int(input("To Loop? (0||1): "))*-1
        player.playSong(sung[1],volume,loopTo)
    elif sung[0] == False:
        print("the song is already downloaded,will be played from the database")
        volume = int(input("Volume(1-100): "))/10
        loopTo = int(input("To Loop? (0||1): "))*-1
        player.playSong(sung[1],volume,loopTo)
        

if __name__ == '__main__':

    while True:
        command = input("\nEnter your command(for now only play and exit exists): ")

        if command == 'play':
            mode = input("\nEnter your mode(offline/online): ")

            if mode == 'offline':
                # print(os.getcwd())
                # os.chdir(current_path)
                foles = list(os.listdir(destiny))
                sang = ""
                
                for j in foles:
                    print(f"{foles.index(j) + 1} || {j}")
                    
                songtoplay = int(input("\nWhich song do u want to play(1,2,3...): ")) - 1
                
                sang = foles[songtoplay]

                poth = os.path.join(destiny,sang).replace('\\',r"\\")

                volume = int(input("Volume(1-100): "))/10
                loopTo = int(input("To Loop? (0||1): "))*-1
                
                print(f"playing: {sang} ....")

                player.playSong(poth,volume,loopTo)

            
            elif mode == "online":

                name = input("Enter the music name and if possible then add by (artist): ")
        
                asyncio.run(search(name))

        elif command == "exit":
            exit()