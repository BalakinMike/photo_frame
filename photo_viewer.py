import os
import time
import pynput
from pynput.keyboard import Key, Controller
import threading
import subprocess

keyboard = Controller()
def os_f(root,file):
    os.system(os.path.join(root, file))

def key_emulation(root, files):
    thr1 = threading.Thread(target = os_f, args = (root, files[0]))
    thr1.start()
    for i in range(len(files)):
        time.sleep(5)
        keyboard.press(Key.right)
    with keyboard.pressed(Key.alt_l):
        keyboard.press(Key.f4)

root_directory = r"D:\ProjectPython\My_Projects\photo_frame\input"
for root, directories, files in os.walk(root_directory):
    
    for file in files:
        if file.endswith('jpg'):
            key_emulation(root, files)
            
            break
    
# subprocess.call(["taskkill", "/F", "/IM", "C:\Program Files\HONOR\PCManager\HnPhotoViewer.exe"])
#"C:\Program Files\HONOR\PCManager\HnPhotoViewer.exe"