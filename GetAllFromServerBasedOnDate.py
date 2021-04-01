import os


fileobj = open('C:\\Users\\brandonh\\Desktop\\RESULTS.xls','a')
for folder, subfolders, files in os.walk("S:\\AS-BUILT CARDS\\SIDE SEWER CARDS"):
    for file in files:
        filePath = os.path.join(os.path.abspath(folder), file)
        if ".pdf" in filePath:
            fileobj.write(filePath)
            fileobj.write('\t')
            fileobj.write(file)
            fileobj.write("\n")
