#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os, sys
from PIL import Image
import piexif
import shutil

rootdir = os.getcwd()
dirname = rootdir


def image_sort(path, recur=0):
    if not recur:
        print("   sorting started ...")

    imagelist = []

    if os.path.isdir(path):
        for x in os.listdir(path):

            absx = os.path.join(path, x)

            if os.path.isfile(absx):
                imagelist.append(absx)
            else:
                print("summon subsort in %s" % x)
                image_sort(absx, recur=1)

        for fname in imagelist:
            try:

                resolution = Image.open(fname).size

                kartinka = piexif.load(fname)
                datetime = None
            except IOError:
                print("not an image: %s" % fname)
                continue
            except Exception:

                datetime = "0000:00"
            else:
                for i in ("0th", "Exif", "GPS", "1st"):
                    for tag in kartinka[i]:

                        if ((piexif.TAGS[i][tag]["name"] == "DateTime") or (
                                (piexif.TAGS[i][tag]["name"] == "DateTimeOriginal"))):
                            datetime = kartinka[i][tag]

                if (datetime == None):
                    datetime = b'0000:00'
                datetime = datetime.decode("utf-8")

            foldername = datetime[5:7] + "." + datetime[0:4]

            imdir = os.path.join(rootdir, foldername)

            if imdir == os.path.split(fname)[-2]:
                continue
            elif not os.path.exists(imdir):
                print("making dir %s" % imdir)
                os.mkdir(imdir)
            try:

                shutil.copyfile(fname, os.path.join(imdir, os.path.split(fname)[-1]))
                os.remove(fname)
            except WindowsError:
                print("error with %s/n" % fname)
    if not recur: print("  sorting completed!")


def del_empty_dirs(path):
    for d in os.listdir(path):
        a = os.path.join(path, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)
                print(a, " deleted")


image_sort(dirname)
print("   delete empty folders")
del_empty_dirs(dirname)
print("  deleted completed!")
path = dirname
for folder in os.listdir(path):
    if not '.py' in folder:

        try:
            os.rename(folder, folder.replace('01.', 'Jan_'))
            os.rename(folder, folder.replace('02.', 'Feb_'))
            os.rename(folder, folder.replace('03.', 'Mar_'))
            os.rename(folder, folder.replace('04.', 'Apr_'))
            os.rename(folder, folder.replace('05.', 'May_'))
            os.rename(folder, folder.replace('06.', 'Jun_'))
            os.rename(folder, folder.replace('07.', 'Jul_'))
            os.rename(folder, folder.replace('08.', 'Aug_'))
            os.rename(folder, folder.replace('09.', 'Sep_'))
            os.rename(folder, folder.replace('10.', 'Oct_'))
            os.rename(folder, folder.replace('11.', 'Nov_'))
            os.rename(folder, folder.replace('12.', 'Dec_'))
            os.rename(folder, folder.replace('00.0000', 'DO THESE MANUALLY'))
        except FileNotFoundError:
            pass