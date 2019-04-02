'''
Brandon Henson
Download shapefiles and update on \\mukgis
3/28/19
'''

import webbrowser
import zipfile
import os
import time

dir_name = 'C:/Users/brandonh/Downloads'
extension = ".zip"
os.chdir(dir_name)
for item in os.listdir(dir_name):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        os.remove(file_name)


webbrowser.open('ftp://ftp.snoco.org/Assessor/shapefiles/lots.zip')
webbrowser.open('ftp://ftp.snoco.org/assessor/shapefiles/muni_annexations.zip')
webbrowser.open('ftp://ftp.snoco.org/Assessor/shapefiles/allparcels.zip')
webbrowser.open('ftp://ftp.snoco.org/assessor/shapefiles/plss.zip')
webbrowser.open('ftp://ftp.snoco.org/assessor/shapefiles/rows.zip')
webbrowser.open('ftp://ftp.snoco.org/Assessor/shapefiles/parcelcent.zip')
webbrowser.open('ftp://ftp.snoco.org/Assessor/shapefiles/parcels.zip')

time.sleep(55)
dir_name = 'C:/Users/brandonh/Downloads'
extension = ".zip"
os.chdir(dir_name)

for item in os.listdir(dir_name):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall('//mukgis/GIS Files/Geodatabase/Snohomish County Updated')
        zip_ref.close()
        os.remove(file_name)
