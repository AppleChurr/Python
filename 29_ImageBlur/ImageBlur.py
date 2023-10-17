import os
import shutil
import cv2

File_PATH = os.getcwd()+"\\"
Ext = [".jpg", ".bmp", ".png"] 

Dest_Folder = File_PATH + "BluredImg\\"

if not(os.path.isdir(Dest_Folder)):
    os.makedirs(os.path.join(Dest_Folder))

FileList = os.listdir()

for file_ in FileList:
    vFmt = file_[-4:]
    if any(vFmt == _ext for _ext in Ext):
        vFileName = file_[:-4]

        if os.path.exists(vFileName + ".txt"):

            vCapture = cv2.imread(file_)

            ksize = (25, 25)  # 커널 크기 설정, (5, 5)는 예시
            sigmaX = 0  # X 방향의 가우시안 커널 표준 편차
            vCapture = cv2.GaussianBlur(vCapture, ksize, sigmaX)

            cv2.imwrite(Dest_Folder + vFileName + "b.jpg", vCapture)

            shutil.copy2(vFileName + ".txt", Dest_Folder + vFileName + "b.txt")

            print(vFileName)

        else:
            continue

