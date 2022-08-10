import sys
import os

import shutil



COCO_PATH = "D:\\20_Data\\02_COCO\\"

fPerson = "0_Person"
fVehicle = "1_Vehicle"
fPersonVehicle = "2_Person_and_Vehicle"

FileList = os.listdir(COCO_PATH)

if not(os.path.isdir(COCO_PATH + fPerson)):
    os.makedirs(COCO_PATH + fPerson)

if not(os.path.isdir(COCO_PATH + fVehicle)):
    os.makedirs(COCO_PATH + fVehicle)

if not(os.path.isdir(COCO_PATH + fPersonVehicle)):
    os.makedirs(COCO_PATH + fPersonVehicle)

for file_ in FileList:
    dCount = [0, 0, 0, 0, 0] # 사람, 차, 트럭, 오토바이, 버스
    tFileName = file_[:-4]
    tFmt = file_[-4:]
    if(tFmt == ".TXT"):
        if(os.path.isfile(COCO_PATH + tFileName + ".TXT") and os.path.isfile(COCO_PATH + tFileName + ".jpg")):
            tFile = open(COCO_PATH + file_, 'r')
            
            for tData in tFile.readlines():
                dIdx = int(tData[0]) - int('0')
                dCount[dIdx] = dCount[dIdx] + 1
                    
            if(dCount[0] == 0 and (dCount[1] != 0 or dCount[2] != 0  or dCount[3] != 0 or dCount[4] != 0)): # 차량 류 만
                fGoal = fVehicle + "\\"
            elif(dCount[0] != 0 and dCount[1] == 0 and dCount[2] == 0  and dCount[3] == 0 and dCount[4] == 0): # 사람만
                fGoal = fPerson + "\\"
            elif(dCount[0] != 0 and (dCount[1] != 0 or dCount[2] != 0  or dCount[3] != 0 or dCount[4] != 0)): # 둘다
                fGoal = fPersonVehicle + "\\"
            else:
                fGoal = ""

            if not(os.path.isfile(COCO_PATH + fGoal + tFileName + ".TXT") and os.path.isfile(COCO_PATH + fGoal + tFileName + ".jpg")):
                shutil.copy(COCO_PATH + tFileName + ".TXT", COCO_PATH + fGoal)
                shutil.copy(COCO_PATH + tFileName + ".jpg", COCO_PATH + fGoal)

    print("{:.2f} %".format(round(FileList.index(file_) / len(FileList) * 100.0, 2)), end="\r")  