import os
import time
from pynput.keyboard import Key, Controller
import threading

keyboard = Controller() 

def os_f(root,file):
    os.system(os.path.join(root, file)) #executing jpg file

# Указываем корневой каталог, с которого хотим начать обход
root_directory = r"D:\11\22"

# Используем цикл для обхода всех подкаталогов и файлов
for root, directories, files in os.walk(root_directory):
    for directory in directories:
        print("Подкаталог:", os.path.join(root, directory))
        
    thr1 = threading.Thread(target = os_f, args = (root, files[0]))
    thr1.start()
    for i in range(len(files)):
        time.sleep(5)
        keyboard.press(Key.right)


    # for file in files:
    #     if file.endswith('jpg'):
    #         print("Файл:", os.path.join(root, file))
    #         os.system(os.path.join(root, file))
    #     time.sleep(1)