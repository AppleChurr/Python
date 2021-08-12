import glob
import os

import time

import shutil

File_PATH = os.getcwd()+"\\"
Ext = [".jpg", ".txt"] 

# 하위 ListFile 경로 상에 있는 txt 파일 내에 있는 이름과 동일한 txt 파일과 jpg 파일을
# 해당 파일 이름과 같은 폴더로 복사해 저장.


# TXTList = ["List_YOLO.txt", "List_SigNet.txt", "YOLO_SigNet.txt"]
# TXTList = ["YOLO_SigNet.txt"]
TXTList = ["1K_00.txt"]

for txtName in TXTList:
    Dest_PATH = File_PATH + txtName[:-4] + "\\"
    if not(os.path.isdir(Dest_PATH)):
        os.makedirs(os.path.join(Dest_PATH))

    print(Dest_PATH)

    if not(os.path.isdir(Dest_PATH)):
        os.makedirs(os.path.join(Dest_PATH))

    MoveListTXT = open(File_PATH + "ListFile\\" + txtName, 'r', encoding="UTF8")
    CopyList = MoveListTXT.readlines()
    MoveListTXT.close()

    for TargetFile in CopyList:
        TargetFile = TargetFile.split("\n")[0]

        for ext in Ext:
            Dest_File = os.path.join(Dest_PATH, TargetFile + ext)
            if os.path.exists(Dest_File):
                try:
                    os.remove(Dest_File)
                except:
                    print('\tRemove Fail : \n', Dest_File)
                    continue

            if not os.path.isfile(TargetFile + ext):
                print("Target File Is Wrong >> ", TargetFile + ext)
                break

            print(File_PATH + TargetFile + ext + "\n\t>>", Dest_File)
            shutil.copy(TargetFile + ext, Dest_PATH)
