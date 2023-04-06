import os
import sys
import cv2
import numpy as np
# DATAPATH = ["\\\\192.168.0.148\\g\\학습데이터\\011_5C_청주\\01_청주_data\\" ,  # 1520 장
#             "\\\\192.168.0.148\\g\\학습데이터\\009_5C_청주준비\\02_화성교차로추가본\\", # 2290 장
#             "\\\\192.168.0.148\\g\\학습데이터\\001_5C_교차로\\01_Data\\"] # 10308

DATAPATH = ["D:\\20_Data\\해강안 캡쳐폴더(선박,사람)\\"]

DATAEXT = ".txt"

IMGEXT = ".jpg"

SplitChar = ' '

CSVFile = open("MergeData.csv", 'w')


for PATH_ in DATAPATH:
    FileList = os.listdir(PATH_)

    for file_ in FileList:
        if(file_[-4:] == DATAEXT):
            print(PATH_ + file_)
            gtData = open(PATH_ + file_, 'r')

            imgArray = np.fromfile(PATH_ + file_[:-4] + IMGEXT, np.uint8)
            imgData = cv2.imdecode(imgArray,  cv2.IMREAD_COLOR) 

            print(imgData.shape)


            
            lines = gtData.readlines()
            for line in lines:
                line = line.split(SplitChar)
                if(len(line) == 5):
                    [DataClass, DataCx, DataCy, DataW, DataH] = line
                    DataH = DataH.strip('\n')

                    Rate = (int(float(DataW)* 10000) / 10000) / (int(float(DataH) * 10000) / 10000 + 0.0000001)
                    
                    xPixel = int(float(DataCx) * imgData.shape[1])
                    yPixel = int(float(DataCy) * imgData.shape[0])
                    
                    wPixel = int(float(DataW) * imgData.shape[1])
                    hPixel = int(float(DataH) * imgData.shape[0])

                    exData = str(DataClass) + ", " + str(DataCx) + ", " + str(DataCy) + ", " + str(DataW)  + ", " + str(DataH) + ", " + str(xPixel) + ", " + str(yPixel) + ", " + str(wPixel) + ", " + str(hPixel) + ", " + str(Rate) + "\n"
                    
                    print(exData)

                    CSVFile.write(exData)

            gtData.close()

CSVFile.close()
    