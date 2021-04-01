import os
import time
import keyboard


path = 'E:'
'''
for i in os.listdir(path):
    file = os.path.join(path+'\\'+i)
    if 'pdf' in file:
        #print(i)
'''
for folder, subfolders, files in os.walk(path):
    for file in files:
        if 'pdf' in file:
            filePath = os.path.join(os.path.abspath(folder), file)
            #print(filePath)
            keyboard.press_and_release('cmd')
            time.sleep(.25)
            keyboard.write(filePath)
            time.sleep(.25)
            keyboard.press_and_release('enter')
            time.sleep(1.5)
            keyboard.press_and_release('alt')
            time.sleep(.25)
            keyboard.press_and_release('f')
            time.sleep(.25)
            keyboard.press_and_release('a')
            time.sleep(.25)
            keyboard.press_and_release('tab')
            time.sleep(.25)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
    
            keyboard.press_and_release('down')
            time.sleep(.15)
            keyboard.press_and_release('down')
            time.sleep(.15)
    
            keyboard.press_and_release('enter')
            time.sleep(.25)
            keyboard.press_and_release('enter')
            time.sleep(5)
            keyboard.press_and_release('ctrl + q')
            time.sleep(1)

