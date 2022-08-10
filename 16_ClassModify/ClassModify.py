import glob
import os

import time

import numpy as np
import random

import shutil

# 라벨링된 파일을 옮깁니다. 이미지는 카피하고 라벨링 txt 파일은 클래스를 바꿔야 한다면 조건에 따라 수정해서 넘길 수 있도록 합니다.
# 지금은 5C (사람_차량_트럭_오토바이_버스) 에서 3C 로 수정 (차량_버스_오토)

TargetPATH = "\\\\192.168.0.148\\h\\[20211124] 콜롬비아 2차\\이미지_라벨링 데이터\\"
DestPATH = "\\\\192.168.0.148\\h\\[20211124] 콜롬비아 2차\\이미지_라벨링 데이터_3C\\"

TXTExt = ".txt"
JPGExt = ".jpg"

PATHList = os.listdir(TargetPATH)

print(PATHList)

for Path_ in PATHList:

    tPATH = TargetPATH + Path_
    dPATH = DestPATH + Path_
    
    print(tPATH, end=" =>> ")
    print(dPATH)

    if not(os.path.isdir(dPATH)):
            os.makedirs(dPATH)

    FileList = os.listdir(tPATH)

    for File_ in FileList:
        TargetFilePATH = tPATH + "\\" + File_
        DestFilePATH = dPATH + "\\" + File_
        if TargetFilePATH[-4:] == TXTExt:
            # print(TargetFilePATH)
            LabelFile = open(TargetFilePATH, 'r+')
            ObjectList = LabelFile.readlines()
            ListStack = []
            for Obj_ in ObjectList:
                Obj_ = Obj_.split(" ")
                ListStack.append(Obj_)
            ReLabelFile = open(DestFilePATH, 'w+')

            for Stack_ in ListStack:
                if(Stack_[0] == '0'): # Person => skip
                    continue
                elif(Stack_[0] == '1'): # Car => 0
                    ReLabelFile.write('0')
                elif(Stack_[0] == '2'): # Truck => 1
                    ReLabelFile.write('1')
                elif(Stack_[0] == '3'): # Motoby => 2
                    ReLabelFile.write('2')
                elif(Stack_[0] == '4'): # Bus => 1
                    ReLabelFile.write('1')

                ReLabelFile.write(" ")
                ReLabelFile.write(Stack_[1])
                ReLabelFile.write(" ")
                ReLabelFile.write(Stack_[2])
                ReLabelFile.write(" ")
                ReLabelFile.write(Stack_[3])
                ReLabelFile.write(" ")
                ReLabelFile.write(Stack_[4])
            
            LabelFile.close()
            ReLabelFile.close()

        elif TargetFilePATH[-4:] == JPGExt: 
            shutil.copy(TargetFilePATH, dPATH)