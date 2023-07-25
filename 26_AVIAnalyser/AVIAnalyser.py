import os
import matplotlib.pyplot as plt
from PIL import Image
import csv
import glob

# AVI Class
class AVIClass:
    def __init__(self):
        self.__Path = ""
        self.__Fmt = ""

        self.__Year = -1
        self.__Month = -1
        self.__Day = -1

        self.__Hour = -1
        self.__Minute = -1
        self.__Seconds = -1

        self.__Lane = "00"
        self.__Plate = "Empty"

        self.__Brightness = -1

    def setFromImg(self, imgPath):
        self.__Path = imgPath
        self.__Fmt = imgPath[-4:]

        file = imgPath[:-4]
        lfile = file.split('_')

        self.__Year = int(lfile[0][:4])
        self.__Month = int(lfile[0][4:6])
        self.__Day = int(lfile[0][6:8])

        self.__Hour = int(lfile[0][8:10])
        self.__Minute = int(lfile[0][10:12])
        self.__Seconds = int(lfile[0][12:])

        self.__Lane = lfile[2]
        self.__Plate = lfile[3]

        print(os.path.join(fPATH, imgPath))
        image = Image.open(os.path.join(fPATH, imgPath)).convert("L")
        pixels = list(image.getdata())
        image_brightness = int(sum(pixels) / len(pixels))
        self.__Brightness = image_brightness

    def setFromList(self, listdata):
        self.__Path = listdata[0]
        self.__Fmt = listdata[1]

        self.__Year = int(listdata[2])
        self.__Month = int(listdata[3])
        self.__Day = int(listdata[4])

        self.__Hour = int(listdata[5])
        self.__Minute = int(listdata[6])
        self.__Seconds = int(listdata[7])

        self.__Lane = listdata[8]
        self.__Plate = listdata[9]

        self.__Brightness = int(listdata[10])

    def getDate(self):
        return str(self.__Year).zfill(4) + "-" + str(self.__Month).zfill(2) + "-" + str(self.__Day).zfill(2)

    def getTime(self):
        return str(self.__Hour).zfill(2) + ":" + str(self.__Minute).zfill(2) + ":" + str(self.__Seconds).zfill(2)
    
    def getTimeMinute(self):
        return self.__Hour * 60 + self.__Minute

    def getLane(self):
        return self.__Lane

    def getPlate(self):
        return self.__Plate
    
    def getBrightness(self):
        return self.__Brightness
        
    def getListData(self):
        return [self.__Path, self.__Fmt, 
                self.__Year, self.__Month, self.__Day, 
                self.__Hour, self.__Minute, self.__Seconds, 
                self.__Lane, self.__Plate, self.__Brightness]

# Data Proc
def SaveAnalysisData(Objects):
    print("Save Analysis Data...", end=' ')

    csv_file = fPATH + ".csv"
    data = [["File Name", "Format", 
             "Year", "Month", "Day", 
             "Hour", "Minute", "Seconds", 
             "Lane", "Plate", "Brightness"]]

    for obj in Objects:
        data.append(obj.getListData())

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Done")

def LoadAnalysisData():
    Objects = []
    if(os.path.exists(fPATH + ".csv")):
        with open(fPATH + ".csv", "r") as file:
            reader = list(csv.reader(file))
            nImg = len(glob.glob(fPATH + "\\*.jpg"))
            nCSV = (len(reader) - 1)
            if(nImg != nCSV): 
               print("n Images : ", str(nImg), "n CSV Lines : ", str(nCSV))
               Objects = LoadAnalysisImg()
               return Objects
            else:
                print("Load CSV File...", end=' ')
                for line in reader:
                    if(line[0] == 'File Name'): continue
                    obj = AVIClass()
                    obj.setFromList(line)
                    Objects.append(obj)
                print("Done")
                return Objects
    
    Objects = LoadAnalysisImg()
    return Objects

def LoadAnalysisImg():
    print("Load Image Files...", end=' ')

    FileList = os.listdir(fPATH)
    Objects = []
    for _File in FileList:
        vFmt = _File[-4:]
        if vFmt == ".jpg":
            obj = AVIClass()
            obj.setFromImg(_File)
            Objects.append(obj)

    print("Done")

    SaveAnalysisData(Objects)
    
    return Objects

# Plot
def ShowPlot(Objects):

    if(len(Objects) <= 0):
        return
    
    nLane = 4
    nLine = 3
    fig_, axe_ = plt.subplots(nLine, nLane + 1, figsize=set_figsize_in_pixels(2560, 1440))
    fig_.subplots_adjust(left=0.07, right=0.95, top=0.9, bottom=0.08, hspace=0.6, wspace=0.3)

    BrightnessPlot(axe_, Objects, nLane=nLane)

    PlatePlot(axe_, Objects, nLane=nLane)

    BrightnessAveragePlot(axe_, Objects, nLane=nLane)

    lpath = fPATH.split('\\')
    fig_.suptitle(lpath[len(lpath)-1])

    save_filename = lpath[len(lpath) - 1] + '.png'
    fig_.savefig(save_filename, dpi=300, bbox_inches='tight')
    # plt.show()

def set_figsize_in_pixels(width_px, height_px, dpi=100):
    # 픽셀을 인치로 변환하여 figsize 설정
    width_inch = width_px / dpi
    height_inch = height_px / dpi
    return (width_inch, height_inch)

def BrightnessPlot(axe_, Objects, plotloc=0, nLane=3):
    colors = ['#FF0000', '#00FF00', '#0000FF', '#00FFFF', '#FF00FF', '#FFFF00']
    BrightnessList = []
    for lane in range(nLane):
        blist = [0] * 256
        BrightnessList.append(blist)

    for obj in Objects:
        BrightnessList[int(obj.getLane())-1][obj.getBrightness()] += 1

    # ymax = max(max(BrightnessList)) * 1.1
    ymax = 230

    for n in range(0, nLane):
        axe_[plotloc, n].set_title( "Lane " + str(n+1))
        axe_[plotloc, n].plot(range(0, 256, 1), BrightnessList[n], color=colors[n])
        axe_[plotloc, n].set_xticks(range(0, 256, 50))
        axe_[plotloc, n].set_xlabel('Brightness')
        axe_[plotloc, n].set_ylabel('Number of Cars')
        axe_[plotloc, n].set_ylim(0, ymax)
        axe_[plotloc, n].grid(True, 'both')

    axe_[plotloc, nLane].set_title('ALL Lane')
    for n in range(0, nLane):
        axe_[plotloc, nLane].plot(range(0, 256, 1), BrightnessList[n], color=colors[n])
    axe_[plotloc, nLane].set_xticks(range(0, 256, 50))
    axe_[plotloc, nLane].set_xlabel('Brightness')
    axe_[plotloc, nLane].set_ylabel('Number of Cars')
    axe_[plotloc, nLane].set_ylim(0, ymax)
    axe_[plotloc, nLane].grid(True, 'both')

def PlatePlot(axe_, Objects, TimeStep = 10, plotloc=1, nLane=3):
    TimeTicks = range(0, 24*60 + 1, TimeStep)

    TimeSpan = []
    nSkip = int(24 / (TimeStep / 10))
    cSkip = 0
    for _t in TimeTicks:
        if(cSkip % nSkip == 0): # TimeStep : 1/cSkip = 60 : 1/4
            TimeSpan.append('{0:02d}:{1:02d}'.format(int(_t / 60),  _t - int(_t / 60) * 60))
        else:
            TimeSpan.append("")
        cSkip += 1

    nPlate = []
    nEmptyPlate = []
    for lane in range(nLane):
        plist = [0] * len(TimeSpan)
        mlist = [0] * len(TimeSpan) 
        nPlate.append(plist)
        nEmptyPlate.append(mlist)

    for obj in Objects:
        idx = int(obj.getTimeMinute() / TimeStep)
        nPlate[int(obj.getLane()) - 1][idx] += 1
        if(obj.getPlate() == ""):
            nEmptyPlate[int(obj.getLane()) - 1][idx] += 1

    # ymax = max(max(nPlate)) * 1.1
    ymax = 120

    for n in range(0, nLane):
        axe_[plotloc, n].plot(range(len(TimeSpan)), nPlate[n], color='skyblue')
        axe_[plotloc, n].fill_between(range(len(TimeSpan)), nPlate[n], color='skyblue')
        axe_[plotloc, n].plot(range(len(TimeSpan)), nEmptyPlate[n], color='orange')
        axe_[plotloc, n].fill_between(range(len(TimeSpan)), nEmptyPlate[n], color='orange')
        axe_[plotloc, n].set_xticks(range(len(TimeSpan)))
        axe_[plotloc, n].set_xticklabels(TimeSpan)
        axe_[plotloc, n].set_xlabel('Time')
        axe_[plotloc, n].set_ylabel('Number of Cars')
        axe_[plotloc, n].set_ylim(0, ymax)
        axe_[plotloc, n].grid(True, 'minor')

    snPlate = [sum(column) for column in zip(*nPlate)]
    snEmpty = [sum(column) for column in zip(*nEmptyPlate)]
    axe_[plotloc, nLane].plot(range(len(TimeSpan)), snPlate, color='skyblue')
    axe_[plotloc, nLane].fill_between(range(len(TimeSpan)), snPlate, color='skyblue')
    axe_[plotloc, nLane].plot(range(len(TimeSpan)), snEmpty, color='orange')
    axe_[plotloc, nLane].fill_between(range(len(TimeSpan)), snEmpty, color='orange')
    axe_[plotloc, nLane].set_xticks(range(len(TimeSpan)))
    axe_[plotloc, nLane].set_xticklabels(TimeSpan)
    axe_[plotloc, nLane].set_xlabel('Time (' + 
                                    str( float(10000 - int((sum(snEmpty) / sum(snPlate)) * 10000)) / 100 ) + 
                                    '%)')
    axe_[plotloc, nLane].set_ylabel('Number of Cars')
    axe_[plotloc, nLane].set_ylim(0, nLane*0.8*ymax)
    axe_[plotloc, nLane].grid(True, 'minor')

def BrightnessAveragePlot(axe_, Objects, TimeStep = 10, plotloc=2, nLane=3):
    colors = ['#FF0000', '#00FF00', '#0000FF', '#00FFFF', '#FF00FF', '#FFFF00']
    TimeTicks = range(0, 24*60 + 1, TimeStep)

    TimeSpan = []
    nSkip = int(24 / (TimeStep / 10))
    cSkip = 0
    for _t in TimeTicks:
        if(cSkip % nSkip == 0): # TimeStep : 1/cSkip = 60 : 1/4
            TimeSpan.append('{0:02d}:{1:02d}'.format(int(_t / 60),  _t - int(_t / 60) * 60))
        else:
            TimeSpan.append("")
        cSkip += 1

    nCar = []
    sBrightness = []
    aBrightness = []
    for lane in range(nLane):
        nCar.append([0] * len(TimeSpan))
        sBrightness.append([0] * len(TimeSpan))
        aBrightness.append([0] * len(TimeSpan))

    for obj in Objects:
        idx = int(obj.getTimeMinute() / TimeStep)
        nCar[int(obj.getLane()) - 1][idx] += 1
        sBrightness[int(obj.getLane()) - 1][idx] += obj.getBrightness()

    for n in range(0, nLane):
        for idx in range(0, len(TimeSpan)):
            if(nCar[n][idx] != 0):
                aBrightness[n][idx] = sBrightness[n][idx] / nCar[n][idx]

    # ymax = max(max(aBrightness)) * 1.1
    ymax = 120

    for n in range(0, nLane):
        # print(vBrightness[n], nCar[n])
        axe_[plotloc, n].plot(range(len(TimeSpan)), aBrightness[n], color=colors[n])
        axe_[plotloc, n].set_xticks(range(len(TimeSpan)))
        axe_[plotloc, n].set_xticklabels(TimeSpan)
        axe_[plotloc, n].set_xlabel('Time')
        axe_[plotloc, n].set_ylabel('Brightness Average')
        axe_[plotloc, n].set_ylim(0, ymax)
        axe_[plotloc, n].grid(True, 'minor')

    for n in range(0, nLane):
        axe_[plotloc, nLane].plot(range(len(TimeSpan)), aBrightness[n], color=colors[n])
    axe_[plotloc, nLane].set_xticks(range(len(TimeSpan)))
    axe_[plotloc, nLane].set_xticklabels(TimeSpan)
    axe_[plotloc, nLane].set_xlabel('Time')
    axe_[plotloc, nLane].set_ylabel('Brightness Average')
    axe_[plotloc, nLane].set_ylim(0, ymax)
    axe_[plotloc, nLane].grid(True, 'minor')

# Main Script
exePATH = os.getcwd()
dirList = os.listdir(exePATH)

for _dir in dirList:
    fPATH = os.path.join(exePATH, _dir)
    print(fPATH)
    if os.path.isdir(fPATH):
        ShowPlot(LoadAnalysisData())