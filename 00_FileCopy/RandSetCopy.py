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

FileList = os.listdir()

TXTList = []

for _File in FileList:
    if(_File[-4:] == ".txt"):
        TXTList.append(_File)
    
for Ridx in range(0, 10000):
    if(len(TXTList) == 0):
        break

    if Ridx < 10 :
        Dest_PATH = File_PATH + "Random" + "\\RandSet_000" + str(Ridx) + "\\"
    elif Ridx < 100 :
        Dest_PATH = File_PATH + "Random" + "\\RandSet_00" + str(Ridx) + "\\"
    elif Ridx < 1000 :
        Dest_PATH = File_PATH + "Random" + "\\RandSet_0" + str(Ridx) + "\\"
    else:
        Dest_PATH = File_PATH + "Random" + "\\RandSet_" + str(Ridx) + "\\"
    
    if not(os.path.isdir(Dest_PATH)):
        os.makedirs(os.path.join(Dest_PATH))

    print(Dest_PATH)

    nRandom = 30
    if(nRandom > len(TXTList)):
        nRandom = len(TXTList)

    nData = len(TXTList)

    RandSet = np.round((nData-1)*np.random.rand(1, nRandom))

    RandSet = set(RandSet[0])

    while len(RandSet)<nRandom:
        RandVal = np.round((nData-1)*np.random.rand())
        RandSet.add(RandVal)

    RandSet = list(RandSet)
    RandSet.sort()
    RandSet = set(map(int, RandSet))

    for RandIdx in RandSet:
        TargetFile = TXTList[RandIdx][:-4]

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

    RandSet = list(RandSet)
    RandSet.sort()
    RandSet.reverse()
    for RandIdx in RandSet: 
        TXTList.pop(RandIdx)
