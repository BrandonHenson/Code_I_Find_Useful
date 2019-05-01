import ctypes
import getpass
import random
import os

user = getpass.getuser()
DIR = 'C:\\Users\\' + user + '\\Pictures\\Wallpapers\\'
if not os.path.exists(DIR):
    os.makedirs(DIR)
rand = str(random.randint(1,40))
name = rand + '.jpg'
ind = 0
for folder, subfolders, files in os.walk(DIR):
    for file in files:
        filePath = os.path.join(os.path.abspath(folder), file)
        sourcefolder = DIR

        if ".jpg" in file:
            ind = ind + 1
            os.rename(filePath, os.path.join(os.path.abspath(folder), str(ind) + '.jpg'))


filepath = str(DIR + name)
file_name = filepath
ctypes.windll.user32.SystemParametersInfoW(20, 0, file_name , 0)
print(filepath)
