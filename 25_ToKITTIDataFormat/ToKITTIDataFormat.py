import os
import sys
from PIL import Image
import numpy as np
import time
import glob

SAVEPATH = "./KITTI/"
DATAEXT = ".txt"
IMGEXT = ".jpg"

if not(os.path.isdir(SAVEPATH)):
    os.makedirs(os.path.join(SAVEPATH))

DirFileList = os.listdir()

names = open("name.names", 'r')

lClass = []

lines = names.readlines()
for line in lines:
    line = line.split('\n')
    lClass.append(line[0])
names.close()

for file_ in DirFileList:
    if(file_[-4:] == DATAEXT):
        print(file_)
        lData = open(file_, 'r')

        if os.path.isfile(file_[:-4] + IMGEXT):
            with Image.open(file_[:-4] + IMGEXT) as img:
                iw, ih = img.size
                print(f"Image size: {iw}x{ih}")
            

            kittiData = open(SAVEPATH + file_, 'w')

            labels = lData.readlines()
            for label in labels:
                label = label.split('\n')
                label = label[0].split(' ')

                
                width = float(label[3]) * iw
                height = float(label[4]) * ih

                left = float(label[1]) * iw - width / 2
                top = float(label[2]) * ih - height / 2

                kittiLabel = [lClass[int(label[0])], "0.00", "0", "0.00", str(left), str(top), str(left + width), str(top + height), "0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00"]

                print(kittiLabel)

                for kitti in kittiLabel:
                    kittiData.write(kitti)
                    kittiData.write(' ')

                kittiData.write('\n')

            kittiData.close()
            



