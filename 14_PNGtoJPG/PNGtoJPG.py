import sys
import os
from datetime import date
import cv2

FileList = os.listdir()

for file_ in FileList:

    vFmt = file_[-4:]
    if(vFmt == ".png"):
        vFileName = file_[:-4]
        vCapture = cv2.imread(file_)
        cv2.imwrite(vFileName+".jpg", vCapture)
        os.remove(file_)

