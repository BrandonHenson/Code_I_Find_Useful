import getpass
import webbrowser
import os
import time
import shutil
import keyboard
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

ind2 = 0
dirs = os.listdir(path)
list1 = []
for file in dirs:
    file = path + '/' + str(file)
    with open(file, 'r') as f:
        LIST = []
        for line in f:
            if "Link To Map for MUKWA01:" in line:
                ind2 = ind2 + 1
                ind = (line.index("MUKWA01: "))
                ind1 = ind + 9
                line1 = line[ind1:]
                Type = line1
                LIST.append(Type)
                time.sleep(2)
                webbrowser.open(line1)
                time.sleep(2)
                keyboard.press_and_release('ctrl+p')
                time.sleep(2)
                keyboard.press_and_release('enter')
                time.sleep(2)
                keyboard.write(str('C:\\Users\\' + user + '\\Desktop\\MapLink' + today) + '\\' + str(today) + '_' + str(ind2))
                time.sleep(2)
                keyboard.press_and_release('enter')
                time.sleep(2)
os.system("taskkill /im chrome.exe /f")

dirs = os.listdir(path)
for file in dirs:
    file = path + '/' + str(file)
    if '.pdf' not in file:
        os.remove(file)
