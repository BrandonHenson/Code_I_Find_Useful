'''
Brandon Henson
open arcgisonline, download dailys, extract, replace on server
3/28/19
'''
import datetime
import zipfile
import os
import time
import keyboard
import webbrowser

dir_name = 'C:/Users/brandonh/Downloads'
extension = ".zip"
os.chdir(dir_name)
for item in os.listdir(dir_name):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        os.remove(file_name)

now = datetime.datetime.now()
webbrowser.open('http://mukilteowwd.maps.arcgis.com/home/item.html?id=473432d4fa3c429e8a4eb0d6308c6a40')
time.sleep(10)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('enter')
time.sleep(20)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('enter')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('enter')
time.sleep(.25)
keyboard.write(str(now))
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.write('update')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('enter')
time.sleep(40)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('enter')
time.sleep(45)
dir_name = 'C:/Users/brandonh/Downloads'
extension = ".zip"
os.chdir(dir_name)
for item in os.listdir(dir_name):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall("//mukgis/GIS Files/Daily's/Dailys2019")
        zip_ref.close()
        os.remove(file_name)
