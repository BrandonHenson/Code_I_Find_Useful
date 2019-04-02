import os
import arcpy
os.mkdir('//MUKGIS/GIS Files/CollectorSync')
arcpy.CreateFileGDB_management(out_folder_path="//MUKGIS/GIS Files/CollectorSync",out_name="CollectorSync",out_version="CURRENT")
