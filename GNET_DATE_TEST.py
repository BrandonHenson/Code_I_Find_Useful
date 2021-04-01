import time
import keyboard
import webbrowser
import xlrd
import xlwt
import os



list = []
data = xlrd.open_workbook("TV'd_SewerLines.xlsx")
table = data.sheets()[0]
for k in range(table.nrows):
    list.append(table.row_values(k))

ind = 0
for i in list:
    assetid = (list[ind][0])
    print(assetid)
    ind = ind + 1
