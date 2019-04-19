#!/usr/bin/env python3
import os
import random
from shutil import copyfile
sourcefolder = input('Folder of your replacement pics')
#for folder, subfolders, files in os.walk(input('Folder to Wreck')):
for folder, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        if ".jpg" in file:
            filePath = os.path.join(os.path.abspath(folder), file)
            source = random.choice(os.listdir(sourcefolder))
            sourcePath = os.path.join(os.path.abspath(sourcefolder), source)
            copyfile(sourcePath, filePath)
