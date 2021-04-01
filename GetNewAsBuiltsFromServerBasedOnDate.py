import datetime
import os

fileobj = open("C:\\Users\\brandonh\\Desktop\\RESULTS.xls",'a')
year = int(input("4 digit year"))
month = int(input("1 or 2 digit month"))
day = int(input("1 or 2 digit day"))
datetostartfrom = datetime.datetime(year, month, day, 0, 0).timestamp()
count = 0
for i in os.listdir('S:/AS-BUILT CARDS/SIDE SEWER CARDS/'):
    if 'Thumbs' not in i:
        if 'xlsx' not in i:
            foldername = 'S:/AS-BUILT CARDS/SIDE SEWER CARDS/' + i + '/'
            for file in os.listdir(foldername):
                file1 = os.path.join("S:/AS-BUILT CARDS/SIDE SEWER CARDS/" + i + '/' + file)
                ModTime = os.path.getmtime(file1)
                if int(ModTime) > int(datetostartfrom):
                    fileobj.write(file1.replace('/', '\\'))
                    fileobj.write("\n")