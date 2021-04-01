import os
path = '\\\\mukgis\\GIS Files'
lockfiles = open('LOCKFILES.txt','a')
list = []
for folder, subfolders, files in os.walk(path):
    for file in files:
        if 'sr.lock' in file:
            workstation = file.split('.')[1].lstrip().split(' ')[0]
            if 'WKS' in workstation:
                if workstation not in list:
                    list.append(workstation)
'''
for i in list:
    if '70' in i:
        lockfiles.write("My Computer has lock files.")
        lockfiles.write('\n')
    elif '58'in i:
        lockfiles.write("Morgan's Computer has lock files.")
        lockfiles.write('\n')
    elif '56'in i:
        lockfiles.write("Roan's Computer has lock files.")
        lockfiles.write('\n')
    elif '68'in i:
        lockfiles.write("JJ's Computer has lock files.")
        lockfiles.write('\n')
    elif '54' in i:
        lockfiles.write("Eric's Computer has lock files.")
        lockfiles.write('\n')
    elif '67'in i:
        lockfiles.write("Brian's Computer has lock files.")
        lockfiles.write('\n')
    elif '69'in i:
        lockfiles.write("Rick's Computer has lock files.")
        lockfiles.write('\n')
    elif '57'in i:
        lockfiles.write("Jared's Computer has lock files.")
        lockfiles.write('\n')
    elif '61'in i:
        lockfiles.write("Briley's Computer has lock files.")
        lockfiles.write('\n')
'''
for i in list:
    if '70' in i:
        print("My GIS is Open.")

    elif '58'in i:
        print("Morgan's GIS is Open.")

    elif '56'in i:
        print("Roan's GIS is Open.")

    elif '68'in i:
        print("JJ's GIS is Open.")

    elif '54' in i:
        print("Eric's GIS is Open.")

    elif '67'in i:
        print("Brian's GIS is Open.")

    elif '69'in i:
        print("Rick's GIS is Open.")

    elif '57'in i:
        print("Jared's GIS is Open.")

    elif '61'in i:
        print("Briley's GIS is Open.")
print('DONE')
input()