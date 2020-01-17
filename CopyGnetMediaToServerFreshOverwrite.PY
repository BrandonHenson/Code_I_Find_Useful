import shutil
import os
import xlrd
import csv
import pyodbc
import glob
from xlsxwriter.workbook import Workbook
input("Last Run on 1/9/2020 (Change This Date!)")

DESKTOPPATH = "C:\\Users\\brandonh\\Desktop\\GNET_OBSERVATIONS_AND_LINKS\\"
if not os.path.exists(DESKTOPPATH):
    os.mkdir(DESKTOPPATH)
    print("Created Folder")
shutil.copy("\\\\mukgis\\GIS Files\\Projects\\GNet Data\\GNET\\GNetObservation.mdb", DESKTOPPATH)
print("Copied \\\\mukgis\\GIS Files\\Projects\\GNet Data\\GNET\\GNetObservation.mdb to folder")

MDB = 'C:/Users/brandonh/Desktop/GNET_OBSERVATIONS_AND_LINKS/GNetObservation.mdb'
DRV = '{Microsoft Access Driver (*.mdb)}'
PWD = 'pw'


con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()


SQL = 'SELECT * FROM GNet_WwMainlineObservation;'
rows = cur.execute(SQL).fetchall()
cur.close()
con.close()

with open('C:/Users/brandonh/Desktop/GNET_OBSERVATIONS_AND_LINKS/Current_Obs.csv' , 'w') as fou:
    csv_writer = csv.writer(fou)
    csv_writer.writerows(rows)


for csvfile in glob.glob(os.path.join('C:/Users/brandonh/Desktop/GNET_OBSERVATIONS_AND_LINKS/', '*.csv')):
    workbook = Workbook(csvfile[:-4] + '.xlsx')
    worksheet = workbook.add_worksheet()
    with open(csvfile, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()
print("Converted mdb to excel")
list = []
data = xlrd.open_workbook('C:/Users/brandonh/Desktop/GNET_OBSERVATIONS_AND_LINKS/Current_Obs.xlsx')
table = data.sheets()[0]
for k in range(table.nrows):
    list.append(table.row_values(k))
file = open("C:\\Users\\brandonh\\Desktop\\GNET_OBSERVATIONS_AND_LINKS\\LINKS.xls", 'w')
file1 = open("C:\\Users\\brandonh\\Desktop\\GNET_OBSERVATIONS_AND_LINKS\\LINKS.txt", 'w')
ind = 0
for i in list:
    AssetName = (list[ind][2])
    CollectedOn = (list[ind][8])
    StillImage1 = (list[ind][34])
    StillImage2 = (list[ind][35])
    StillImage3 = (list[ind][36])
    VideoSegment = (list[ind][37])
    ind = int(ind)+1
    file.write(AssetName)
    file.write("\t")
    file.write(VideoSegment)
    file.write("\t")
    file.write(str(CollectedOn))
    file.write("\n")
    file.write(AssetName)
    file.write("\t")
    file.write(StillImage1)
    file.write("\t")
    file.write(str(CollectedOn))
    file.write("\n")
    file.write(AssetName)
    file.write("\t")
    file.write(StillImage2)
    file.write("\t")
    file.write(str(CollectedOn))
    file.write("\n")
    file.write(AssetName)
    file.write("\t")
    file.write(StillImage3)
    file.write("\t")
    file.write(str(CollectedOn))
    file.write("\n")
    file1.write(AssetName)
    file1.write("\t")
    file1.write(VideoSegment)
    file1.write("\t")
    file1.write(str(CollectedOn))
    file1.write("\n")
    file1.write(AssetName)
    file1.write("\t")
    file1.write(StillImage1)
    file1.write("\t")
    file1.write(str(CollectedOn))
    file1.write("\n")
    file1.write(AssetName)
    file1.write("\t")
    file1.write(StillImage2)
    file1.write("\t")
    file1.write(str(CollectedOn))
    file1.write("\n")
    file1.write(AssetName)
    file1.write("\t")
    file1.write(StillImage3)
    file1.write("\t")
    file1.write(str(CollectedOn))
    file1.write("\n")
file1.close()
print("Created file")
file.close()
print("Created file")
input("Go To C:/Users/brandonh/Desktop/GNET_OBSERVATIONS_AND_LINKS/Current_Obs.xlsx and sort by column K\n Delete older stuff and save.")
list = []
data = xlrd.open_workbook("C:\\Users\\brandonh\\Desktop\\GNET_OBSERVATIONS_AND_LINKS\\Current_Obs.xlsx")
table = data.sheets()[0]
for k in range(table.nrows):
    list.append(table.row_values(k))

ind = 0
print("checking to make sure paths exist")
for i in list:
    AssetName = (list[ind][2])
    CollectedOn = (list[ind][8])
    StillImage1 = (list[ind][34])
    StillImage2 = (list[ind][35])
    StillImage3 = (list[ind][36])
    VideoSegment = (list[ind][37])
    ind = int(ind)+1

    if os.path.exists(VideoSegment):
        folderpath = "\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)
        if not os.path.exists(folderpath):
            os.mkdir("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName))
            print("Created Folder")
        path = str(VideoSegment)
        path2 = folderpath + "\\"
        shutil.copy(path, path2)
        print("Copied Media")

    if os.path.exists(StillImage1):
        folderpath = "\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)
        if not os.path.exists(folderpath):
            os.mkdir("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName))
            print("Created Folder")
        path = str(StillImage1)
        path2 = folderpath + "\\"
        shutil.copy(path, path2)
        print("Copied Media")

    if os.path.exists(StillImage2):
        folderpath = "\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)
        if not os.path.exists(folderpath):
            os.mkdir("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName))
            print("Created Folder")
        path = str(StillImage2)
        path2 = folderpath + "\\"
        shutil.copy(path, path2)
        print("Copied Media")

    if os.path.exists(StillImage3):
        folderpath = "\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)
        if not os.path.exists(folderpath):
            os.mkdir("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName))
            print("Created Folder")
        path = str(StillImage3)
        path2 = folderpath + "\\"
        shutil.copy(path, path2)
        print("Copied Media")

print("ALL FINISHED")
