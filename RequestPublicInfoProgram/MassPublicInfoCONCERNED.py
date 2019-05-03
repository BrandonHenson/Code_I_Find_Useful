import smtplib
import xlrd
import xlwt
data = xlrd.open_workbook('LIST.xlsx')
table = data.sheets()[0]
list = []
for k in range(table.nrows):
    list.append(table.row_values(k))
fromaddr = 'concernedcitizen.publicinfo@gmail.com'
toaddrs  = list
msg = input('WRITE YOUR MESSAGE HERE')
username = 'concernedcitizen.publicinfo@gmail.com'
password = 'xeourhndoefujlhq'
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
