##import os, sys
##
#########################                     list all folders              
####for folder, subfolders, files in os.walk(os.getcwd()):
####    for file in files:
####        filePath = os.path.join(os.path.abspath(folder), file)
####        print subfolders
######      THIS FILE HAS TO BE IN THE FOLDER OF THE INTENDED TARGET
##
##
########################                   list all files including in subdirectories               
##for folder, subfolders, files in os.walk(os.getcwd()):
##    for file in files:
##        filePath = os.path.join(os.path.abspath(folder), file)
##        print files
####      THIS FILE HAS TO BE IN THE FOLDER OF THE INTENDED TARGET
##
##
#########################                  list absolute paths including in subdirectories              
##
##for folder, subfolders, files in os.walk(os.getcwd()):
##    for file in files:
##        filePath = os.path.join(os.path.abspath(folder), file)
##        print filePath
####      THIS FILE HAS TO BE IN THE FOLDER OF THE INTENDED TARGET
##
##
########################             list all files without subdirectory files              
##  # Open a file
##path = "C:/Users/brandonh/Desktop/New folder (2)"
##dirs = os.listdir( path )
##
### This would print all the files and directories
##for file in dirs:
##   print file
##
##
#####################      move files to different locations          
##
##old_file=os.path.join("C:/Users/brandonh/Desktop/AccountFolders/1")
##new_file=os.path.join("C:/Users/brandonh/Desktop/AccountFolders/ACCT 1 Add 2600 100TH ST SW ")
##os.rename(old_file,new_file)
##
##
#######################               Rename Folders                    
##os.rename("C:/Users/brandonh/Desktop/AccountFolders/9701","C:/Users/brandonh/Desktop/AccountFolders/_Account_9701")
##
##
#########################                 Make Folders                             
##os.mkdir('1')
##
##
##########################                 Delete entire folder tree                
##import os
##import datetime
##import arcpy
##import shutil
##shutil.rmtree('//MUKGIS/GIS Files/CollectorSync')
##
#####################                       Backup Files
##import os
##import shutil
##import datetime
##currentdate = datetime.date.today()
##currentdate =(str(currentdate))
##sourcePath = r'C:\Users\brandonh\Desktop\TestFolder'
##destPath = r'P:\TestDelete'
##for root, dirs, files in os.walk(sourcePath):
##
##    #figure out where we're going
##    dest = destPath + root.replace(sourcePath, '')
##
##    #if we're in a directory that doesn't exist in the destination folder
##    #then create a new folder
##    if not os.path.isdir(dest):
##        os.mkdir (dest)
##        print 'Directory created at: ' + dest
##
##    #loop through all files in the directory
##    for f in files:
##
##        #compute current (old) & new file locations
##        oldLoc = root + '\\' + f
##        newLoc = dest + '\\' + f
##
##        if not os.path.isfile(newLoc):
##            try:
##                shutil.copy2(oldLoc, newLoc)
##                print 'File ' + f + ' copied.'
##            except IOError:
##                print 'file "' + f + '" already exists'
##

