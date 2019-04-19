#!/usr/bin/env python3
import os
import getpass
currentuser = getpass.getuser()
import random
from shutil import copyfile
#sourcefolder = input('Folder of your replacement pics')
for folder, subfolders, files in os.walk('C://Users//' + currentuser):
    for file in files:
        if ".jpg" in file:
            filePath = os.path.join(os.path.abspath(folder), file)
            print(filePath)
            #source = random.choice(os.listdir(sourcefolder))
            #sourcePath = os.path.join(os.path.abspath(sourcefolder), source)
            #copyfile(sourcePath, filePath)

        #elif ".tif" in file:
            #filePath = os.path.join(os.path.abspath(folder), file)
            #print(filePath)
            #source = random.choice(os.listdir(sourcefolder))
            #sourcePath = os.path.join(os.path.abspath(sourcefolder), source)
            #copyfile(sourcePath, filePath)

        #elif ".pdf" in file:
            #filePath = os.path.join(os.path.abspath(folder), file)
            # print(filePath)
            # source = random.choice(os.listdir(sourcefolder))
            # sourcePath = os.path.join(os.path.abspath(sourcefolder), source)
            # copyfile(sourcePath, filePath)
