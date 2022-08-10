import numpy as np
import cv2

def MakeContourImg(GrayImg, RGBImg):

    BImg, GImg, RImg = cv2.split(RGBImg)

    _, BinImg = cv2.threshold(GrayImg, 1, 255, cv2.THRESH_BINARY)

    for ii in range(0, 4):
        BinImg = cv2.morphologyEx(BinImg, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    
    contours, _ = cv2.findContours(BinImg, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    height, width = GrayImg.shape

    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)

    i = 0
    for c in contours:
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])
        i = i+1

    for i in range(len(contours)):
        if boundRect[i][2] >= 30 and boundRect[i][3] >= 50:
            cv2.rectangle(BImg, (int(boundRect[i][0]), int(boundRect[i][1])), \
                (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), 0, 5)
            cv2.rectangle(GImg, (int(boundRect[i][0]), int(boundRect[i][1])), \
                (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), 0, 5)
            cv2.rectangle(RImg, (int(boundRect[i][0]), int(boundRect[i][1])), \
                (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), 255, 5)

    BGRImg = cv2.merge((BImg, GImg, RImg))

    return BGRImg

# cap = cv2.VideoCapture('D:\\21_Labeling\\03_교차로\\교차로_주간.mp4')
# cap = cv2.VideoCapture('D:\\21_Labeling\\02_악천후\\(눈영상)2018.01.30.174800.mp4')
# cap = cv2.VideoCapture('\\\\192.168.0.253\\Shared2\\[20211007] 대구ATMS 테스트영상\\vlc-record-2021-10-07-11h43m56s-rtsp___192.168.101.214_video1-.mp4')

# cap = cv2.VideoCapture('\\\\192.168.0.148\\i\\인포영상\\GOP VIDEO\\군영상\\나방 데모영상\\나방-1.avi') # 철책 나방 iLSBP
# cap = cv2.VideoCapture('\\\\192.168.0.148\\i\\인포영상\\GOP VIDEO\\보고서용 동영상\\CCD-4.avi') # 해안 iKNN
# cap = cv2.VideoCapture('\\\\192.168.0.148\\i\\인포영상\\해상탐지\\090514_1114\\[0][00]_05_14 11_14 23.avi') # 카메라가 이동 Mog2
cap = cv2.VideoCapture('\\\\192.168.0.148\\i\\인포영상\\군\\[1][01]_02_09 19_31 18.avi') # 육군 카메라 회전 iLSBP




# cap = cv2.VideoCapture('\\\\192.168.0.148\\e\\[20200900] 청주 ITS\\20201212_청주 녹화 영상\\CCTV 솔밭공원 사거리 녹화 영상\\D01_20201208145622.mp4')
# cap = cv2.VideoCapture('\\\\192.168.0.148\\i\\Traning_data\\영상자료\\15_수원_2차수집\\법원사거리 2000-2115.mp4')
# cap = cv2.VideoCapture('\\\\192.168.0.148\\i\\Traning_data\\영상자료\\25_수원_12차수집\\관터사거리(야간).mp4')

fps = cap.get(cv2.CAP_PROP_FPS) # 프레임 수 구하기
delay = int(1000/fps)
# 배경 제거 객체 생성 --- ①


bgsGMG = cv2.bgsegm.createBackgroundSubtractorGMG(5)
bgsLSBP = cv2.bgsegm.createBackgroundSubtractorLSBP()
bgsGSOC = cv2.bgsegm.createBackgroundSubtractorGSOC()

bgsKNN = cv2.createBackgroundSubtractorKNN(500, 400, False)
bgsMOG2 = cv2.createBackgroundSubtractorMOG2(5000, 8, False)

while cap.isOpened():
    ret, iOrigin = cap.read()
    if not ret:
        break
    # 배경 제거 마스크 계산 --- ②
    # cv2.imshow('img',iOrigin)

    iGMG = bgsGMG.apply(iOrigin)
    iLSBP = bgsLSBP.apply(iOrigin)
    iGSOC = bgsGSOC.apply(iOrigin)
    iKNN = bgsKNN.apply(iOrigin)
    iMOG2 = bgsMOG2.apply(iOrigin)

    iGMG = MakeContourImg(iGMG, iOrigin)
    iLSBP = MakeContourImg(iLSBP, iOrigin)
    iGSOC = MakeContourImg(iGSOC, iOrigin)
    iKNN = MakeContourImg(iKNN, iOrigin)
    iMOG2 = MakeContourImg(iMOG2, iOrigin)

    # iShow = cv2.hconcat([iOrigin, iGSOC])

    H1 = cv2.hconcat([iOrigin, iGMG, iLSBP])
    H2 = cv2.hconcat([iGSOC, iKNN, iMOG2])
    iShow = cv2.vconcat([H1, H2])

    cv2.imshow('image', cv2.resize(iLSBP, (1280, 720)))
    # cv2.imshow('image', cv2.resize(iShow, (1280, 720)))

    kk = cv2.waitKey(1)

    if kk & 0xff == 27:
        break
    elif kk & 0xff == 119:
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + 60)
    elif kk & 0xff == 115:
        if cap.get(cv2.CAP_PROP_POS_FRAMES) >= 60:
            cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) - 60)
        else :
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
cap.release()
cv2.destroyAllWindows()
