import os
import matplotlib.pyplot as plt

def PrintTraffics(DayList, Traffics):
    # Print
    for _day in DayList:
        print("\t" + _day[-5:], end='')
    print('')

    tIdx = 0
    for _tList in Traffics:
        print(TimeTicks[tIdx], end='\t')
        for _traffic in _tList:
            print(str(_traffic), end="\t")
        print('')
        tIdx += 1

def PrintLastDay(DayList, Traffics):
    # Print
    tIdx = 0
    print("\t" + DayList[-1])
    for _tList in Traffics:
        print(TimeTicks[tIdx], end='\t')
        print(str(_tList[-1]), end="\t")
        print('')
        tIdx += 1

def ShowPlot(DayList, Traffics, TimeTicks):

    hh = int(LastTime[0:2])
    mm = int(LastTime[3:5])
    ss = int(LastTime[6:8])

    t = hh * 60 + mm

    Last24H = [0] * len(xTicks)

    for _h in range(0, xTicks.index( int(t / TimeStep) + 1)):
        Last24H[_h] = Traffics[_h][DayList.index(LastDay)]

    for _h in range(xTicks.index( int(t / TimeStep) + 1), len(xTicks)):
        Last24H[_h] = Traffics[_h][DayList.index(LastDay) - 1]

    LogAvg = [0] * len(xTicks)
    for _h in range(0, len(xTicks)):
        _list = Traffics[_h][0:DayList.index(LastDay)]
        print(_list)
        _avg = sum(_list) / len(_list)
        LogAvg[_h] = _avg

    # Plot Data
    PlotArray = []
    for _List in Traffics:
        PlotArray.append(_List[:-1])

    TimeSpan = []
    for _t in TimeTicks:
        TimeSpan.append( '{0:02d}:{1:02d}'.format(int(_t / 60),  _t - int(_t / 60) * 60))

    PrintTraffics(DayList[:-1], PlotArray)

    fig_, axe_ = plt.subplots()
    axe_.set_title('Traffic Information 24H')
    axe_.boxplot(PlotArray)
    axe_.plot(xTicks, Last24H, 'r-o')
    axe_.plot(xTicks, LogAvg, 'b--')
    axe_.grid(True, 'both')

    plt.xticks(xTicks, TimeSpan, rotation=45)
    plt.show()

fPATH = os.getcwd()+"\\"
FileList = os.listdir()

IndexDay = 1
IndexTime = 2

TimeStep = 20

TimeTicks = range(0, 24*60, TimeStep)
xTicks = range(1, (len(TimeTicks)+1))

DayList = []

# Day Set
for _File in FileList:
    vFmt = _File[-4:]
    if vFmt == ".csv":
        cFile = open(fPATH + _File, 'r')
        toDay = ''
        for lData in cFile.readlines():
            lData = lData.replace("\r", "")
            lData = lData.replace("\n", "")
            lData = lData.replace(" ", "")
            _Data = lData.split(",")

            if toDay == '':
                toDay = _Data[IndexDay]
                DayList.append(toDay)
            else:
                break

Traffics = [[0 for j in range(len(DayList))] for i in range(len(xTicks))]

# Get Data to Array
LastDay = ''
LastTime = ''
for _File in FileList:
    vFmt = _File[-4:]
    if vFmt == ".csv":
        cFile = open(fPATH + _File, 'r')
        for lData in cFile.readlines():
            lData = lData.replace("\r", "")
            lData = lData.replace("\n", "")
            lData = lData.replace(" ", "")
            _Data = lData.split(",")

            Time = _Data[IndexTime]
            Day = _Data[IndexDay]

            hh = int(Time[0:2])
            mm = int(Time[3:5])
            ss = int(Time[6:8])

            t = hh * 60 + mm

            Traffics[xTicks.index( int(t / TimeStep) + 1 )][DayList.index(Day)] += 1

            LastDay = Day
            LastTime = Time

# PrintTraffics(DayList, Traffics)

# PrintLastDay(DayList, Traffics)

ShowPlot(DayList, Traffics, TimeTicks)