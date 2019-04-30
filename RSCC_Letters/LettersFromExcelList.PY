#coding=utf-8
import xlrd
import xlwt
import time
data = xlrd.open_workbook('LIST.xlsx')
table = data.sheets()[0]
## mm/yyyy format
date = (time.strftime("%m/%d/%Y"))
list = []
for k in range(table.nrows):
    list.append(table.row_values(k))
ind = 0
for i in list:
    name = (list[ind][0])
    address = (list[ind][1])
    parcel = (list[ind][2])
    ind = int(ind)+1
    fileread = open('LetterToOpenAndRead.txt', 'r')
    filename = str(name)+'.doc'
    fileobj = open(filename, 'w')
    fileobj.write(fileread.read().format(date, name, parcel, address))
    fileobj.close()