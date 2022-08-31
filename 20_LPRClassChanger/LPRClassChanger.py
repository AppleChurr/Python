import os
from pickletools import uint8
import numpy as np
import cv2

DATA_PATH = "D:\\20_Data\\50_번호판 데이터\\TrainingData\\한줄\\"

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'

FileList = os.listdir(DATA_PATH)

fNames = open(DATA_PATH + "name.names", 'r')
dNames = dict()
ii = 0

for _line in fNames.readlines():
    dNames[str(ord(_line.split("\n")[0]))] = str(ii)
    ii = ii + 1

print(dNames)

for file_ in FileList:
    tFileName = file_[:-4]
    tFmt = file_[-4:]
    if(tFmt == ".txt"):
        tFile = open(DATA_PATH + file_, 'r')
        _NewData = ''
        for tData in tFile.readlines():
            sData = tData.split(' ')
            sData[0] = dNames[sData[0]]
            for aData in sData:
                _NewData += aData
                if(_NewData[-1] != '\n'):
                    _NewData += ' '


        print(_NewData)
        tFile.close()

        tFile = open(DATA_PATH + file_, 'w')
        tFile.write(_NewData)
        tFile.close()
        