import numpy as np
import cv2

# cap = cv2.VideoCapture('D:\\21_Labeling\\03_교차로\\교차로_주간.mp4')
cap = cv2.VideoCapture('D:\\21_Labeling\\02_악천후\\(눈영상)2018.01.30.174800.mp4')

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

    # k = np.ones((3,3), np.uint8)
    
    iGMG = bgsGMG.apply(iOrigin)
    iLSBP = bgsLSBP.apply(iOrigin)
    iGSOC = bgsGSOC.apply(iOrigin)
    iKNN = bgsKNN.apply(iOrigin)
    iMOG2 = bgsMOG2.apply(iOrigin)

    iGMG = cv2.merge((iGMG, iGMG, iGMG))
    iLSBP = cv2.merge((iLSBP, iLSBP, iLSBP))
    iGSOC = cv2.merge((iGSOC, iGSOC, iGSOC))
    iKNN = cv2.merge((iKNN, iKNN, iKNN))
    iMOG2 = cv2.merge((iMOG2, iMOG2, iMOG2))

    H1 = cv2.hconcat([iOrigin, iGMG, iLSBP])
    H2 = cv2.hconcat([iGSOC, iKNN, iMOG2])
    iShow = cv2.vconcat([H1, H2])

    cv2.imshow('image', cv2.resize(iShow, (1280, 720)))

    # ret, fgmask = cv2.threshold(fgmask, 1, 255, cv2.THRESH_BINARY)

    
    # for ii in range(0, 4):
    #     fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,k)
    
    # contours, _ = cv2.findContours(fgmask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # height, width, channel = frame.shape
    # drawing = np.zeros((height, width), dtype=np.uint8)

    # contours_poly = [None]*len(contours)
    # boundRect = [None]*len(contours)

    # i = 0
    # for c in contours:
    #     contours_poly[i] = cv2.approxPolyDP(c, 3, True)
    #     boundRect[i] = cv2.boundingRect(contours_poly[i])
    #     i = i+1

    # for i in range(len(contours)):
    #     if boundRect[i][2] >= 70 and boundRect[i][3] >= 90:
    #         cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
    #             (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), (255, 0, 0), 2)

    # fgmask = cv2.merge((fgmask, fgmask + drawing, fgmask))

    # cv2.imshow('bgsub', fgmask)

    kk = cv2.waitKey(1)

    if kk & 0xff == 27:
        break
    elif kk & 0xff == 119:
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) + 100)
    elif kk & 0xff == 115:
        cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) - 100)
        
cap.release()
cv2.destroyAllWindows()
