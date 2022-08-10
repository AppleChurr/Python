import sys
import os

import shutil

DATA_PATH = "D:\\20_Data\\[20220809] 연천 DZoom 이미지 통합\\"

WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


FileList = os.listdir(DATA_PATH)

for file_ in FileList:
    tFileName = file_[:-4]
    tFmt = file_[-4:]
    if(tFmt == ".txt"):
        tFile = open(DATA_PATH + file_, 'r')
        _NewData = ''
        for tData in tFile.readlines():
            tData = tData.replace(",", "")
            _NewData += tData

        print(_NewData)
        tFile.close()

        tFile = open(DATA_PATH + file_, 'w')
        tFile.write(_NewData)
        tFile.close()
        