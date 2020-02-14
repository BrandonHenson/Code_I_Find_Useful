import os
import keyboard
import time
import webbrowser


folder = input('folder with excels in it?')
ind = 0
for i in os.listdir(folder.replace('\\','//')):
	print("opening " + i)
	webbrowser.open(folder + '//' + i)
	time.sleep(5)
	keyboard.press_and_release('alt + l')
	time.sleep(.25)
	keyboard.press_and_release('v')
	time.sleep(.25)
	keyboard.press_and_release('alt')
	time.sleep(.25)
	keyboard.press_and_release('i')
	time.sleep(.25)
	keyboard.press_and_release('m')
	time.sleep(.5)
	keyboard.write("Sub CopyWestgateValuesToNewSheet()\n")
	keyboard.write('Sheets("Westgate FCV").Select\n')
	keyboard.write('Cells.Select\n')
	keyboard.write('Selection.Copy\n')
	keyboard.write('Workbooks.Add\n')
	keyboard.write('Range("A1").Select\n')
	keyboard.write('ActiveSheet.Paste\n')
	keyboard.write('Cells.Select\n')
	keyboard.write('Application.CutCopyMode = False\n')
	keyboard.write('Selection.Copy\n')
	keyboard.write('Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _\n')
	keyboard.write(':=False, Transpose:=False\n')
	keyboard.write('Application.CutCopyMode = False\n')
	keyboard.write('ChDir "C:\\Users\\brandonh\\Desktop"\n')
	keyboard.write('ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\Westgate.xlsx", _\n')
	keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
	keyboard.press_and_release('f5')
	time.sleep(35)
	os.system("taskkill /f /im EXCEL.EXE")
	time.sleep(5)
	os.rename("C:/Users/brandonh/Desktop/Westgate.xlsx", "C:/Users/brandonh/Desktop/Westgate_" + str(ind) +".xlsx")
	ind = ind + 1
