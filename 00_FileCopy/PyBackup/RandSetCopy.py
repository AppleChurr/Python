import glob
import os

import time

import numpy as np
import random

import shutil

File_PATH = os.getcwd()+"\\"
Ext = [".jpg", ".txt"]

# 하위 ListFile 경로 상에 있는 txt 파일 내에 있는 이름과 동일한 txt 파일과 jpg 파일을
# 하위 Random 폴더에 저장. 단, 20번을 반복하여 0~19 번의 이름을 가진 폴더로 랜덤하게 생성한다.
# 랜덤하게 만들어지는 갯수는 nRandom 의 수로 아래에 300이다.
# 그 외에는 FileCopy와 동일.

#TXTList = ["List_YOLO.txt", "List_SigNet.txt", "YOLO_SigNet.txt"]
#TXTList = ["YOLO_SigNet.txt"]
TXTList = ["1K_00.txt"]

for Ridx in range(0, 20):
    for txtName in TXTList:
        if Ridx < 10 :
            Dest_PATH = File_PATH + "Random" + "\\RandSet0" + str(Ridx) + "\\"
        else :
            Dest_PATH = File_PATH + "Random" + "\\RandSet" + str(Ridx) + "\\"
        

        if not(os.path.isdir(Dest_PATH)):
            os.makedirs(os.path.join(Dest_PATH))

        print(Dest_PATH)

        if not(os.path.isdir(Dest_PATH)):
            os.makedirs(os.path.join(Dest_PATH))

        MoveListTXT = open(File_PATH + "ListFile\\" + txtName, 'r', encoding="UTF8")
        CopyList = MoveListTXT.readlines()
        MoveListTXT.close()

        nRandom = 300
        nData = len(CopyList)

        RandSet = np.round((nData-1)*np.random.rand(1, nRandom))

        RandSet = set(RandSet[0])

        while len(RandSet)<nRandom:
            RandVal = np.round((nData-1)*np.random.rand())
            RandSet.add(RandVal)

        RandSet = list(RandSet)
        RandSet.sort()
        RandSet = set(map(int, RandSet))

        for RandIdx in RandSet:
            TargetFile = CopyList[RandIdx]
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
