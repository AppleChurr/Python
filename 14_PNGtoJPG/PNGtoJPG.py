import sys
import os
from datetime import date
import cv2
import numpy as np

FileList = os.listdir()

PNG = ".png"
JPG = ".jpg"

for file_ in FileList:
    iFmt = file_[-4:]
    if(iFmt.lower() == PNG):
        print(file_)
        iFileName = file_[:-4]
        iArray = np.fromfile(file_, np.uint8)
        iMat = cv2.imdecode(iArray,  cv2.IMREAD_COLOR) 
        cv2.imwrite(iFileName[-23:] + JPG, iMat)
        os.remove(file_)
