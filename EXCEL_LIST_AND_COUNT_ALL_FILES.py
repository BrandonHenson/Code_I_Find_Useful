import os
dirs = os.listdir(os.getcwd())
filelist = open(str(os.getcwd())+'/FILES.xls', 'a')
count = 1
for files in dirs:
    filelist.writelines(str(files))
    filelist.writelines('\n')
    count = count + 1
filelist.writelines(str(count)+' files')
