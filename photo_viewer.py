import os
import time
import pynput
from pynput.keyboard import Key, Controller
import threading
import subprocess

keyboard = Controller()

def os_f(root,file):
    '''Procedure starting file Viewer'''
    os.system(os.path.join(root, file))

def key_emulation(root, files):
    '''Procedure emulating keyboard actions'''
    thr1 = threading.Thread(target = os_f, args = (root, files[0]))
    thr1.start()
    for i in range(len(files)): # Searching through files
        time.sleep(5) # Time delay for viewing photos
        keyboard.press(Key.right)
    with keyboard.pressed(Key.alt_l): # Keyboard action emulation (Alt+F4) for switch off ImageViewer
        keyboard.press(Key.f4)

root_directory = r"D:\ProjectPython\My_Projects\photo_frame\input"

for root, directories, files in os.walk(root_directory):
    
    for file in files:
        if file.endswith('jpg'):
            key_emulation(root, files)
            break
    
