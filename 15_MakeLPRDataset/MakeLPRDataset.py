import os
import numpy as np
import cv2

sPath = '#DataSet\\'

cList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
        '가', '거', '고', '구', '나', '너', '노', '누', 
        '다', '더', '도', '두', '라', '러', '로', '루', 
        '마', '머', '모', '무', '바', '버', '보', '부', 
        '다', '더', '도', '두', '사', '서', '소', '수', 
        '아', '어', '오', '우', '자', '저', '조', '주', 
        '하', '허', '호',]

uList = []


if not os.path.isdir(sPath):
    os.makedirs(sPath)

for char_ in cList:
    uList.append(ord(char_))

for ii in range(0, len(cList)):
    dPath = str(cList[ii]) + "_" + str(uList[ii])
    if(os.path.isdir(dPath)):
        fList = os.listdir(dPath)
#         iIdx = 1
        for iName in fList:
            print(dPath + "\\" + iName)
            Img = cv2.imread(dPath + "\\" + iName)
            
            cv2.imshow(Img)
            cv2.waitKey(1)
#             # print(dPath + str(cList[ii]) + '\\' + iPath)
#             print(tmpPath + str(uList[ii]) + ' (' + str(iIdx) + ').jpg')

#             print(Img)
#             cv2.imwrite(tmpPath + str(uList[ii]) + ' (' + str(iIdx) + ').jpg', Img)
            
#             iIdx+=1
#             for tx in [-5, 5]:
#                 for ty in [-5, 5]:
#                     M = np.float32([[1, 0, tx], [0, 1, ty]])
#                     tImg = cv2.warpAffine(Img, iIdx, (Img.shape[1], Img.shape[0]))
#                     cv2.imwrite(tmpPath + str(uList[ii]) + ' (' + str(iIdx) + ').jpg', tImg)
#                     iIdx+=1

#             for r in [-2, -1, 1, 2]:
#                 (h, w) = Img.shape[:2]
#                 (cX, cY) = (w / 2, h / 2)
#                 M = cv2.getRotationMatrix2D((cX, cY), r, 1.0)
#                 rImg = cv2.warpAffine(Img, iIdx, (Img.shape[1], Img.shape[0]))
#                 cv2.imwrite(tmpPath + str(uList[ii]) + ' (' + str(iIdx) + ').jpg', rImg)
#                 iIdx+=1
            