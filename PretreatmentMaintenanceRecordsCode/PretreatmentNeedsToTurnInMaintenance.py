import os
import datetime
from datetime import date


today = date.today()
year = int(input("4 digit year"))
month = int(input("1 or 2 digit month"))
day = int(input("1 or 2 digit day"))
datetostartfrom = datetime.datetime(year,month,day,0,0).timestamp()
results = open('NeedsMaintenanceRecords.csv','a')
list = []
count = 0
for i in os.listdir('S:/Pretreatment/Pretreatment Inspections'):
    x = i.split('_')
    name = x[0]
    address = x[1]
    list.append(name)
    foldername = 'S:/Pretreatment/Pretreatment Inspections/' + i + '/' + 'MaintenanceRecords'
    for file in os.listdir(foldername):
        file1 = os.path.join("S:/Pretreatment/Pretreatment Inspections/" +  i + '/' + 'MaintenanceRecords/' +file )
        ModTime = os.path.getmtime(file1)
        if int(ModTime) > int(datetostartfrom):
            list.remove(name)
            #print(name)
for i in list:
    results.write(str(i) + '\n')
