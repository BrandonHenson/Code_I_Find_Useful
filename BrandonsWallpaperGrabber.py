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
WORKER_THREADS = 40

q = Queue()


def worker():
    while True:
        resData = q.get()
        if resData is None:
            break
        link = resData[0]
        Type = resData[1]
        DIR = resData[2]
        try:
            req = urllib.request.Request(link)
            req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36")
            res = urllib.request.urlopen(req)
            raw_img = res.read()
            filename = str(sha1(link.encode()).hexdigest()) + "." + Type
            if len(Type) != 0 and res.info().get("Content-Type") != "text/html":
                f = open(os.path.join(DIR, filename), 'wb')
                f.write(raw_img)
                f.close()
        except Exception as e:
            print("could not load : " + link)
            print(e)
        q.task_done()


def get_soup(url, header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url, headers=header)), 'html.parser')


query = input('What wallpapers do you want?\n')
query = query.split()
query = '+'.join(query)
url = "https://www.google.com/search?q=" + query + "&source=lnms&tbm=isch"
DIR = 'C://Users//' + user + '//Pictures//Wallpapers'
if not os.path.exists(DIR):
    os.makedirs(DIR)

header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
          }
soup = get_soup(url, header)
if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])
if not os.path.exists(DIR):
            os.mkdir(DIR)
for i in range(WORKER_THREADS):
    t = Thread(target=worker)
    t.daemon = True
    t.start()
for a in soup.find_all("div", {"class": "rg_meta"}):
    link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
    q.put([link, Type, DIR])

q.join()
print('Downloaded to ' + str(DIR))

currentuser = getpass.getuser()
sourcefolder = (DIR)


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
