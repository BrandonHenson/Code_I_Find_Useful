import os
import shutil
import datetime
currentdate = datetime.date.today()
currentdate =(str(currentdate))
sourcePath = r'\\MUKGIS\GIS Files\Geodatabase\Water.gdb'
destPath = r'P:\GisBackup\Water.gdb'
for root, dirs, files in os.walk(sourcePath):

    #figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    #if we're in a directory that doesn't exist in the destination folder
    #then create a new folder
    if not os.path.isdir(dest):
        os.mkdir (dest)
        print 'Directory created at: ' + dest

    #loop through all files in the directory
    for f in files:

        #compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print 'File ' + f + ' copied.'
            except IOError:
                print 'file "' + f + '" already exists'



sourcePath = r'\\MUKGIS\GIS Files\Geodatabase\Sewer.gdb'
destPath = r'P:\GisBackup\Sewer.gdb'
for root, dirs, files in os.walk(sourcePath):

    #figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    #if we're in a directory that doesn't exist in the destination folder
    #then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print 'Directory created at: ' + dest

    #loop through all files in the directory
    for f in files:

        #compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print 'File ' + f + ' copied.'
            except IOError:
                print 'file "' + f + '" already exists'


sourcePath = r'\\MUKGIS\GIS Files\Geodatabase\Inspection_Information.idb'
destPath = r'P:\GisBackup\Inspection_Information.idb'
for root, dirs, files in os.walk(sourcePath):

    #figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    #if we're in a directory that doesn't exist in the destination folder
    #then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print 'Directory created at: ' + dest

    #loop through all files in the directory
    for f in files:

        #compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print 'File ' + f + ' copied.'
            except IOError:
                print 'file "' + f + '" already exists'




sourcePath = r'\\MUKGIS\GIS Files\FebCollector.gdb'
destPath = r'P:\GisBackup\FebCollector.gdb'
for root, dirs, files in os.walk(sourcePath):

    #figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    #if we're in a directory that doesn't exist in the destination folder
    #then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print 'Directory created at: ' + dest

    #loop through all files in the directory
    for f in files:

        #compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print 'File ' + f + ' copied.'
            except IOError:
                print 'file "' + f + '" already exists'


sourcePath = r'\\MUKGIS\GIS Files\Projects\Audit'
destPath = r'P:\GisBackup\Audit'
for root, dirs, files in os.walk(sourcePath):

    #figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    #if we're in a directory that doesn't exist in the destination folder
    #then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print 'Directory created at: ' + dest

    #loop through all files in the directory
    for f in files:

        #compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print 'File ' + f + ' copied.'
            except IOError:
                print 'file "' + f + '" already exists'


sourcePath = r'\\MUKGIS\GIS Files\Projects\GNet Data\Sewer.gdb'
destPath = r'P:\GisBackup\GNet Data Sewer.gdb'
for root, dirs, files in os.walk(sourcePath):

    #figure out where we're going
    dest = destPath + root.replace(sourcePath, '')

    #if we're in a directory that doesn't exist in the destination folder
    #then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print 'Directory created at: ' + dest

    #loop through all files in the directory
    for f in files:

        #compute current (old) & new file locations
        oldLoc = root + '\\' + f
        newLoc = dest + '\\' + f

        if not os.path.isfile(newLoc):
            try:
                shutil.copy2(oldLoc, newLoc)
                print 'File ' + f + ' copied.'
            except IOError:
                print 'file "' + f + '" already exists'
##
#######################################################################################                         RENAME WITH DATE
os.mkdir('P:/GisBackup/'+(str(currentdate)))

oldname1 = "P:\GisBackup\GNet Data Sewer.gdb"
NewName1 = "P:\GisBackup\GNet Data Sewer" + str(currentdate)+".gdb" 
os.rename(oldname1,NewName1)
##   
oldname2 = "P:\GisBackup\Water.gdb"
NewName2 = "P:\GisBackup\Water" + str(currentdate)+".gdb" 
os.rename(oldname2,NewName2)
##
oldname3 = "P:\GisBackup\Inspection_Information.idb"
NewName3 = "P:\GisBackup\Inspection_Information" + str(currentdate)+".idb" 
os.rename(oldname3,NewName3)
##
oldname4 = "P:\GisBackup\FebCollector.gdb"
NewName4 = "P:\GisBackup\FebCollector" + str(currentdate)+".gdb" 
os.rename(oldname4,NewName4)
##
oldname5 = "P:\GisBackup\Audit"
NewName5 = "P:\GisBackup\Audit"

##

oldname6 = "P:\GisBackup\Sewer.gdb"
NewName6 = "P:\GisBackup\Sewer" + str(currentdate)+".gdb" 
os.rename(oldname6,NewName6)

NewName7 = "P:\GisBackup\\" + str(currentdate)+"\Sewer.gdb"
os.rename(NewName6,NewName7)

NewName8 = "P:\GisBackup\\" + str(currentdate)+"\Audit.gdb"
os.rename(NewName5,NewName8)

NewName9 = "P:\GisBackup\\" + str(currentdate)+"\FebCollector.gdb"
os.rename(NewName4,NewName9)

NewName10 = "P:\GisBackup\\" + str(currentdate)+"\Information.idb"
os.rename(NewName3,NewName10)

NewName11 = "P:\GisBackup\\" + str(currentdate)+"\Water.gdb"
os.rename(NewName2,NewName11)

NewName12 = "P:\GisBackup\\" + str(currentdate)+"\GNet Data Sewer.gdb"
os.rename(NewName1,NewName12)

    

