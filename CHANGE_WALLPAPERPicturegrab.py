import ctypes
import winreg
import os
import random
import getpass
currentuser = getpass.getuser()
sourcefolder = ('C://Users//' + currentuser + '//Pictures//Wallpapers')

if not os.path.exists(sourcefolder):
    os.mkdir(sourcefolder)

for folder, subfolders, files in os.walk(sourcefolder):
    for file in files:
        if ".jpg" in file:
            filePath = os.path.join(os.path.abspath(folder), file)
            source = random.choice(os.listdir(sourcefolder))
            sourcePath = os.path.join(os.path.abspath(sourcefolder), source)
            regKey = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(regKey, "WallpaperStyle", 0, winreg.REG_SZ, "0")
            winreg.SetValueEx(regKey, "TileWallpaper", 0, winreg.REG_SZ, "0")
            ctypes.windll.user32.SystemParametersInfoW(20, 0, sourcePath)

