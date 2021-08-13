import sys
import os
from datetime import date
import cv2

def GetVideoInfo(vCapture):
    length = int(vCapture.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(vCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(vCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = vCapture.get(cv2.CAP_PROP_FPS)
 
    return length, width, height, fps

def Second2Time(Second):

    ss = int(Second)
    ms = int((Second - int(ss)) * 1000)
    if(ms < 10):
        ms = "00" + str(ms)
    elif(ms < 100):
        ms = "0" + str(ms)
    else:
        ms = str(ms)

    mm = int(ss / 60)
    ss = ss % 60
    if(ss < 10):
        ss = "0" + str(ss)
    else:
        ss = str(ss)

    hh = int(mm / 60)
    if(hh < 10):
        hh = "0" + str(hh)
    else:
        hh = str(hh)

    mm = mm % 60
    if(mm < 10):
        mm = "0" + str(mm)
    else:
        mm = str(mm)

    return hh, mm, ss, ms

# vFilePath = sys.argv[1]

FileList = os.listdir()

for file_ in FileList:

    vFmt = file_[-4:]
    if(vFmt == ".mp4" or vFmt == ".mkv" or vFmt == ".avi"):
        vFileName = file_[:-4]
        vCapture = cv2.VideoCapture(vFileName + vFmt)

        if vCapture.isOpened():
            iFmt = ".idx"
            vLength, _, _, vFPS = GetVideoInfo(vCapture)
            vSPF = 1/vFPS

            YY = str(date.today().year)
            MM = str(date.today().month)
            DD = str(date.today().day)

            print("          Today : " + YY + "." + MM + "." + DD, end='\n\n')

            print('         Length : %d' %vLength)
            print('            FPS : %.3f' %vFPS)
            print('Total Play Time : %.3f' %(vLength * vFPS))
            print('            SPF : %.3f' %vSPF)

            Idxfile = open(vFileName + iFmt, 'w')

            for vIdx in range(0, vLength):
                hh, mm, ss, ms = Second2Time(vIdx * vSPF)
                Idxfile.write(str(vIdx) + ", " + YY + "." + MM + "." + DD + 
                    "-" + hh + ":" + mm  + ":" + ss  + "." + ms + '\n')

            vCapture.release()
            Idxfile.close()
        else:
            print(sys.argv[1] + " is not found")
