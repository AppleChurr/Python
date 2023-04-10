import os
import sys
from PIL import Image
import numpy as np
import time
import glob

SAVEPATH = "./KITTI_"
DATAEXT = ".txt"
IMGEXT = ".jpg"

config = open("config.ini", 'r')

ditcConfig = {"START_INDEX":0, "MIN_WIDTH":30, "MIN_HEIGHT":30, "DIST_IMG_WIDTH":1280, "DIST_IMG_HEIGHT":720}
for line in config.readlines():
    line = line.split('\n')[0]
    dictEle = line.split('=')
    ditcConfig.update({dictEle[0]:int(dictEle[1])})

SAVEPATH += str(ditcConfig["DIST_IMG_WIDTH"]) + "x" + str(ditcConfig["DIST_IMG_HEIGHT"]) + "/"

if not(os.path.isdir(SAVEPATH)):
    os.makedirs(os.path.join(SAVEPATH))

DirFileList = os.listdir()

names = open("name.names", 'r')



save_idx = ditcConfig["START_INDEX"]

lClass = []

lines = names.readlines()
for line in lines:
    line = line.split('\n')
    lClass.append(line[0])
names.close()

iw = 1280
ih = 720

for file_ in DirFileList:
    if(file_[-4:] == DATAEXT):
        title = file_[:-4]
        print(file_)
        lData = open(file_, 'r')

        if os.path.isfile(title + IMGEXT):
            with Image.open(title + IMGEXT) as img:
                # iw, ih = img.size
                print(f"Image size: {iw}x{ih}")
                img = img.resize([ditcConfig["DIST_IMG_WIDTH"], ditcConfig["DIST_IMG_HEIGHT"]])
                img.save(SAVEPATH + str(save_idx).zfill(10) + IMGEXT)
            

            kittiData = open(SAVEPATH + str(save_idx).zfill(10) + DATAEXT, 'w')

            labels = lData.readlines()
            for label in labels:
                label = label.split('\n')
                label = label[0].split(' ')

                
                width = float(label[3]) * iw
                height = float(label[4]) * ih

                if((width <= ditcConfig["MIN_WIDTH"]) or (height <= ditcConfig["MIN_HEIGHT"])):
                    continue

                left = float(label[1]) * iw - width / 2
                top = float(label[2]) * ih - height / 2

                

                kittiLabel = [lClass[int(label[0])], "0.00", "0", "0.00", str(left), str(top), str(left + width), str(top + height), "0.00", "0.00", "0.00", "0.00", "0.00", "0.00", "0.00"]

                print(kittiLabel)

                for kitti in kittiLabel:
                    kittiData.write(kitti)
                    kittiData.write(' ')

                kittiData.write('\n')

            kittiData.close()

            save_idx += 1
            



