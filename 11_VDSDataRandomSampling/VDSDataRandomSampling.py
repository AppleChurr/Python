import sys
import os
import random

SplitCom = ','
SplitSp = ' '
SplitCor = ':'
csvFmt = ".csv"
FileList = os.listdir()

random.seed()

for file_ in FileList:
    lFmt = file_[-4:]
    nMin = 0
    if(lFmt == csvFmt):
        for ii in range(0, 18): # 여기 0, 0 이에요!!!
            lFile = open(file_, 'r')
            dFile = open(file_[:-4] + "_" + str(ii) + ".csv", 'w')

            lines = lFile.readlines()
            for ii in range(0, len(lines)).__reversed__():
                line = lines[ii]
                line = line.split(SplitCom)

                if(random.random() < 0.033):
                    continue

                # t = line[0].strip('\n') # 시간
                # d = line[1].strip('\n') # 상행/하행
                # l = line[2].strip('\n') # 차선

                # t = t.split(SplitCor)

                # dFile.write("2020-12-22")
                # dFile.write(',')

                # dFile.write("00:")
                # dFile.write(t[1].strip('\n'))
                # dFile.write(':')
                # dFile.write(t[2].strip('\n'))
                # dFile.write(',')

                # dFile.write(d)
                # dFile.write(',')

                # dFile.write(l)
                # dFile.write(',')

                # dFile.write('\n')

            lFile.close
            dFile.close

        
        