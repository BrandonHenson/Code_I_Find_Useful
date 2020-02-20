from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename, askdirectory
from xlrd import *
import pandas as pd 
import configparser
import os.path
import os

folder = input('What folder are the files in?')
#folder = 'C:/Users/brandonh/Desktop/ExcelFilesToSplit/'
for file in os.listdir(folder):
    os.mkdir(folder +'/' + file.replace('xlsx',''))

def createConfigfile():
    config = configparser.ConfigParser()
    config['DEFAULTS'] = {'Filename':'',
                            'SaveDirectory':''}
    with open('configuration.ini','w') as configfile:
        config.write(configfile)

def readConfigfile():
    if not os.path.isfile('configuration.ini'):
        createConfigfile()

    config = configparser.ConfigParser()
    config.read('configuration.ini')
    print(config['DEFAULTS']['Filename'])
    localfilename = config['DEFAULTS']['Filename']
    localdirectory = config['DEFAULTS']['SaveDirectory']
    return localfilename, localdirectory

def saveConfigfile():
    localfilename = myfileName.get()
    localdirectoryname = myDirectoryName.get()
    config = configparser.ConfigParser()

    config['DEFAULTS'] = {'Filename':localfilename,
                            'SaveDirectory':localdirectoryname}
    with open('configuration.ini','w') as configfile:
        config.write(configfile)

def selectFile():
    try:
        value = askopenfilename()
        myfileName.set(value)
    except ValueError:
        pass

def selectFileDirectory():
    try:
        value = askdirectory()
        myDirectoryName.set(value)
    except ValueError:
        pass        

def splitExcelFile():
    inputfile = myfileName.get()     
    xl = open_workbook(inputfile)    
    mysheetnames = xl.sheet_names()
    path = myDirectoryName.get()+'/'

    for name in mysheetnames:
        writer = pd.ExcelWriter(path+name+'.xlsx')
        parsing = pd.ExcelFile(inputfile).parse(sheet_name=name)
        parsing.to_excel(writer,name)
        writer.save()
    saveConfigfile()
    messagebox.showinfo("Split successfully", "File was split.")


root = Tk()
root.title("Brandon's Excel Splitter")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
myfileName = StringVar()
myDirectoryName = StringVar()
tempfileName, tempdirectory = readConfigfile()
myfileName.set(tempfileName)
myDirectoryName.set(tempdirectory)
ttk.Label(mainframe,text="Filename").grid(column=1, row=1,sticky=(W))
fileName_entry = ttk.Entry(mainframe, width = 20, textvariable = myfileName)
fileName_entry.grid(column=2, row=1,sticky=(W,E))
ttk.Button(mainframe, text="Choose a file", command=selectFile).grid(column=3, row=1, sticky=W)
ttk.Label(mainframe,text="Outputdirectory").grid(column=1, row=2,sticky=(E))
fileName_entry = ttk.Entry(mainframe, width = 20, textvariable = myDirectoryName)
fileName_entry.grid(column=2, row=2,sticky=(W,E))
ttk.Button(mainframe, text="Select directory", command=selectFileDirectory).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="BY PRESSING THIS, I ACKNOWLEDGE BRANDON IS THE MAN.", command=splitExcelFile).grid(column=1,columnspan=3,row=3, sticky=(E,W))
root.mainloop()

