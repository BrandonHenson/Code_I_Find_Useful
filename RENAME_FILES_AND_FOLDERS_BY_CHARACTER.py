import os
import shutil

location = input('WHERE?')
badletter = input('BAD CHARACTER')
goodletter = input('GOOD CHARACTER')
savefile = open('NAME_CHANGES.txt', 'a')
savefile.write('Changed ' + badletter + ' to ' + goodletter + '\n')
savefile.close()

def fileobj():
    for folder, subfolders, files in os.walk(location):
        for file in files:
            filePath = os.path.join(os.path.abspath(folder), file)
            newfilepath = os.path.join(os.path.abspath(folder), file.replace(badletter, goodletter))
            if badletter in file:
                os.rename(filePath, newfilepath)



for folder, subfolders, files in os.walk(location):
    for file in files:
        folderpath = os.path.join(os.path.abspath(folder))
        newfolderpath = folderpath.replace(badletter, goodletter)
        if badletter in folderpath:
            shutil.copytree(folderpath, newfolderpath)
            shutil.rmtree(folderpath)

fileobj()


