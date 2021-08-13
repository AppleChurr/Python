import sys
import os

FileList = os.listdir()
cFmt = ".csv"
for file_ in FileList:
    xFmt = file_[-4:]
    if(xFmt == ".txt"):
        xFileName = file_[:-4]
        xFile = open(file_, 'r')
        cFile = open(xFileName + cFmt, 'w+')

        for xData_ in xFile:
            # print(len(xData_))
            for ii in range(0, len(xData_)):
                if xData_[ii] != '\n':
                    # print(xData_[ii], end=",")
                    cFile.write(xData_[ii])
                    cFile.write(",")
            # print("\n", end="")
            cFile.write("\n")

        xFile.close()
        cFile.close()