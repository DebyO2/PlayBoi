import pygame
import keyboard
from win32gui import GetWindowText, GetForegroundWindow
pygame.init()
running = True
paused = False

def toggled():
    global paused
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False        
    
    

def playSong(path : str,volume : int,Toloop : int):
    print("spacebar : pause/unpause")
    print("esc : stop")
    name = GetWindowText(GetForegroundWindow())
    pygame.mixer.music.load(path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(Toloop)
    while running:
        if paused or pygame.mixer.music.get_busy():
            pass
        else:
            print("finished playing")
            break

        event = keyboard.read_event()
        if(GetWindowText(GetForegroundWindow()) == name):
            if event.event_type == keyboard.KEY_DOWN and event.name == 'space':
                toggled()
            if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
                pygame.mixer.music.stop()
                break
    
if __name__ == '__main__':
    porth = input("Enter the path of the song: ")
    volune = int(input("Enter the volume(1-100): "))/100
    looop = int(input("To Loop? (0||1): "))*-1
    playSong(porth,volune,looop)