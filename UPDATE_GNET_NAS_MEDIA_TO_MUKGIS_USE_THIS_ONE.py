import os
import shutil
import time
import datetime

input("Enter the date of the last sync")
year = int(input("4 digit year"))
month = int(input("1 or 2 digit month"))
day = int(input("1 or 2 digit day"))
datetostartfrom = datetime.datetime(year,month,day,0,0).timestamp()


for file in os.listdir("//muknas01/Videos/Photos"):
	file = os.path.join("//muknas01/Videos/Photos/" + file)
	ModTime = os.path.getmtime(file)
	if int(ModTime) > int(datetostartfrom):
		if ".JPG" in file:
			list = file.replace("//muknas01/Videos/Photos/","").split("~")
			folder = list[0]
			foldermkdir = "//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder)
			fileonly = list[1]
			copypath = str(os.path.join("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder) + "/" + str(fileonly)))

			if not os.path.exists(foldermkdir):
				os.mkdir(foldermkdir)
			shutil.copy(file, copypath)
			print("Copied " + file + " to " + copypath)

for file in os.listdir("//muknas01/Videos/Video"):
	file = os.path.join("//muknas01/Videos/Video/" + file)
	ModTime = os.path.getmtime(file)
	if int(ModTime) > int(datetostartfrom):
		if ".mpg" in file:
			list = file.replace("//muknas01/Videos/Video/","").split("~")
			folder = list[1]
			foldermkdir = "//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder)
			fileonly = list[2]
			copypath = str(os.path.join("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder) + "/" + str(fileonly)))
			if not os.path.exists(foldermkdir):
				os.mkdir(foldermkdir)
			shutil.copy(file, copypath)
			print("Copied " + file + " to " + copypath)
