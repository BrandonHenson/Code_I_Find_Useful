#http://survey123.arcgis.com/surveys

import datetime
import time
import keyboard
import webbrowser
import os
import shutil
import zipfile
now = datetime.datetime.now()
date = str(datetime.date)


list =['http://survey123.arcgis.com/surveys/0aea9858723047d890880287de41739f/data',
'http://survey123.arcgis.com/surveys/01b00bca04db48f2a2169e9249bc2abd/data',
'http://survey123.arcgis.com/surveys/d365f6ae516345fea3cd6c329234790b/data',
'http://survey123.arcgis.com/surveys/7641180a470b424d8182c7234c1495e5/data',
'http://survey123.arcgis.com/surveys/6c148b89ccde4cd18304faf632699296/data',
'http://survey123.arcgis.com/surveys/30790cb7ea9648d5b992a211bd3bc4d2/data',
'http://survey123.arcgis.com/surveys/ff4bed89defd416b9a4f8ce3135b4687/data',
'http://survey123.arcgis.com/surveys/a4f7d9a7d9d14962b6a48e89a2146872/data',
'http://survey123.arcgis.com/surveys/ceb279926ebc45bf97032bfa6a71262c/data',
'http://survey123.arcgis.com/surveys/306bc76b8a1244a881e833d0f653972b/data',
'http://survey123.arcgis.com/surveys/42313bcc9d764cd1998438b7a6ea0233/data',
'http://survey123.arcgis.com/surveys/afcb08ab540441ada3ba7fe7ca740b4a/data',
'http://survey123.arcgis.com/surveys/74461fa3a48d4fafb062b7c907f95491/data',
'http://survey123.arcgis.com/surveys/fa6182e31893459a89cbf10966f6ede8/data',
'http://survey123.arcgis.com/surveys/5a7a57a3a87c4edebcf2010bdda3b0cb/data',
'http://survey123.arcgis.com/surveys/b74ea9b11e714e3085f001bff9fb024c/data',
'http://survey123.arcgis.com/surveys/5ae5d46aa1264d12a0abe0a224c75a2f/data',
'http://survey123.arcgis.com/surveys/3d5ad6d387ea49f082191b2a5c91ccd7/data',
'http://survey123.arcgis.com/surveys/6092dd3a519f4ba3bede999fadbdba9e/data',
'http://survey123.arcgis.com/surveys/14b81c2892534934a13767863e8e596c/data',
'http://survey123.arcgis.com/surveys/b435439f591d4333837439785e2ec089/data',
]

print('Backing up Dailys.........')
ind = 21
for i in list:
    webbrowser.open(i)
    time.sleep(4)
    keyboard.press_and_release('ctrl + f')
    time.sleep(.7)
    keyboard.write('export')
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('enter')
    time.sleep(.25)
    keyboard.press_and_release('enter')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('enter')
    time.sleep(17)
    keyboard.press_and_release('ctrl + w')
    time.sleep(.5)
    ind = ind - 1
    print(str(ind)+ ' left')
#RENAME FILES ON SERVER
currentdate = datetime.date.today()
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\Cathodic_Protection.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\Cathodic_Protection.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_Cathodic_Protection.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RESERVOIR_INSPECTIONS.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RESERVOIR_INSPECTIONS.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_RESERVOIR_INSPECTIONS.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RES2_TRANSFER_PUMP.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RES2_TRANSFER_PUMP.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_RES2_TRANSFER_PUMP.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\FIRE_PUMPS.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\FIRE_PUMPS.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_FIRE_PUMPS.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\NONPERMIT_CONFINED.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\NONPERMIT_CONFINED.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_NONPERMIT_CONFINED.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\CONFINED_SPACE_PERMIT.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\CONFINED_SPACE_PERMIT.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_CONFINED_SPACE_PERMIT.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\GENERATORS.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\GENERATORS.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_GENERATORS.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\PFDAILY.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\PFDAILY.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_PFDAILY.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\S7.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\S7.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_S7.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\112TH.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\112TH.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_112TH.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\HOLLY.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\HOLLY.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_HOLLY.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS14.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS14.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS14.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS13.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS13.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS13.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS12.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS12.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS12.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS11.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS11.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS11.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS10.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS10.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS10.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS9.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS9.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS9.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS8.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS8.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS8.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS5.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS5.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS5.xlsx")
if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS2.xlsx"):
    os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS2.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS2.xlsx")
#MOVE AND RENAME FILES TO SERVER
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_0aea9858723047d890880287de41739f_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_0aea9858723047d890880287de41739f_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\Cathodic_Protection.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_01b00bca04db48f2a2169e9249bc2abd_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_01b00bca04db48f2a2169e9249bc2abd_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RESERVOIR_INSPECTIONS.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_d365f6ae516345fea3cd6c329234790b_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_d365f6ae516345fea3cd6c329234790b_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RES2_TRANSFER_PUMP.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_7641180a470b424d8182c7234c1495e5_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_7641180a470b424d8182c7234c1495e5_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\FIRE_PUMPS.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_6c148b89ccde4cd18304faf632699296_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_6c148b89ccde4cd18304faf632699296_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\ls dailys")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_30790cb7ea9648d5b992a211bd3bc4d2_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_30790cb7ea9648d5b992a211bd3bc4d2_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\NONPERMIT_CONFINED.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_ff4bed89defd416b9a4f8ce3135b4687_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_ff4bed89defd416b9a4f8ce3135b4687_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\CONFINED_SPACE_PERMIT.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_a4f7d9a7d9d14962b6a48e89a2146872_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_a4f7d9a7d9d14962b6a48e89a2146872_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\GENERATORS.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_ceb279926ebc45bf97032bfa6a71262c_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_ceb279926ebc45bf97032bfa6a71262c_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\PFDAILY.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_306bc76b8a1244a881e833d0f653972b_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_306bc76b8a1244a881e833d0f653972b_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\S7.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_42313bcc9d764cd1998438b7a6ea0233_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_42313bcc9d764cd1998438b7a6ea0233_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\112TH.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_afcb08ab540441ada3ba7fe7ca740b4a_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_afcb08ab540441ada3ba7fe7ca740b4a_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\HOLLY.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_74461fa3a48d4fafb062b7c907f95491_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_74461fa3a48d4fafb062b7c907f95491_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS14.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_fa6182e31893459a89cbf10966f6ede8_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_fa6182e31893459a89cbf10966f6ede8_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS13.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_5a7a57a3a87c4edebcf2010bdda3b0cb_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_5a7a57a3a87c4edebcf2010bdda3b0cb_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS12.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_b74ea9b11e714e3085f001bff9fb024c_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_b74ea9b11e714e3085f001bff9fb024c_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS11.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_5ae5d46aa1264d12a0abe0a224c75a2f_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_5ae5d46aa1264d12a0abe0a224c75a2f_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS10.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_3d5ad6d387ea49f082191b2a5c91ccd7_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_3d5ad6d387ea49f082191b2a5c91ccd7_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS9.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_6092dd3a519f4ba3bede999fadbdba9e_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_6092dd3a519f4ba3bede999fadbdba9e_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS8.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_14b81c2892534934a13767863e8e596c_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_14b81c2892534934a13767863e8e596c_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS5.xlsx")
if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_b435439f591d4333837439785e2ec089_EXCEL.xlsx"):
    shutil.move("C:\\Users\\brandonh\\Downloads\\S123_b435439f591d4333837439785e2ec089_EXCEL.xlsx","\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS2.xlsx")

currentdate = datetime.date.today()
currentdate = (str(currentdate))
sourcePath = r'\\MUKGIS\GIS Files\Geodatabase\Water.gdb'
destPath = r'P:\GisBackup\Water.gdb'
for root, dirs, files in os.walk(sourcePath):

    # figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    # if we're in a directory that doesn't exist in the destination folder
    # then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print('Directory created at: ' + dest)

    # loop through all files in the directory
    for f in files:

        # compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print('File ' + f + ' copied.')
            except IOError:
                print('file "' + f + '" already exists')

sourcePath = r'\\MUKGIS\GIS Files\Geodatabase\Sewer.gdb'
destPath = r'P:\GisBackup\Sewer.gdb'
for root, dirs, files in os.walk(sourcePath):

    # figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    # if we're in a directory that doesn't exist in the destination folder
    # then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print('Directory created at: ' + dest)

    # loop through all files in the directory
    for f in files:

        # compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print('File ' + f + ' copied.')
            except IOError:
                print('file "' + f + '" already exists')

sourcePath = r'\\MUKGIS\GIS Files\Projects\GNet Data\Sewer.gdb'
destPath = r'P:\GisBackup\GNet Data Sewer.gdb'
for root, dirs, files in os.walk(sourcePath):

    # figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    # if we're in a directory that doesn't exist in the destination folder
    # then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print('Directory created at: ' + dest)

    # loop through all files in the directory
    for f in files:

        # compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print('File ' + f + ' copied.')
            except IOError:
                print('file "' + f + '" already exists')
##
sourcePath = r'\\MUKGIS\GIS Files\Geodatabase\Flushing.gdb'
destPath = r'P:\GisBackup\Flushing.gdb'
for root, dirs, files in os.walk(sourcePath):

    # figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    # if we're in a directory that doesn't exist in the destination folder
    # then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print('Directory created at: ' + dest)

    # loop through all files in the directory
    for f in files:

        # compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print('File ' + f + ' copied.')
            except IOError:
                print('file "' + f + '" already exists')

############################################################################################
sourcePath = r'\\MUKGIS\GIS Files\Maps'
destPath = r'P:\GisBackup\Maps'
for root, dirs, files in os.walk(sourcePath):

    # figure out where we're going
    dest = 'P:\GisBackup\Maps'

    # if we're in a directory that doesn't exist in the destination folder
    # then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print('Directory created at: ' + dest)

    # loop through all files in the directory
    for f in files:

        # compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print('File ' + f + ' copied.')
            except IOError:
                print('file "' + f + '" already exists')

    ###################################################################################
    sourcePath = r'\\MUKGIS\GIS Files\Projects\SewerCleaning.gdb'
    destPath = r'P:\GisBackup\Projects'
    for root, dirs, files in os.walk(sourcePath):
        # figure out where we're going
        dest = destPath + root.replace(sourcePath, '')

    # if we're in a directory that doesn't exist in the destination folder
    # then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print('Directory created at: ' + dest)

    # loop through all files in the directory
    for f in files:

        # compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print('File ' + f + ' copied.')
            except IOError:
                print('file "' + f + '" already exists')
            #####################################################################################                         RENAME WITH DATE
os.mkdir('P:/GisBackup/' + (str(currentdate)))

oldname1 = "P:\GisBackup\GNet Data Sewer.gdb"
NewName1 = "P:\GisBackup\\" + str(currentdate) + "\GNet Data Sewer.gdb"
os.rename(oldname1, NewName1)

oldname2 = "P:\GisBackup\Water.gdb"
NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Water.gdb"
os.rename(oldname2, NewName2)

oldname2 = "P:\GisBackup\Sewer.gdb"
NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Sewer.gdb"
os.rename(oldname2, NewName2)
oldname2 = "P:\GisBackup\Flushing.gdb"
NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Flushing.gdb"
os.rename(oldname2, NewName2)
oldname2 = "P:\GisBackup\Maps"
NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Maps"
os.rename(oldname2, NewName2)

oldname2 = "P:\GisBackup\Projects"
NewName2 = "P:\GisBackup\\" + str(currentdate) + "\SewerCleaning"
os.rename(oldname2, NewName2)
##################################################################################
