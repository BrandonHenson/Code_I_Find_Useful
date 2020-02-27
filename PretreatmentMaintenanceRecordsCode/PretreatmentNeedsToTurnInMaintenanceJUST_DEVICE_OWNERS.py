import os
import datetime
from datetime import date

ownerlist = ["H.P. AUTO BATH",
             "KARMICHAEL AUTO SALON",
             "LES SCHWAB",
             "THE SPOT (CARWASH",
             "MUKILTEO SHELL",
             "SMART AUTO SERVICE",
             "A BURGER PLACE",
             "ARNIES RESTAURANT ",
             "CAFÉ SOLEIL",
             "AMICI",
             "HILTON GARDEN INN",
             "IVARS FISH BAR",
             "KAMIAK HIGH SCHOOL",
             "KISS OF THE OCEAN",
             "LOMBARDOS",
             "MONGOLIAN GRILL",
             "MUKILTEO SPEEDWAY CAFE",
             "SAKUMA",
             "SUBWAY",
             "TACO BELL",
             "WHIDBEY COFFEE ",
             "AMBROSIA",
             "AZTECA",
             "BITE OF NEW YORK",
             "BROOKLYN BROTHERS PIZZA",
             "DIAMOND KNOT BREWERY",
             "DIAMOND KNOT BREWING CO",
             "GARLIC JIMS FAMOUS GOURMET PIZZA",
             "GROUCHY CHEF",
             "GYRO STOP",
             "H.P. MIDDLE SCHOOL",
             "H.P. RETIREMENT",
             "HANAMI",
             "HENRYS DONUTS",
             "JOHNS GRILL",
             "KAMIAK HIGH SCHOOL",
             "KINGS TERIYAKI",
             "KOSTAS",
             "LOTUS",
             "MUKILTEO CHOCOLATE CO",
             "MUKILTEO LODGE",
             "MUKILTEO THAI",
             "PATTY'S EGG NEST",
             "PIZZA HUT",
             "RAINBOW WOK & TERIYAKI ",
             "ROSEHILL COMMUNITY CENTER",
             "SABOR A MEXICO ",
             "SHAKE 'N GO",
             "STARBUCKS COFFEE",
             "STAYBRIDGE SUITES",
             "SULLYS",
             "THE SCOTSMAN",
             "THE SYDNEY BAKERY",
             "TRAXX ",
             "WELLERS",
             "ZS BURGER ",
             "MUKILTEO SHELL",
             "KARMICHAEL AUTO SALON ",
             "SUGARCANE"]
today = date.today()
year = int(input("4 digit year"))
month = int(input("1 or 2 digit month"))
day = int(input("1 or 2 digit day"))
datetostartfrom = datetime.datetime(year, month, day, 0, 0).timestamp()
results = open('NeedsMaintenanceRecords.csv', 'a')
list = []
count = 0
for i in os.listdir('S:/Pretreatment/Pretreatment Inspections'):
    x = i.split('_')
    name = x[0]
    # address = x[1]
    if name.upper() in ownerlist:
        list.append(name)
        foldername = 'S:/Pretreatment/Pretreatment Inspections/' + i + '/' + 'MaintenanceRecords'
        if not os.path.exists(foldername):
            os.mkdir(foldername)
        for file in os.listdir(foldername):
            file1 = os.path.join("S:/Pretreatment/Pretreatment Inspections/" + i + '/' + 'MaintenanceRecords/' + file)
            ModTime = os.path.getmtime(file1)
            if int(ModTime) > int(datetostartfrom):
                list.remove(name)
                # print(name)
for i in list:
    results.write(str(i) + '\n')
