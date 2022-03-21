import pygame
import keyboard
from win32gui import GetWindowText, GetForegroundWindow
pygame.init()
running = True
paused = False
name = GetWindowText(GetForegroundWindow())

def toggled():
    global paused
    global name
    if(GetWindowText(GetForegroundWindow()) == name):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            paused = True
        else:
            pygame.mixer.music.unpause()
            paused = False        
    
def leave():
    global running
    global name
    if(GetWindowText(GetForegroundWindow()) == name):
        running = False
        pygame.mixer.music.stop()

def toggledchk():
    global paused
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False        
    
def leavechk():
    global running
    running = False
    pygame.mixer.music.stop()

def playSong(path : str,volume : int,Toloop : int):
    print("spacebar         : pause/unpause (within the window)")
    print("shift + spacebar : pause/unpause (global shortcut)")
    print("esc              : stop          (within the window)")
    print("shift + esc      : stop          (global shortcut)\n")
    pygame.mixer.music.load(path)
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(Toloop)
    keyboard.add_hotkey('space', toggled)
    keyboard.add_hotkey('escape', leave)
    keyboard.add_hotkey('shift+space', toggledchk)
    keyboard.add_hotkey('shift+escape', leavechk)
    while running:
        if paused or pygame.mixer.music.get_busy():
            pass
        else:
            break
    print("finished playing")
        
    
if __name__ == '__main__':
    porth = input("Enter the path of the song: ")
    volune = int(input("Enter the volume(1-100): "))/100
    looop = int(input("To Loop? (0||1): "))*-1
    playSong(porth,volune,looop)
