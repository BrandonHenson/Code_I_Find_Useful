import os
import keyboard
import time
import xlrd


newtvdlist = []
listofalreadydone = []
keyboard.press_and_release('cmd')
time.sleep(.25)
keyboard.write("\\\\MUKGIS\\GIS Files\\Maps\\TV'D.mxd")
time.sleep(1)
keyboard.press_and_release('enter')
time.sleep(15)
keyboard.press_and_release('alt')
time.sleep(.25)
keyboard.press_and_release('g')
time.sleep(.25)
keyboard.press_and_release('enter')
time.sleep(2)
keyboard.press_and_release('p')
time.sleep(3)
keyboard.write('arcpy.TableToExcel_conversion(Input_Table="TV_D_AT_SOME_POINT", Output_Excel_File="C:/Users/brandonh/Desktop/tv_d.xls", Use_field_alias_as_column_header="NAME", Use_domain_and_subtype_description="CODE")')
time.sleep(1)
keyboard.press_and_release('enter')
time.sleep(10)
os.system("taskkill /f /im ArcMap.exe")
time.sleep(2)
keyboard.press_and_release('cmd')
time.sleep(.5)
keyboard.write("C:\\Users\\brandonh\\Desktop\\tv_d.xls")
time.sleep(2)
keyboard.press_and_release('enter')
time.sleep(2)
keyboard.press_and_release('enter')
time.sleep(5)
keyboard.press_and_release('alt')
time.sleep(1.5)
keyboard.press_and_release('f')
time.sleep(1.5)
keyboard.press_and_release('a')
time.sleep(1.5)
keyboard.press_and_release('1')
time.sleep(1.5)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('down')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('enter')
time.sleep(.25)
keyboard.press_and_release('enter')
time.sleep(2)
os.system("taskkill /f /im EXCEL.EXE")


list1 = []
data = xlrd.open_workbook("tv_d.xlsx")
table = data.sheets()[0]
for k in range(table.nrows):
    list1.append(table.row_values(k))
ind = 0
for i in list1:
    assetid = (list1[ind][8])
    listofalreadydone.append(str(assetid))
    ind = ind + 1



filecsv = open("C:/Users/brandonh/Desktop/TV'd_SewerLines.csv", "a")
list = []
for folder, subfolders, files in os.walk("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS"):
    for file in files:
        folder = folder.replace("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS\\", "")
        filePath = os.path.join(os.path.abspath(folder), file)
        if folder in list:
            pass
        else:
            list.append(folder)
for i in list:
    filecsv.write(i + "\n")
#filecsv.write('\n\nIGNORE \nColson 01\nGM0230\nGmbh51\nGMO580RD\nGM_BH_27')
filecsv.close()
time.sleep(1)
keyboard.press_and_release('cmd')
time.sleep(.25)
keyboard.write("C:\\Users\\brandonh\\Desktop\\TV'd_SewerLines.csv")
time.sleep(1)
keyboard.press_and_release('enter')
time.sleep(2)
keyboard.press_and_release('alt')
time.sleep(.5)
keyboard.press_and_release('f')
time.sleep(.5)
keyboard.press_and_release('a')
time.sleep(.5)
keyboard.press_and_release('1')
time.sleep(.5)
keyboard.press_and_release('tab')
time.sleep(.25)
keyboard.press_and_release('down')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('up')
time.sleep(.25)
keyboard.press_and_release('enter')
time.sleep(.25)
keyboard.press_and_release('enter')
time.sleep(2)
os.system("taskkill /f /im EXCEL.EXE")

list = []
data = xlrd.open_workbook("TV'd_SewerLines.xlsx")
table = data.sheets()[0]
for k in range(table.nrows):
    if table.row_values(k) not in list:
        list.append(table.row_values(k))
ind = 0
for i in list:
    assetid = (list[ind][0])
    newtvdlist.append(str(assetid))
    #print(str(assetid))
    ind = ind + 1


keyboard.press_and_release('cmd')
time.sleep(.25)
keyboard.write("\\\\MUKGIS\\GIS Files\\Maps\\TV'D.mxd")
time.sleep(1)
keyboard.press_and_release('enter')
time.sleep(15)
keyboard.press_and_release('alt')
time.sleep(.25)
keyboard.press_and_release('s')
time.sleep(.25)
keyboard.press_and_release('a')
time.sleep(.25)
keyboard.press_and_release('m')
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

for i in newtvdlist:
    if i not in listofalreadydone:
        if "\\" not in i:
            if ".0" not in i:
                #print("Add " + i)
                keyboard.write("Asset_ID ='")
                time.sleep(.25)
                keyboard.write(i)
                keyboard.write("'OR\n")