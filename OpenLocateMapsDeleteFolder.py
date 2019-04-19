import getpass
import webbrowser
import os
import time
import shutil
import random
today = (time.strftime("%m_%d_%Y"))
user = getpass.getuser()
strpath = str('C:/Users/' + user + '/Desktop/MapLink' + today)
os.mkdir(strpath)
path = strpath
serverpath = "S:/LOCATES/"
server = os.listdir("S:/LOCATES")
servdirs = os.listdir(path)
for item in server:
    if '.doc' in item and '~' not in item:
        source = serverpath + str(item)
        destination = path + '/' + str(item) + '.txt'
        shutil.copy(source, destination)


dirs = os.listdir(path)
list1 = []
for file in dirs:
    file = path + '/' + str(file)
    with open(file, 'r') as f:
        LIST = []
        for line in f:
            if "Link To Map for MUKWA01:" in line:
                ind = (line.index("MUKWA01: "))
                ind1 = ind + 9
                line1 = line[ind1:]
                Type = line1
                LIST.append(Type)
                webbrowser.open(line1)

dirs = os.listdir(path)
for file in dirs:
    file = path + '/' + str(file)
    if '.txt' in file:
        os.remove(file)
indrename = random.randint(1, 100)
os.rename(path, 'C:/Users/' + user + '/Desktop/' + 'DELETE_THIS_FOLDER' + str(indrename))
