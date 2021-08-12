import numpy as np
import os
import sys

CSVFileName = "Data.csv"

CSVRawData = open(CSVFileName)

CSVLines = CSVRawData.readlines()

for line in CSVLines:
    Data = line.split(',')
    ii = 0
    for Data_ in Data:
        Data_ = Data_.split('\n')
        if(len(Data_) > 1):
            print("%.2f" %float(Data_[0]))
        else:
            print("%.2f" %float(Data_[0]), end='\t')
        
