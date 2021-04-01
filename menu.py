import datetime
import time
import keyboard
import webbrowser
import os
import shutil
import getpass
import zipfile


def county():
    dir_name = 'C:/Users/brandonh/Downloads'
    extension = ".zip"
    os.chdir(dir_name)
    for item in os.listdir(dir_name):
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            os.remove(file_name)


    webbrowser.open('ftp://ftp.snoco.org/Assessor/shapefiles/lots.zip')
    webbrowser.open('ftp://ftp.snoco.org/assessor/shapefiles/muni_annexations.zip')
    webbrowser.open('ftp://ftp.snoco.org/Assessor/shapefiles/allparcels.zip')
    webbrowser.open('ftp://ftp.snoco.org/assessor/shapefiles/plss.zip')
    webbrowser.open('ftp://ftp.snoco.org/assessor/shapefiles/rows.zip')
    webbrowser.open('ftp://ftp.snoco.org/Assessor/shapefiles/parcelcent.zip')
    webbrowser.open('ftp://ftp.snoco.org/Assessor/shapefiles/parcels.zip')
    time.sleep(55)
    dir_name = 'C:/Users/brandonh/Downloads'
    extension = ".zip"
    os.chdir(dir_name)
    for item in os.listdir(dir_name):
        if item.endswith(extension):
            file_name = os.path.abspath(item)
            zip_ref = zipfile.ZipFile(file_name)
            zip_ref.extractall('//mukgis/GIS Files/Geodatabase/Snohomish County Updated')
            zip_ref.close()
            os.remove(file_name)


def graph():
    os.mkdir('C:/Users/brandonh/Desktop/DAILYSFORGRAPH')
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/112TH.xlsx",
                "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/112TH.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/Cathodic_Protection.xlsx",
                "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/Cathodic_Protection.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/CONFINED_SPACE_PERMIT.xlsx",
                "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/CONFINED_SPACE_PERMIT.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/FIRE_PUMPS.xlsx",
                "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/FIRE_PUMPS.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/GENERATORS.xlsx",
                "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/GENERATORS.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/HOLLY.xlsx",
                "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/HOLLY.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/LS10.xlsx", "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS10.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/LS11.xlsx", "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS11.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/LS12.xlsx", "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS12.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/LS13.xlsx", "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS13.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/LS14.xlsx", "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS14.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/LS2.xlsx", "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS2.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/LS5.xlsx", "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS5.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/LS8.xlsx", "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS8.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/LS9.xlsx", "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS9.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/NONPERMIT_CONFINED.xlsx",
                "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/NONPERMIT_CONFINED.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/PFDAILY.xlsx",
                "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/PFDAILY.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/RES2_TRANSFER_PUMP.xlsx",
                "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/RES2_TRANSFER_PUMP.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/RESERVOIR_INSPECTIONS.xlsx",
                "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/RESERVOIR_INSPECTIONS.xlsx")
    shutil.copy("//mukgis/GIS Files/Daily's/Dailys2020/S7.xlsx", "C:/Users/brandonh/Desktop/DAILYSFORGRAPH/S7.xlsx")

    # LS5
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS5.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("sub LS5()\n")
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "P1"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "P2"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Range("C:C,N:N").Select\n')
    keyboard.write('Range("N1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$N:$N")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,P:P").Select\n')
    keyboard.write('Range("P1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$P:$P")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,O:O").Select\n')
    keyboard.write('Range("O1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$O:$O")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_LS5.xlsx", _\n')
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # 112TH
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/112TH.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub Graph()\n")
    keyboard.write('\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Axes(xlCategory).Select\n')
    keyboard.write('Range("F20").Select\n')
    keyboard.write('ActiveSheet.ChartObjects("Chart 1").Activate\n')
    keyboard.write('ActiveSheet.ChartObjects("Chart 1").Activate\n')
    keyboard.write('ActiveSheet.ChartObjects("Chart 1").Activate\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "P1 Amps Graph"\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("metadata_1").Select\n')
    keyboard.write('ActiveWindow.SelectedSheets.Visible = False\n')
    keyboard.write('Sheets("P1 Amps Graph").Select\n')
    keyboard.write('Sheets("P1 Amps Graph").Name = "P1 Graph"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('Range("C:C,T:T").Select\n')
    keyboard.write('Range("T1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$T:$T")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1 Graph").Select\n')
    keyboard.write('ActiveChart.Paste\n')
    keyboard.write('ActiveSheet.ChartObjects("Chart 1").Activate\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("H18").Select\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "P2 Graph"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 1\n')
    keyboard.write('Range("C:C,R:R").Select\n')
    keyboard.write('Range("R1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$R:$R")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2 Graph").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('Range("C:C,U:U").Select\n')
    keyboard.write('Range("U1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$U:$U")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2 Graph").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("H19").Select\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet3").Select\n')
    keyboard.write('Sheets("Sheet3").Name = "P3 Graph"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("G:G,S:S").Select\n')
    keyboard.write('Range("S1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$G:$G,surveyPoint_0!$S:$S")\n')
    keyboard.write('ActiveChart.ChartArea.Copy\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P3 Graph").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("G:G,V:V").Select\n')
    keyboard.write('Range("V1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$G:$G,surveyPoint_0!$V:$V")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P3 Graph").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I19").Select\n')
    keyboard.write('Sheets("P1 Graph").Select\n')
    time.sleep(.25)
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_LS112TH.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # HOLLY
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/HOLLY.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub Macro18()\n")
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "P1"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "P2"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Range("C:C,N:N").Select\n')
    keyboard.write('Range("N1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$N:$N")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,P:P").Select\n')
    keyboard.write('Range("P1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$P:$P")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,O:O").Select\n')
    keyboard.write('Range("O1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$O:$O")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("P1").Select\n')
    time.sleep(.25)
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_HOLLY.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # LS2
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS2.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub Macro16()\n")
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "P1"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "P2"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Range("C:C,N:N").Select\n')
    keyboard.write('Range("N1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$N:$N")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,P:P").Select\n')
    keyboard.write('Range("P1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$P:$P")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,O:O").Select\n')
    keyboard.write('Range("O1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$O:$O")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("P1").Select\n')
    time.sleep(.25)
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_LS2.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # LS8
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS8.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub Macro14()\n")
    keyboard.write('\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "AMPS"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "FLOW"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Range("C:C,P:P").Select\n')
    keyboard.write('Range("P1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$P:$P")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("AMPS").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("AMPS").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("A17").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,R:R").Select\n')
    keyboard.write('Range("R1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$R:$R")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("AMPS").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I17").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,S:S").Select\n')
    keyboard.write('Range("S1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$S:$S")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("AMPS").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('Range("C:C,T:T").Select\n')
    keyboard.write('Range("T1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(240, xlXYScatterLines).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$T:$T")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("FLOW").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 1\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('ActiveWindow.ScrollColumn = 11\n')
    keyboard.write('ActiveWindow.ScrollColumn = 12\n')
    keyboard.write('ActiveWindow.ScrollColumn = 13\n')
    keyboard.write('ActiveWindow.ScrollColumn = 14\n')
    keyboard.write('ActiveWindow.ScrollColumn = 15\n')
    keyboard.write('ActiveWindow.ScrollColumn = 16\n')
    keyboard.write('Range("C:C,U:U").Select\n')
    keyboard.write('Range("U1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(240, xlXYScatterLines).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$U:$U")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("FLOW").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("AMPS").Select\n')
    time.sleep(.25)
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_LS8.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # LS9
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS9.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub Macro13()\n")
    keyboard.write('\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "Amps"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "Flow"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Range("C:C,P:P").Select\n')
    keyboard.write('Range("P1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$P:$P")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("Amps").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("Amps").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("A17").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,R:R").Select\n')
    keyboard.write('Range("R1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$R:$R")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("Amps").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,S:S").Select\n')
    keyboard.write('Range("S1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$S:$S")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("Amps").Select\n')
    keyboard.write('Range("I17").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('Range("C:C,T:T").Select\n')
    keyboard.write('Range("T1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$T:$T")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("Flow").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 1\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('Range("C:C,U:U").Select\n')
    keyboard.write('Range("U1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$U:$U")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("Flow").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("Amps").Select\n')
    time.sleep(.25)
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_LS9.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # LS10
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS10.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub Macro11()\n")
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "Pump Amps"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "GPM"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Range("C:C,P:P").Select\n')
    keyboard.write('Range("P1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$P:$P")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("Pump Amps").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("Pump Amps").Select\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,R:R").Select\n')
    keyboard.write('Range("R1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$R:$R")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("Pump Amps").Select\n')
    keyboard.write('Range("A17").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,S:S").Select\n')
    keyboard.write('Range("S1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$S:$S")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("Pump Amps").Select\n')
    keyboard.write('Range("I17").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('ActiveWindow.SmallScroll Down:=0\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('Range("C:C,T:T").Select\n')
    keyboard.write('Range("T1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$T:$T")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("GPM").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 1\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('ActiveWindow.ScrollColumn = 11\n')
    keyboard.write('ActiveWindow.ScrollColumn = 12\n')
    keyboard.write('ActiveWindow.ScrollColumn = 13\n')
    keyboard.write('ActiveWindow.ScrollColumn = 14\n')
    keyboard.write('ActiveWindow.ScrollColumn = 15\n')
    keyboard.write('ActiveWindow.ScrollColumn = 16\n')
    keyboard.write('ActiveWindow.ScrollColumn = 17\n')
    keyboard.write('Range("C:C,U:U").Select\n')
    keyboard.write('Range("U1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$U:$U")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("GPM").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("U17").Select\n')
    keyboard.write('Sheets("Pump Amps").Select\n')
    time.sleep(.25)
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_LS10.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # LS11
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS11.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub Macro8()\n")
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "P1"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "P2"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,N:N").Select\n')
    keyboard.write('Range("N1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$N:$N")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Range("C21").Select\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('ActiveWindow.ScrollColumn = 11\n')
    keyboard.write('Range("C:C,P:P").Select\n')
    keyboard.write('Range("P1").Activate\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 1\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(240, xlXYScatterLines).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$P:$P")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,O:O").Select\n')
    keyboard.write('Range("O1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$O:$O")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(240, xlXYScatterLines).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("P1").Select\n')
    time.sleep(.25)
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_LS11.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # LS12
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS12.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub Macro9()\n")
    keyboard.write('\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "P1"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "P2"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Range("C:C,N:N").Select\n')
    keyboard.write('Range("N1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$N:$N")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,P:P").Select\n')
    keyboard.write('Range("P1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$P:$P")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,O:O").Select\n')
    keyboard.write('Range("O1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$O:$O")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("P1").Select\n')
    time.sleep(.25)
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_LS12.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # LS13

    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/LS13.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub graph()\n")
    keyboard.write('\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "P1"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "P2"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,N:N").Select\n')
    keyboard.write('Range("N1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$N:$N")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,P:P").Select\n')
    keyboard.write('Range("P1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$P:$P")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,O:O").Select\n')
    keyboard.write('Range("O1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$O:$O")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("P1").Select\n')
    time.sleep(.25)
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_LS13.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # PF
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/PFDAILY.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub graph()\n")
    keyboard.write('\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Columns("J:J").EntireColumn.AutoFit\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "P1"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "P2"\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,J:J").Select\n')
    keyboard.write('Range("J1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$J:$J")\n')
    keyboard.write('ActiveChart.Axes(xlValue).MajorGridlines.Select\n')
    keyboard.write('ActiveChart.ChartArea.Select\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,L:L").Select\n')
    keyboard.write('Range("L1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$L:$L")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("Q1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,N:N").Select\n')
    keyboard.write('Range("N1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$N:$N")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('ActiveWindow.ScrollColumn = 11\n')
    keyboard.write('ActiveWindow.ScrollColumn = 12\n')
    keyboard.write('ActiveWindow.ScrollColumn = 13\n')
    keyboard.write('ActiveWindow.ScrollColumn = 14\n')
    keyboard.write('Range("C:C,V:V").Select\n')
    keyboard.write('Range("V1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$V:$V")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('Range("A17").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('ActiveSheet.ChartObjects("Chart 3").Activate\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Range("I17").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('ActiveWindow.SmallScroll Down:=-3\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 13\n')
    keyboard.write('ActiveWindow.ScrollColumn = 12\n')
    keyboard.write('ActiveWindow.ScrollColumn = 11\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 1\n')
    keyboard.write('Range("C:C,K:K").Select\n')
    keyboard.write('Range("K1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$K:$K")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,M:M").Select\n')
    keyboard.write('Range("M1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$M:$M")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("A17").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Columns("N:N").ColumnWidth = 12.82\n')
    keyboard.write('Range("C:C,O:O").Select\n')
    keyboard.write('Range("O1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$O:$O")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("I17").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('Range("C:C,W:W").Select\n')
    keyboard.write('Range("W1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$W:$W")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('ActiveWindow.SmallScroll Down:=3\n')
    keyboard.write('Sheets("P1").Select\n')
    time.sleep(.25)
    keyboard.write(
        'ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_PFDAILY.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)

    # S7
    webbrowser.open('C:/Users/brandonh/Desktop/DAILYSFORGRAPH/S7.xlsx')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('l')
    time.sleep(.25)
    keyboard.press_and_release('v')
    time.sleep(.25)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('i')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.write("Sub graph()\n")
    keyboard.write('\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('Selection.NumberFormat = "m/d/yyyy"\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets.Add After:=ActiveSheet\n')
    keyboard.write('Sheets("Sheet1").Select\n')
    keyboard.write('Sheets("Sheet1").Name = "P1"\n')
    keyboard.write('Sheets("Sheet2").Select\n')
    keyboard.write('Sheets("Sheet2").Name = "P2"\n')
    keyboard.write('Sheets("Sheet3").Select\n')
    keyboard.write('Sheets("Sheet3").Name = "P3"\n')
    keyboard.write('Range("E13").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Range("C:C,Q:Q").Select\n')
    keyboard.write('Range("Q1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$Q:$Q")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('Range("C:C,T:T").Select\n')
    keyboard.write('Range("T1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$T:$T")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P1").Select\n')
    keyboard.write('Range("I1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 1\n')
    keyboard.write('Range("C:C,R:R").Select\n')
    keyboard.write('Range("R1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$R:$R")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('Range("C:C,U:U").Select\n')
    keyboard.write('Range("U1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$U:$U")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P2").Select\n')
    keyboard.write('Range("J1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 1\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('Range("C:C,S:S").Select\n')
    keyboard.write('Range("S1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(276, xlAreaStacked).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$S:$S")\n')
    keyboard.write('ActiveChart.FullSeriesCollection(1).Select\n')
    keyboard.write('ActiveChart.ChartArea.Select\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P3").Select\n')
    keyboard.write('Range("A1").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Range("J1").Select\n')
    keyboard.write('Sheets("surveyPoint_0").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 1\n')
    keyboard.write('Columns("C:C").Select\n')
    keyboard.write('ActiveWindow.ScrollColumn = 2\n')
    keyboard.write('ActiveWindow.ScrollColumn = 3\n')
    keyboard.write('ActiveWindow.ScrollColumn = 4\n')
    keyboard.write('ActiveWindow.ScrollColumn = 5\n')
    keyboard.write('ActiveWindow.ScrollColumn = 6\n')
    keyboard.write('ActiveWindow.ScrollColumn = 7\n')
    keyboard.write('ActiveWindow.ScrollColumn = 8\n')
    keyboard.write('ActiveWindow.ScrollColumn = 9\n')
    keyboard.write('ActiveWindow.ScrollColumn = 10\n')
    keyboard.write('Range("C:C,V:V").Select\n')
    keyboard.write('Range("V1").Activate\n')
    keyboard.write('ActiveSheet.Shapes.AddChart2(227, xlLineMarkers).Select\n')
    keyboard.write('ActiveChart.SetSourceData Source:=Range( _\n')
    keyboard.write('"surveyPoint_0!$C:$C,surveyPoint_0!$V:$V")\n')
    keyboard.write('ActiveChart.Parent.Cut\n')
    keyboard.write('Sheets("P3").Select\n')
    keyboard.write('ActiveSheet.Paste\n')
    keyboard.write('Sheets("P1").Select\n')
    time.sleep(.25)
    keyboard.write('ActiveWorkbook.SaveAs Filename:="C:\\Users\\brandonh\\Desktop\\DAILYSFORGRAPH\\Graph_S7.xlsx", _\n')
    time.sleep(.25)
    keyboard.write('FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False\n')
    time.sleep(.5)
    keyboard.press_and_release('f5')
    time.sleep(3)
    keyboard.press_and_release('enter')
    time.sleep(3)
    os.system("taskkill /f /im EXCEL.EXE")
    time.sleep(2)


def locates():
    today = (time.strftime("%m_%d_%Y"))
    user = getpass.getuser()
    strpath = str('C:/Users/' + user + '/Desktop/MapLink' + today)
    os.mkdir(strpath)
    path = strpath
    serverpath = "S:/LOCATES/"
    server = os.listdir("S:/LOCATES")
    servdirs = os.listdir(path)
    for item in server:
        if '.doc' in item and '~' not in item:
            source = serverpath + str(item)
            destination = path + '/' + str(item) + '.txt'
            shutil.copy(source, destination)
    dirs = os.listdir(path)
    list1 = []
    for file in dirs:
        file = path + '/' + str(file)
        with open(file, 'r') as f:
            LIST = []
            for line in f:
                if "Link To Map for MUKWA01:" in line:
                    ind = (line.index("MUKWA01: "))
                    ind1 = ind + 9
                    line1 = line[ind1:]
                    Type = line1
                    LIST.append(Type)
                    webbrowser.open(line1)


def menu_selection(prompt, dispatch_dict):
    while True:
        response = input(prompt)
        try:
            if dispatch_dict[response]() == "Exit Menu":
                break
        except KeyError:
            print("\nPick from the listed options.")


prompt = ('\nSelect an option:\n'
          '[1] UPDATE DAILY GENERATORS AND STATIONS\n'
          '[2] UPDATE GNET MEDIA FROM MUKNAS01 TO MUKGIS\n'
          '[3] BACKUP GIS FILES\n'
          '[4] FIND OUT WHAT HAS BEEN INSPECTED\n'
          '[5] LOCATES\n'
          '[6] GRAPH\n'
          '[7] UPDATE COUNTY LAYERS\n'
          '[8] Exit\n')


def exit():
    return "Exit Menu"

'''
def inspected():
    filecsv = open("C:/Users/brandonh/Desktop/TV'd_SewerLines.csv", "a")
    list = []
    for folder, subfolders, files in os.walk("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS"):
        for file in files:
            folder = folder.replace("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS\\", "")
            filePath = os.path.join(os.path.abspath(folder), file)
            if folder in list:
                pass
            else:
                list.append(folder)
    filecsv.write("CodeToPasteInGIS_SelectFrom" + "\n")
    for i in list:
        filecsv.write("Mains_Gravity.Asset_ID = '" + i + "' OR" + "\n")
    filecsv.write('\n\nIGNORE \nColson 01\nGM0230\nGmbh51\nGMO580RD\nGM_BH_27')
'''

def inspected():
    import os
    import keyboard
    import time
    import xlrd
    newtvdlist = []
    listofalreadydone = []
    keyboard.press_and_release('cmd')
    time.sleep(.25)
    keyboard.write("\\\\MUKGIS\\GIS Files\\Maps\\TV'D.mxd")
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(15)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('g')
    time.sleep(.25)
    keyboard.press_and_release('enter')
    time.sleep(2)
    keyboard.press_and_release('p')
    time.sleep(3)
    keyboard.write(
        'arcpy.TableToExcel_conversion(Input_Table="TV_D_AT_SOME_POINT", Output_Excel_File="C:/Users/brandonh/Desktop/tv_d.xls", Use_field_alias_as_column_header="NAME", Use_domain_and_subtype_description="CODE")')
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(10)
    os.system("taskkill /f /im ArcMap.exe")
    time.sleep(2)
    keyboard.press_and_release('cmd')
    time.sleep(.5)
    keyboard.write("C:\\Users\\brandonh\\Desktop\\tv_d.xls")
    time.sleep(2)
    keyboard.press_and_release('enter')
    time.sleep(2)
    keyboard.press_and_release('enter')
    time.sleep(5)
    keyboard.press_and_release('alt')
    time.sleep(1.5)
    keyboard.press_and_release('f')
    time.sleep(1.5)
    keyboard.press_and_release('a')
    time.sleep(1.5)
    keyboard.press_and_release('1')
    time.sleep(1.5)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('down')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('enter')
    time.sleep(.25)
    keyboard.press_and_release('enter')
    time.sleep(2)
    os.system("taskkill /f /im EXCEL.EXE")

    list1 = []
    data = xlrd.open_workbook("C:\\Users\\brandonh\\Desktop\\tv_d.xlsx")
    table = data.sheets()[0]
    for k in range(table.nrows):
        list1.append(table.row_values(k))
    ind = 0
    for i in list1:
        assetid = (list1[ind][8])
        listofalreadydone.append(str(assetid))
        ind = ind + 1

    filecsv = open("C:/Users/brandonh/Desktop/TV'd_SewerLines.csv", "a")
    list = []
    for folder, subfolders, files in os.walk("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS"):
        for file in files:
            folder = folder.replace("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS\\", "")
            filePath = os.path.join(os.path.abspath(folder), file)
            if folder in list:
                pass
            else:
                list.append(folder)
    for i in list:
        filecsv.write(i + "\n")
    # filecsv.write('\n\nIGNORE \nColson 01\nGM0230\nGmbh51\nGMO580RD\nGM_BH_27')
    filecsv.close()
    time.sleep(1)
    keyboard.press_and_release('cmd')
    time.sleep(.25)
    keyboard.write("C:\\Users\\brandonh\\Desktop\\TV'd_SewerLines.csv")
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(2)
    keyboard.press_and_release('alt')
    time.sleep(.5)
    keyboard.press_and_release('f')
    time.sleep(.5)
    keyboard.press_and_release('a')
    time.sleep(.5)
    keyboard.press_and_release('1')
    time.sleep(.5)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('down')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('up')
    time.sleep(.25)
    keyboard.press_and_release('enter')
    time.sleep(.25)
    keyboard.press_and_release('enter')
    time.sleep(2)
    os.system("taskkill /f /im EXCEL.EXE")

    list = []
    data = xlrd.open_workbook("C:\\Users\\brandonh\\Desktop\\TV'd_SewerLines.xlsx")
    table = data.sheets()[0]
    for k in range(table.nrows):
        if table.row_values(k) not in list:
            list.append(table.row_values(k))
    ind = 0
    for i in list:
        assetid = (list[ind][0])
        newtvdlist.append(str(assetid))
        # print(str(assetid))
        ind = ind + 1

    keyboard.press_and_release('cmd')
    time.sleep(.25)
    keyboard.write("\\\\MUKGIS\\GIS Files\\Maps\\TV'D.mxd")
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(15)
    keyboard.press_and_release('alt')
    time.sleep(.25)
    keyboard.press_and_release('s')
    time.sleep(.25)
    keyboard.press_and_release('a')
    time.sleep(.25)
    keyboard.press_and_release('m')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)
    keyboard.press_and_release('tab')
    time.sleep(.25)

    for i in newtvdlist:
        if i not in listofalreadydone:
            if "\\" not in i:
                if ".0" not in i:
                    keyboard.write("Asset_ID ='")
                    time.sleep(.25)
                    keyboard.write(i)
                    keyboard.write("'OR\n")







def daily():
    # http://survey123.arcgis.com/surveys
    webbrowser.open('http://survey123.arcgis.com/surveys')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(2)
    keyboard.press_and_release('tab')
    time.sleep(2)
    keyboard.press_and_release('enter')
    time.sleep(2)
    list = ['http://survey123.arcgis.com/surveys/0aea9858723047d890880287de41739f/data',
            'http://survey123.arcgis.com/surveys/01b00bca04db48f2a2169e9249bc2abd/data',
            'http://survey123.arcgis.com/surveys/d365f6ae516345fea3cd6c329234790b/data',
            'http://survey123.arcgis.com/surveys/7641180a470b424d8182c7234c1495e5/data',
            'http://survey123.arcgis.com/surveys/30790cb7ea9648d5b992a211bd3bc4d2/data',
            'http://survey123.arcgis.com/surveys/ff4bed89defd416b9a4f8ce3135b4687/data',
            'http://survey123.arcgis.com/surveys/a4f7d9a7d9d14962b6a48e89a2146872/data',
            'http://survey123.arcgis.com/surveys/ceb279926ebc45bf97032bfa6a71262c/data',
            'http://survey123.arcgis.com/surveys/306bc76b8a1244a881e833d0f653972b/data',
            'http://survey123.arcgis.com/surveys/42313bcc9d764cd1998438b7a6ea0233/data',
            'http://survey123.arcgis.com/surveys/afcb08ab540441ada3ba7fe7ca740b4a/data',
            'http://survey123.arcgis.com/surveys/74461fa3a48d4fafb062b7c907f95491/data',
            'http://survey123.arcgis.com/surveys/fa6182e31893459a89cbf10966f6ede8/data',
            'http://survey123.arcgis.com/surveys/5a7a57a3a87c4edebcf2010bdda3b0cb/data',
            'http://survey123.arcgis.com/surveys/b74ea9b11e714e3085f001bff9fb024c/data',
            'http://survey123.arcgis.com/surveys/5ae5d46aa1264d12a0abe0a224c75a2f/data',
            'http://survey123.arcgis.com/surveys/3d5ad6d387ea49f082191b2a5c91ccd7/data',
            'http://survey123.arcgis.com/surveys/6092dd3a519f4ba3bede999fadbdba9e/data',
            'http://survey123.arcgis.com/surveys/14b81c2892534934a13767863e8e596c/data',
            'http://survey123.arcgis.com/surveys/b435439f591d4333837439785e2ec089/data',
            ]

    print('Backing up Dailys.........')
    ind = 21
    for i in list:
        webbrowser.open(i)
        time.sleep(6)
        keyboard.press_and_release('ctrl + f')
        time.sleep(4)
        keyboard.write('export')
        time.sleep(4)
        keyboard.press_and_release('enter')
        time.sleep(.25)
        keyboard.press_and_release('tab')
        time.sleep(.25)
        keyboard.press_and_release('tab')
        time.sleep(.25)
        keyboard.press_and_release('tab')
        time.sleep(.25)
        keyboard.press_and_release('enter')
        time.sleep(.25)
        keyboard.press_and_release('enter')
        time.sleep(.25)
        keyboard.press_and_release('tab')
        time.sleep(.25)
        keyboard.press_and_release('tab')
        time.sleep(.25)
        keyboard.press_and_release('tab')
        time.sleep(.25)
        keyboard.press_and_release('enter')
        time.sleep(17)
        keyboard.press_and_release('ctrl + w')
        time.sleep(.5)
        ind = ind - 1
        print(str(ind) + ' left')
    currentdate = datetime.date.today()
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\Cathodic_Protection.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\Cathodic_Protection.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(
                      currentdate) + "_Cathodic_Protection.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RESERVOIR_INSPECTIONS.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RESERVOIR_INSPECTIONS.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(
                      currentdate) + "_RESERVOIR_INSPECTIONS.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RES2_TRANSFER_PUMP.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RES2_TRANSFER_PUMP.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(
                      currentdate) + "_RES2_TRANSFER_PUMP.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\FIRE_PUMPS.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\FIRE_PUMPS.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_FIRE_PUMPS.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\NONPERMIT_CONFINED.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\NONPERMIT_CONFINED.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(
                      currentdate) + "_NONPERMIT_CONFINED.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\CONFINED_SPACE_PERMIT.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\CONFINED_SPACE_PERMIT.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(
                      currentdate) + "_CONFINED_SPACE_PERMIT.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\GENERATORS.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\GENERATORS.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_GENERATORS.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\PFDAILY.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\PFDAILY.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_PFDAILY.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\S7.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\S7.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_S7.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\112TH.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\112TH.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_112TH.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\HOLLY.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\HOLLY.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_HOLLY.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS14.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS14.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS14.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS13.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS13.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS13.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS12.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS12.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS12.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS11.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS11.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS11.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS10.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS10.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS10.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS9.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS9.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS9.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS8.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS8.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS8.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS5.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS5.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS5.xlsx")
    if os.path.exists("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS2.xlsx"):
        os.rename("\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS2.xlsx",
                  "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\DailyBackups\\" + str(currentdate) + "_LS2.xlsx")
    # MOVE AND RENAME FILES TO SERVER
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_0aea9858723047d890880287de41739f_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_0aea9858723047d890880287de41739f_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\Cathodic_Protection.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_01b00bca04db48f2a2169e9249bc2abd_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_01b00bca04db48f2a2169e9249bc2abd_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RESERVOIR_INSPECTIONS.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_d365f6ae516345fea3cd6c329234790b_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_d365f6ae516345fea3cd6c329234790b_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\RES2_TRANSFER_PUMP.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_7641180a470b424d8182c7234c1495e5_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_7641180a470b424d8182c7234c1495e5_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\FIRE_PUMPS.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_6c148b89ccde4cd18304faf632699296_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_6c148b89ccde4cd18304faf632699296_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\ls dailys")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_30790cb7ea9648d5b992a211bd3bc4d2_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_30790cb7ea9648d5b992a211bd3bc4d2_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\NONPERMIT_CONFINED.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_ff4bed89defd416b9a4f8ce3135b4687_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_ff4bed89defd416b9a4f8ce3135b4687_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\CONFINED_SPACE_PERMIT.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_a4f7d9a7d9d14962b6a48e89a2146872_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_a4f7d9a7d9d14962b6a48e89a2146872_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\GENERATORS.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_ceb279926ebc45bf97032bfa6a71262c_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_ceb279926ebc45bf97032bfa6a71262c_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\PFDAILY.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_306bc76b8a1244a881e833d0f653972b_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_306bc76b8a1244a881e833d0f653972b_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\S7.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_42313bcc9d764cd1998438b7a6ea0233_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_42313bcc9d764cd1998438b7a6ea0233_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\112TH.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_afcb08ab540441ada3ba7fe7ca740b4a_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_afcb08ab540441ada3ba7fe7ca740b4a_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\HOLLY.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_74461fa3a48d4fafb062b7c907f95491_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_74461fa3a48d4fafb062b7c907f95491_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS14.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_fa6182e31893459a89cbf10966f6ede8_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_fa6182e31893459a89cbf10966f6ede8_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS13.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_5a7a57a3a87c4edebcf2010bdda3b0cb_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_5a7a57a3a87c4edebcf2010bdda3b0cb_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS12.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_b74ea9b11e714e3085f001bff9fb024c_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_b74ea9b11e714e3085f001bff9fb024c_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS11.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_5ae5d46aa1264d12a0abe0a224c75a2f_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_5ae5d46aa1264d12a0abe0a224c75a2f_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS10.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_3d5ad6d387ea49f082191b2a5c91ccd7_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_3d5ad6d387ea49f082191b2a5c91ccd7_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS9.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_6092dd3a519f4ba3bede999fadbdba9e_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_6092dd3a519f4ba3bede999fadbdba9e_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS8.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_14b81c2892534934a13767863e8e596c_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_14b81c2892534934a13767863e8e596c_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS5.xlsx")
    if os.path.exists("C:\\Users\\brandonh\\Downloads\\S123_b435439f591d4333837439785e2ec089_EXCEL.xlsx"):
        shutil.move("C:\\Users\\brandonh\\Downloads\\S123_b435439f591d4333837439785e2ec089_EXCEL.xlsx",
                    "\\\\mukgis\\GIS Files\\Daily's\\Dailys2020\\LS2.xlsx")


def gis_files():


# GIS BACKUP
    import datetime
    import os
    import shutil

    currentdate = datetime.date.today()
    currentdate = (str(currentdate))

    sourcePath = r"\\mukgis\GIS Files\Geodatabase\LeakSurvey.gdb"
    destPath = r'P:\GisBackup\LeakSurvey'
    for root, dirs, files in os.walk(sourcePath):
        dest = destPath + root.replace(sourcePath, '')
        if not os.path.isdir(dest):
            os.mkdir(dest)
            print('Directory created at: ' + dest)
        for f in files:
            oldLoc = root + '\\' + f
            newLoc = dest + '\\' + f
            if not os.path.isfile(newLoc):
                try:
                    shutil.copy2(oldLoc, newLoc)
                    print('File ' + f + ' copied.')
                except IOError:
                    print('file "' + f + '" already exists')

    sourcePath = r'\\mukgis\GIS Files\Geodatabase\Imagery.gdb'
    destPath = r'P:\GisBackup\Imagery.gdb'
    for root, dirs, files in os.walk(sourcePath):
        dest = destPath + root.replace(sourcePath, '')
        if not os.path.isdir(dest):
            os.mkdir(dest)
            print('Directory created at: ' + dest)
        for f in files:
            if "a00000057.gdbtable" not in f:
                if "a00000052.gdbtable" not in f:
                    if "a00000011.gdbtable" not in f:
                        if "West Side Manhole Basemap   MH (600scale) 06-07-121.tif" not in f:
                            if "a0000002a.gdbtable" not in f:
                                if "a00000025.gdbtable" not in f:
                                    oldLoc = root + '\\' + f
                                    newLoc = dest + '\\' + f
                                    if not os.path.isfile(newLoc):
                                        try:
                                            shutil.copy2(oldLoc, newLoc)
                                            print('File ' + f + ' copied.')
                                        except IOError:
                                            print('file "' + f + '" already exists')

    sourcePath = r"\\mukgis\\GIS Files\\Daily's"
    destPath = r'P:\GisBackup\Dailys'
    for root, dirs, files in os.walk(sourcePath):
        dest = destPath + root.replace(sourcePath, '')
        if not os.path.isdir(dest):
            os.mkdir(dest)
            print('Directory created at: ' + dest)
        for f in files:
            oldLoc = root + '\\' + f
            newLoc = dest + '\\' + f
            if not os.path.isfile(newLoc):
                try:
                    shutil.copy2(oldLoc, newLoc)
                    print('File ' + f + ' copied.')
                except IOError:
                    print('file "' + f + '" already exists')

    sourcePath = r'\\mukgis\GIS Files\Geodatabase\Brandons_Pretreatment.gdb'
    destPath = r'P:\GisBackup\Brandons_Pretreatment.gdb'
    for root, dirs, files in os.walk(sourcePath):
        dest = destPath + root.replace(sourcePath, '')
        if not os.path.isdir(dest):
            os.mkdir(dest)
            print('Directory created at: ' + dest)
        for f in files:
            oldLoc = root + '\\' + f
            newLoc = dest + '\\' + f
            if not os.path.isfile(newLoc):
                try:
                    shutil.copy2(oldLoc, newLoc)
                    print('File ' + f + ' copied.')
                except IOError:
                    print('file "' + f + '" already exists')

    sourcePath = r'\\MUKGIS\GIS Files\Geodatabase\Water.gdb'
    destPath = r'P:\GisBackup\Water.gdb'
    for root, dirs, files in os.walk(sourcePath):
        dest = destPath + root.replace(sourcePath, '')
        if not os.path.isdir(dest):
            os.mkdir(dest)
            print('Directory created at: ' + dest)
        for f in files:
            oldLoc = root + '\\' + f
            newLoc = dest + '\\' + f
            if not os.path.isfile(newLoc):
                try:
                    shutil.copy2(oldLoc, newLoc)
                    print('File ' + f + ' copied.')
                except IOError:
                    print('file "' + f + '" already exists')

    sourcePath = r'\\MUKGIS\GIS Files\Geodatabase\Sewer.gdb'
    destPath = r'P:\GisBackup\Sewer.gdb'
    for root, dirs, files in os.walk(sourcePath):

        dest = destPath + root.replace(sourcePath, '')
        if not os.path.isdir(dest):
            os.mkdir(dest)
            print('Directory created at: ' + dest)

        for f in files:

            oldLoc = root + '\\' + f
            newLoc = dest + '\\' + f

            if not os.path.isfile(newLoc):
                try:
                    shutil.copy2(oldLoc, newLoc)
                    print('File ' + f + ' copied.')
                except IOError:
                    print('file "' + f + '" already exists')

    sourcePath = r'\\MUKGIS\GIS Files\Projects\GNet Data\Sewer.gdb'
    destPath = r'P:\GisBackup\GNet Data Sewer.gdb'
    for root, dirs, files in os.walk(sourcePath):

        dest = destPath + root.replace(sourcePath, '')

        if not os.path.isdir(dest):
            os.mkdir(dest)
            print('Directory created at: ' + dest)

        for f in files:
            oldLoc = root + '\\' + f
            newLoc = dest + '\\' + f

            if not os.path.isfile(newLoc):
                try:
                    shutil.copy2(oldLoc, newLoc)
                    print('File ' + f + ' copied.')
                except IOError:
                    print('file "' + f + '" already exists')

    sourcePath = r'\\MUKGIS\GIS Files\Geodatabase\Admin.gdb'
    destPath = r'P:\GisBackup\Admin.gdb'
    for root, dirs, files in os.walk(sourcePath):
        dest = destPath + root.replace(sourcePath, '')
        if not os.path.isdir(dest):
            os.mkdir(dest)
            print('Directory created at: ' + dest)
        for f in files:
            if "a0000006c.gdbtable" not in f:
                if "a0000003a.gdbtable" not in f:
                    if "a00000080.gdbtable" not in f:
                        if "a0000007b.gdbtable" not in f:
                            if "a0000006c.blk_key_index.atx" not in f:
                                if "a0000003a.blk_key_index.atx" not in f:
                                    oldLoc = root + '\\' + f
                                    newLoc = dest + '\\' + f
                                    if not os.path.isfile(newLoc):
                                        try:
                                            shutil.copy2(oldLoc, newLoc)
                                            print('File ' + f + ' copied.')
                                        except IOError:
                                            print('file "' + f + '" already exists')

    sourcePath = r'\\MUKGIS\GIS Files\Maps'
    destPath = r'P:\GisBackup\Maps'
    for root, dirs, files in os.walk(sourcePath):
        dest = 'P:\GisBackup\Maps'
        if not os.path.isdir(dest):
            os.mkdir(dest)
            print('Directory created at: ' + dest)
        for f in files:
            oldLoc = root + '\\' + f
            newLoc = dest + '\\' + f
            if not os.path.isfile(newLoc):
                try:
                    shutil.copy2(oldLoc, newLoc)
                    print('File ' + f + ' copied.')
                except IOError:
                    print('file "' + f + '" already exists')
        sourcePath = r'\\mukgis\GIS Files\Maps\SewerCleaning\SewerCleaning.gdb'
        destPath = r'P:\GisBackup\SewerCleaning.gdb'
        for root, dirs, files in os.walk(sourcePath):
            dest = 'P:\GisBackup\SewerCleaning.gdb'
        if not os.path.isdir(dest):
            os.mkdir(dest)
            print('Directory created at: ' + dest)
        for f in files:
            oldLoc = root + '\\' + f
            newLoc = dest + '\\' + f
            if not os.path.isfile(newLoc):
                try:
                    shutil.copy2(oldLoc, newLoc)
                    print('File ' + f + ' copied.')
                except IOError:
                    print('file "' + f + '" already exists')

    os.mkdir('P:/GisBackup/' + (str(currentdate)))

    oldname1 = "P:\GisBackup\GNet Data Sewer.gdb"
    NewName1 = "P:\GisBackup\\" + str(currentdate) + "\GNet Data Sewer.gdb"
    os.rename(oldname1, NewName1)

    oldname2 = "P:\GisBackup\Water.gdb"
    NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Water.gdb"
    os.rename(oldname2, NewName2)

    oldname2 = "P:\GisBackup\Sewer.gdb"
    NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Sewer.gdb"
    os.rename(oldname2, NewName2)
    oldname2 = "P:\GisBackup\Admin.gdb"
    NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Admin.gdb"
    os.rename(oldname2, NewName2)
    oldname2 = "P:\GisBackup\Maps"
    NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Maps"
    os.rename(oldname2, NewName2)

    oldname2 = "P:\GisBackup\SewerCleaning.gdb"
    NewName2 = "P:\GisBackup\\" + str(currentdate) + "\SewerCleaning.gdb"
    os.rename(oldname2, NewName2)

    oldname2 = "P:\GisBackup\LeakSurvey"
    NewName2 = "P:\GisBackup\\" + str(currentdate) + "\LeakSurvey"
    os.rename(oldname2, NewName2)

    oldname2 = "P:\GisBackup\Imagery.gdb"
    NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Imagery.gdb"
    os.rename(oldname2, NewName2)

    oldname2 = "P:\GisBackup\Dailys"
    NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Dailys"
    os.rename(oldname2, NewName2)

    oldname2 = "P:\GisBackup\Brandons_Pretreatment.gdb"
    NewName2 = "P:\GisBackup\\" + str(currentdate) + "\Brandons_Pretreatment.gdb"
    os.rename(oldname2, NewName2)


##################################################################################

'''
def gnet_media():
    # GNET NAS01 MEDIA TO MUKGIS ORIGINAL
    import os
    import shutil
    import datetime
    from datetime import date

    today = date.today()
    year = int(input("4 digit year"))
    month = int(input("1 or 2 digit month"))
    day = int(input("1 or 2 digit day"))
    datetostartfrom = datetime.datetime(year, month, day, 0, 0).timestamp()
    log = open("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/Logs/CopyLog" + str(today) + ".txt", "a")

    for file in os.listdir("//muknas01/Videos/Photos"):
        file = os.path.join("//muknas01/Videos/Photos/" + file)
        ModTime = os.path.getmtime(file)
        if int(ModTime) > int(datetostartfrom):
            if ".JPG" in file:
                list = file.replace("//muknas01/Videos/Photos/", "").split("~")
                folder = list[0]
                foldermkdir = "//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder)
                fileonly = list[1]
                copypath = str(
                    os.path.join("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder) + "/" + str(fileonly)))

                if not os.path.exists(foldermkdir):
                    os.mkdir(foldermkdir)
                shutil.copy(file, copypath)
                log.write("Copied " + file + " to " + copypath + "\n")

    for file in os.listdir("//muknas01/Videos/Video"):
        file = os.path.join("//muknas01/Videos/Video/" + file)
        ModTime = os.path.getmtime(file)
        if int(ModTime) > int(datetostartfrom):
            if ".mpg" in file:
                list = file.replace("//muknas01/Videos/Video/", "").split("~")
                folder = list[1]
                foldermkdir = "//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder)
                fileonly = list[2]
                copypath = str(
                    os.path.join("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder) + "/" + str(fileonly)))
                if not os.path.exists(foldermkdir):
                    os.mkdir(foldermkdir)
                shutil.copy(file, copypath)
                log.write("Copied " + file + " to " + copypath + "\n")
    print("Created log @ \\\\mukgis\GIS Files\GNET\GNET_FOLDERS_VIDS_PICS\Logs")

'''


def gnet_media():
    #WITH FLOW DIRECTION
    import os
    import shutil
    import datetime
    from datetime import date
    today = date.today()
    year = int(input("4 digit year"))
    month = int(input("1 or 2 digit month"))
    day = int(input("1 or 2 digit day"))
    datetostartfrom = datetime.datetime(year, month, day, 0, 0).timestamp()
    log = open("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/Logs/CopyLog" + str(today) + ".txt", "a")

    for file in os.listdir("//muknas01/Videos/Photos"):
        file = os.path.join("//muknas01/Videos/Photos/" + file)
        ModTime = os.path.getmtime(file)
        if int(ModTime) > int(datetostartfrom):
            if ".JPG" in file:
                if "Sewer Lateral" in file:
                    list = file.replace("//muknas01/Videos/Photos/Lateral Inspection on Sewer Lateral '", "").split("-")
                    folder = str(list[0].strip(' '))
                    numanddate = str(list[1])
                    obsandfootage = str(list[2].strip('.'))
                    address = str(list[3].strip(".JPG"))
                    foldermkdir = "//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder) + "/Laterals"
                    fileonly = address + " LATERAL_" + obsandfootage + numanddate + "-" +  "-" +  ".JPG"
                    copypath = str(
                        os.path.join(
                            "//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder) + "/" + "Laterals" +  "/" + str(fileonly)))
                    if not os.path.exists(foldermkdir):
                        os.mkdir(foldermkdir)
                    shutil.copy(file, copypath)
                    log.write("Copied " + file + " to " + copypath + "\n")
                else:
                    if "flow" in file:
                        if "clock" in file:
                            list = file.replace("//muknas01/Videos/Photos/", "").split("~")
                            direction = list[0]
                            folder = list[1]
                            clock = list[3].replace("'","_")
                            fileonly = str(list[0]) + "_" +  str(list[2]) + str(clock)
                    foldermkdir = "//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder)
                    fileonly = str(list[0]) + "_" + str(list[2] + "_" + clock)
                    copypath = str(
                        os.path.join("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder) + "/" + str(fileonly)))
                if not os.path.exists(foldermkdir):
                    os.mkdir(foldermkdir)
                shutil.copy(file, copypath)
                log.write("Copied " + file + " to " + copypath + "\n")
    for file in os.listdir("//muknas01/Videos/Video"):
        file = os.path.join("//muknas01/Videos/Video/" + file)
        ModTime = os.path.getmtime(file)
        if int(ModTime) > int(datetostartfrom):
            if ".mpg" in file:
                if "-Sewer Lateral " in file:
                    list = file.replace("//muknas01/Videos/Video/", "").split("-")
                    folder1 = str(list[1].strip("Sewer Lateral '"))
                    folder = folder1.strip(" ")
                    foldermkdir = "//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder) + "/Laterals"
                    address = str(list[3].strip(".mpg"))
                    addresswithmpg = str(address) + ".mpg"
                    if not os.path.exists(foldermkdir):
                        os.mkdir(foldermkdir)
                    copypath = str(os.path.join(
                    "//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder) + "/" + "Laterals" +  "/" + str(addresswithmpg)))
                    shutil.copy(file, copypath)
                    log.write("Copied " + file + " to " + copypath + "\n")
                else:
                    list = file.replace("//muknas01/Videos/Video/", "").split("~")
                    direction = list[0]
                    folder = list[2]
                    foldermkdir = "//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder)
                    fileonly = str(list[0]) + "_" + str(list[3])
                    copypath = str(
                        os.path.join("//mukgis/GIS Files/GNET/GNET_FOLDERS_VIDS_PICS/" + str(folder) + "/" + str(fileonly)))
                    if not os.path.exists(foldermkdir):
                        os.mkdir(foldermkdir)
                    shutil.copy(file, copypath)
                    log.write("Copied " + file + " to " + copypath + "\n")
    print("Created log @ \\\\mukgis\GIS Files\GNET\GNET_FOLDERS_VIDS_PICS\Logs")

arg_dict = {"1": daily, "2": gnet_media, "3": gis_files, "4": inspected, "5": locates, "6": graph, "7": county,"8": exit}

if __name__ == '__main__':
    menu_selection(prompt, arg_dict)
