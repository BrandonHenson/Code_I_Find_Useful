import shutil
import os
import xlrd
import csv
import pyodbc
import glob
from xlsxwriter.workbook import Workbook


DESKTOPPATH = "C:\\Users\\brandonh\\Desktop\\GNET_OBSERVATIONS_AND_LINKS\\"
if not os.path.exists(DESKTOPPATH):
    os.mkdir(DESKTOPPATH)
    print("Created Folder")
shutil.copy("\\\\mukgis\\GIS Files\\GNET\\GNetObservation.mdb", DESKTOPPATH)
print("Copied \\\\mukgis\\GIS Files\\GNET\\GNetObservation.mdb to folder")

MDB = 'C:/Users/brandonh/Desktop/GNET_OBSERVATIONS_AND_LINKS/GNetObservation.mdb'
DRV = '{Microsoft Access Driver (*.mdb)}'
PWD = 'pw'


con = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()


SQL = 'SELECT * FROM GNet_WwMainlineObservation;'
rows = cur.execute(SQL).fetchall()
cur.close()
con.close()

with open('C:/Users/brandonh/Desktop/GNET_OBSERVATIONS_AND_LINKS/GNet_WwMainlineObservation.csv' , 'w') as fou:
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
data = xlrd.open_workbook("C:\\Users\\brandonh\\Desktop\\GNET_OBSERVATIONS_AND_LINKS\\GNet_WwMainlineObservation.xlsx")
table = data.sheets()[0]
tableodds = 1
for k in range(table.nrows):
	tableodds = int(tableodds) + 1
	if int(tableodds) % 2 == 0:
		list.append(table.row_values(k))

ind = 0
for i in list:
	Newfiles = 0
	Newfolders = 0
	AssetName = str((list[ind][2]))
	CollectedOn = str((list[ind][8]))
	StillImage1 = str((list[ind][34]))
	StillImage2 = str((list[ind][35]))
	StillImage3 = str((list[ind][36]))
	VideoSegment = str((list[ind][37]))
	ind = int(ind)+1
	folderpath = "\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)
	if not os.path.exists(folderpath):
		os.mkdir("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName))
		Newfolders = Newfolders + 1

	if os.path.exists(StillImage1):
		if not os.path.exists(StillImage1.replace('\\\\MUKNAS01\\Videos\\Photos\\',("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)+"\\"))):
			shutil.copy(StillImage1,StillImage1.replace('\\\\MUKNAS01\\Videos\\Photos\\',("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)+"\\")))
			print('Copied Picture')
			Newfiles = Newfiles + 1
		else:
			print('Already There (Image1)')
	if os.path.exists(StillImage2):
		if not os.path.exists(StillImage2.replace('\\\\MUKNAS01\\Videos\\Photos\\',("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)+"\\"))):
			shutil.copy(StillImage2,StillImage2.replace('\\\\MUKNAS01\\Videos\\Photos\\',("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)+"\\")))
			print('Copied Picture')
			Newfiles = Newfiles + 1
		else:
			print('Already There (Image2)')
	if os.path.exists(StillImage3):
		if not os.path.exists(StillImage3.replace('\\\\MUKNAS01\\Videos\\Photos\\',("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)+"\\"))):
			shutil.copy(StillImage3,StillImage3.replace('\\\\MUKNAS01\\Videos\\Photos\\',("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)+"\\")))
			print('Copied Picture')
			Newfiles = Newfiles + 1
		else:
			print('Already There (Image3)')

	if os.path.exists(VideoSegment):
		if not os.path.exists(VideoSegment.replace('\\\\MUKNAS01\\Videos\\Video\\',("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)+"\\"))):
			shutil.copy(VideoSegment,VideoSegment.replace('\\\\MUKNAS01\\Videos\\Video\\',("\\\\mukgis\\GIS Files\\GNET\\GNET_FOLDERS_VIDS_PICS\\" + str(AssetName)+"\\")))
			print('Copied Video')
			Newfiles = Newfiles + 1
		else:
			print('Already There (Video)')

print(str(Newfiles) + ' New Files Copied')
print(str(Newfolders) + ' New Folders Copied')
