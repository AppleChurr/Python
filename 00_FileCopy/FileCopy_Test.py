import glob
import os

import time

import shutil

File_PATH = os.getcwd()+"\\"
Dest_PATH = File_PATH + "img\\"
Ext = [".jpg", ".txt"]

if not(os.path.isdir(Dest_PATH)):
    os.makedirs(os.path.join(Dest_PATH))

MoveListTXT = open(File_PATH + "List.txt", 'r', encoding="UTF8")
MoveList = MoveListTXT.readlines()
MoveListTXT.close()

for MoveFile in MoveList:
    MoveFile = MoveFile.split("\n")[0]

    for ext in Ext:
        Dest_File = os.path.join(Dest_PATH, MoveFile + ext)
        print(File_PATH + MoveFile + ext + "\n\t>>", Dest_File)
        if os.path.exists(Dest_File):
            try:
                os.remove(Dest_File)
            except:
                print('\tRemove Fail : \n', Dest_File)
                continue
        shutil.copy(MoveFile + ext, Dest_PATH)
