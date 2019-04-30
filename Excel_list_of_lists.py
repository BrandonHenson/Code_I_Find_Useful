#coding=utf-8
import xlrd
import xlwt
# CREATE A FILE IN THE SAME DIRECTORY NAMED LIST.xlsx
data = xlrd.open_workbook('LIST.xlsx')
table = data.sheets()[0] #table
#print(table.nrows) #number of rows
#print(table.ncols) #number of columns
list = []
for k in range(table.nrows):
    print(table.row_values(k))
print(list)
'''
'''
'''
for i in range(table.ncols):
    print(table.col_values(i))
'''
'''
print(table.cell(2,2).value)
'''
'''
for a in range(1,table.nrows):
    for b in range(table.ncols):
        print(table.cell(a,b).value)
    print('-------')
'''