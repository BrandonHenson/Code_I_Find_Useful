import os
import datetime
from datetime import date


today = date.today()
year = int(input("4 digit year"))
month = int(input("1 or 2 digit month"))
day = int(input("1 or 2 digit day"))
datetostartfrom = datetime.datetime(year,month,day,0,0).timestamp()

filelist = open(str(os.getcwd())+'/SubmittedPretreatmentMaintenanceRecords.csv', 'a')
count = 0
for i in os.listdir('S:/Pretreatment/Pretreatment Inspections'):
    foldername = 'S:/Pretreatment/Pretreatment Inspections/' + i + '/' + 'MaintenanceRecords'
    for file in os.listdir(foldername):
        file1 = os.path.join("S:/Pretreatment/Pretreatment Inspections/" +  i + '/' + 'MaintenanceRecords/' +file )
        ModTime = os.path.getmtime(file1)
        if int(ModTime) > int(datetostartfrom):
            filelist.writelines(str(file1))
            filelist.writelines('\n')
            count = count + 1
filelist.writelines(str(count) + ' files')
