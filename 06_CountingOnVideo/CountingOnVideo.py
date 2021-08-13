import cv2
from pytictoc import TicToc

def CountingCSV(cStream, wData):
    cStream.write(Time.strip("\n"))
    cStream.write(',')
    cStream.write(wData)
    cStream.write('\n')
    return 0

def kEvent(iKey, cStream, tFrame, iESC):
    if(iKey == 27):
        iESC = 0
    elif(iKey == ord('a') or iKey == ord('A')):
        CountingCSV(cStream, '1')
    elif(iKey == ord('s') or iKey == ord('S')):
        CountingCSV(cStream, '2')
    elif(iKey == ord('d') or iKey == ord('D')):
        CountingCSV(cStream, '3')
    elif(iKey == ord('f') or iKey == ord('F')):
        CountingCSV(cStream, '4')
    elif(iKey == ord('j') or iKey == ord('J')):
        CountingCSV(cStream, '5')
    elif(iKey == ord('k') or iKey == ord('K')):
        CountingCSV(cStream, '6')
    elif(iKey == ord('l') or iKey == ord('L')):
        CountingCSV(cStream, '7')
    elif(iKey == ord(';')):
        CountingCSV(cStream, '8')
    elif(iKey == ord('+')):
        tFrame = tFrame - 3
        if tFrame <= 0:
            tFrame = 3
    elif(iKey == ord('-')):
        tFrame = tFrame + 3
    elif(iKey == ord(' ')):
        pp = -1
        while pp == -1:
            pp = cv2.waitKey()

    return iESC, tFrame

t = TicToc()

vFilename = "(눈영상)2018.01.30.174800"
vStream = cv2.VideoCapture(vFilename + ".mp4")
iStream = open(vFilename + ".idx", 'r')
cStream = open(vFilename + ".csv", 'w')

SumOfTime = 0
nFrame = 0

iData = iStream.readlines()

tFrame = 33
iKey = -1
iESC = 1

while iESC:
    iData_ = iData[int(vStream.get(cv2.CAP_PROP_POS_FRAMES))]
    idx, Time = iData_.split(",")

    ret, frame = vStream.read()
    cv2.imshow("VideoFrame", frame)

    iKey = cv2.waitKey(tFrame)

    [iESC, tFrame] = kEvent(iKey, cStream, tFrame, iESC)
    


vStream.release()
iStream.close()
cStream.close()
cv2.destroyAllWindows()