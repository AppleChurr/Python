import os
import sys

# DATAPATH = ["\\\\192.168.0.148\\g\\학습데이터\\011_5C_청주\\01_청주_data\\" ,  # 1520 장
#             "\\\\192.168.0.148\\g\\학습데이터\\009_5C_청주준비\\02_화성교차로추가본\\", # 2290 장
#             "\\\\192.168.0.148\\g\\학습데이터\\001_5C_교차로\\01_Data\\"] # 10308

DATAPATH = ["D:\\20_Data\\해강안 캡쳐폴더(선박,사람)\\"]

DATAEXT = ".txt"

SplitChar = ' '

CSVFile = open("MergeData.csv", 'w')


for PATH_ in DATAPATH:
    FileList = os.listdir(PATH_)

    for file_ in FileList:
        if(file_[-4:] == DATAEXT):
            gtData = open(PATH_ + file_, 'r')
            print(PATH_ + file_)
            lines = gtData.readlines()
            for line in lines:
                line = line.split(SplitChar)
                if(len(line) == 5):
                    [DataClass, DataCx, DataCy, DataW, DataH] = line

                    Rate = (int(float(DataW)* 10000) / 10000) / (int(float(DataH.strip('\n')) * 10000) / 10000 + 0.0000001)

                    CSVFile.write(DataClass)
                    CSVFile.write(',')
                    CSVFile.write(str(int(float(DataW)* 10000) / 10000))
                    CSVFile.write(',')
                    CSVFile.write(str(int(float(DataH.strip('\n')) * 10000) / 10000))
                    CSVFile.write(",")
                    CSVFile.write(str(int(float(Rate)* 10000) / 10000))
                    CSVFile.write(",\n")

            gtData.close()

CSVFile.close()
    