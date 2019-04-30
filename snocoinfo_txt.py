import time
import keyboard
import webbrowser
import xlrd
import xlwt
import subprocess
list = []
data = xlrd.open_workbook('LIST.xlsx')
table = data.sheets()[0]
for k in range(table.nrows):
    list.append(table.row_values(k))

ind = 0
for i in list:
    parcel = (list[ind][0])
    ind = int(ind)+1
    strparcel = str(parcel)
    webbrowser.open('https://www.snohomishcountywa.gov/5167/Assessor')
    time.sleep(10)
    keyboard.press_and_release('ctrl + f')
    time.sleep(2)
    keyboard.press_and_release('ctrl + f')
    time.sleep(1)
    keyboard.write('parcel no.')
    time.sleep(1)
    keyboard.press_and_release('esc')
    time.sleep(1)
    keyboard.press_and_release('tab')
    time.sleep(1)
    keyboard.write(parcel)
    time.sleep(1)
    keyboard.press_and_release('tab')
    time.sleep(.5)
    keyboard.press_and_release('tab')
    time.sleep(.5)
    keyboard.press_and_release('tab')
    time.sleep(.5)
    keyboard.press_and_release('enter')
    time.sleep(7)
    keyboard.press_and_release('ctrl + a')
    time.sleep(1)
    keyboard.press_and_release('ctrl + c')
    time.sleep(1)
    txtfile = strparcel + '.txt'
    p = subprocess.Popen('C:\\WINDOWS\\system32\\notepad.exe')
    time.sleep(3)
    keyboard.press_and_release('ctrl + v')
    time.sleep(1)
    keyboard.press_and_release('ctrl + s')
    time.sleep(1)
    keyboard.write(txtfile)
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(1)
    p.kill()
