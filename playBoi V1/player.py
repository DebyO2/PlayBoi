import pygame
import keyboard
from win32gui import GetWindowText, GetForegroundWindow
import os

pygame.init()
running = True
paused = False
number_of_time_space_pressed = 0
name = ""
# name = "playboi"
def toggle(Global : bool):
    global number_of_time_space_pressed
    global paused
    global name
    if Global:
        if(GetWindowText(GetForegroundWindow()) == name):
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.pause()
                paused = True
                number_of_time_space_pressed +=1
            else:
                pygame.mixer.music.unpause()
                paused = False
                number_of_time_space_pressed +=1
    else :
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            paused = True
            number_of_time_space_pressed +=1
        else:
            pygame.mixer.music.unpause()
            paused = False
            number_of_time_space_pressed +=1

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


def playSong(path : str,offline :bool):
    global number_of_time_space_pressed
    number_of_time_space_pressed = 0
    global name
    name = GetWindowText(GetForegroundWindow())
    volume = int(input("Volume(1-100): "))/10
    Toloop = int(input("To Loop? (0||1): "))*-1
    # print(name)
    global paused
    global running
    running = True
    print("spacebar         : pause/unpause (within the window)")
    print("ctrl + spacebar  : pause/unpause (global shortcut)")
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
    keyboard.add_hotkey('ctrl+space', toggle,args=[(False)])
    keyboard.add_hotkey('shift+escape', leave,args=[(False)])
   
    while running:              
        if paused or pygame.mixer.music.get_busy():
            # print(GetWindowText(GetForegroundWindow()))
            # print(name)
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
    
    for _ in range(number_of_time_space_pressed):
        keyboard.press_and_release('backspace')
if __name__ == '__main__':
    porth = input("Enter the path of the song: ")
    playSong(porth,offline=True)
