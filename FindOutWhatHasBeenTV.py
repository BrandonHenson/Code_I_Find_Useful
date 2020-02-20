import os
import shutil
import datetime
from datetime import date

filecsv = open("C:/Users/brandonh/Desktop/TV'd_SewerLines.csv","a")
list = []
for folder, subfolders, files in os.walk("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS"):
    for file in files:
        folder = folder.replace("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS\\","")
        filePath = os.path.join(os.path.abspath(folder), file)
        if folder in list:
            pass
        else:
            list.append(folder)
filecsv.write("CodeToPasteInGIS_SelectFrom"+"\n")
for i in list:
    filecsv.write("Mains_Gravity.Asset_ID = '" + i + "' OR" + "\n")
