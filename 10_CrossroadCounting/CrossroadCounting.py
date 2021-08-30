import sys
import os

def str2int(sData):
    nData = len(sData)
    iData = 0
    for idx in range(0, nData):
        iData = iData + (ord(sData[idx]) - ord('0')) * (10 ** (nData - idx - 1))
    return iData

def SplitData(line):
    Device = line[0]
    StartTime = line[1].split(SplitCor)
    StartSec = float(str2int(StartTime[0])) * 3600 + float(str2int(StartTime[1])) * 60 + float(str2int(StartTime[2])) + float(str2int(StartTime[3])) / 1000.
    EndTime = line[2].split(SplitCor)
    EndSec = float(str2int(EndTime[0])) * 3600 + float(str2int(EndTime[1])) * 60 + float(str2int(EndTime[2])) + float(str2int(EndTime[3])) / 1000.
    Dir = line[3]
    return Device, StartSec, EndSec, Dir

def SaveAndReset(File, Line, nMin, rMin):
    nMin = nMin + rMin
    for idx in range(0, 5):
        File.write(str(Line[idx]))
        File.write(',')
    File.write('\n')
    Line = [nMin, 0, 0, 0, 0]
    return File, Line, nMin

if(len(sys.argv) == 1):
    rMin = 300
elif(len(sys.argv) == 2):
    rMin = sys.argv[1] * 60

SplitCom = ','
SplitSp = ' '
SplitCor = ':'
csvFmt = ".csv"
FileList = os.listdir()

for file_ in FileList:
    if(file_[-6:-4] == "_d"):
        break

    lFmt = file_[-4:]
    nMin = 0
    if(lFmt == csvFmt):
        lFile = open(file_, 'r')
        dFile = open(file_[:-4] + "_d.csv", 'w')

        dFile.write("시간,좌회전,우회전,직진,유턴\n")
        dLine = [nMin, 0, 0, 0, 0]
        lines = lFile.readlines()
        for line in lines:
            line = line.split(SplitCom)

            Device, StartSec, EndSec, Dir = SplitData(line)

            if (nMin+rMin) < EndSec:
                dFile, dLine, nMin = SaveAndReset(dFile, dLine, nMin, rMin)

            if(Dir == "좌회전"):
                dLine[1] = dLine[1] + 1
            elif(Dir == "우회전"):
                dLine[2] = dLine[2] + 1
            elif(Dir == "직진"):
                dLine[3] = dLine[3] + 1
            elif(Dir == "유턴"):
                dLine[4] = dLine[4] + 1

            print(Device, StartSec, EndSec, Dir)

        lFile.close
        dFile.close
