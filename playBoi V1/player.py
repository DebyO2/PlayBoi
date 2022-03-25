import pygame
import keyboard
from win32gui import GetWindowText, GetForegroundWindow
import os

pygame.init()
running = True
paused = False
name = GetWindowText(GetForegroundWindow())


def toggle(Global : bool):
    global paused
    global name
    if Global:
        if(GetWindowText(GetForegroundWindow()) == name):
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                paused = True
            else:
                pygame.mixer.music.unpause()
                paused = False
            
    else :
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            paused = True
        else:
            pygame.mixer.music.unpause()
            paused = False

def leave(Global : bool):
    global running
    global name
    
    if Global:
        if(GetWindowText(GetForegroundWindow()) == name):
            running = False
            pygame.mixer.music.stop()
            
    else :
        running = False
        pygame.mixer.music.stop()


def playSong(path : str,volume : int,Toloop : int,offline :bool):
    global paused
    global running
    running = True
    print("spacebar         : pause/unpause (within the window)")
    print("shift + spacebar : pause/unpause (global shortcut)")
    print("esc              : stop          (within the window)")
    print("shift + esc      : stop          (global shortcut)\n")
    try :
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(Toloop)
    except:
        print("oops looks like the song doesn't exist are u drunk or something? ")
        return
    keyboard.add_hotkey('space', toggle,args=[(True)])
    keyboard.add_hotkey('escape', leave,args=[(True)])
    keyboard.add_hotkey('shift+space', toggle,args=[(False)])
    keyboard.add_hotkey('shift+escape', leave,args=[(False)])
   
    while running:              
        if paused or pygame.mixer.music.get_busy():
            continue   
        else:
            print("finished playing")
            break
    

    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    keyboard.unhook_all_hotkeys()

    if offline:
        pass
    else:
        todelete = input("save song? (y/n) : ")
        if todelete == "y":
            print("saved")
        elif todelete == "n":
            os.remove(path)
            print("deleted")
if __name__ == '__main__':
    porth = input("Enter the path of the song: ")
    volune = int(input("Enter the volume(1-100): "))/100
    looop = int(input("To Loop? (0||1): "))*-1
    playSong(porth,volune,looop,offline=True)
