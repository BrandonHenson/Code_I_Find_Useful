import os
import sys
import getpass
from bs4 import BeautifulSoup
import urllib.request
import os
import json
from hashlib import sha1
from queue import Queue
from threading import Thread
import getpass
import ctypes
import winreg
import random
user = getpass.getuser()
DIR = 'C://Users//' + user + '//Pictures//Wallpapers'
for folder, subfolders, files in os.walk(DIR):
    for file in files:
        filePath = os.path.join(os.path.abspath(folder), file)
        print(filePath)
        sourcefolder = DIR
        if ".jpg" in file:
            filePath = os.path.join(os.path.abspath(folder), file)
            source = random.choice(os.listdir(sourcefolder))
            sourcePath = os.path.join(os.path.abspath(sourcefolder), source)
            regKey = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(regKey, "WallpaperStyle", 0, winreg.REG_SZ, "0")
            winreg.SetValueEx(regKey, "TileWallpaper", 0, winreg.REG_SZ, "0")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, filePath)
