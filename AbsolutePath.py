import os, sys

for folder, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        filePath = os.path.join(os.path.abspath(folder), file)
        print filePath
##      THIS FILE HAS TO BE IN THE FOLDER OF THE INTENDED TARGET
