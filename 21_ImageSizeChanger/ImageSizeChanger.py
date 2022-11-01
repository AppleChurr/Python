import os
import cv2

File_PATH = os.getcwd()+"\\"
Ext = [".jpg", ".bmp", ".png"] 

Dest_Folder = File_PATH + "ResizeImg\\"

if not(os.path.isdir(Dest_Folder)):
    os.makedirs(os.path.join(Dest_Folder))

FileList = os.listdir()

for file_ in FileList:

    vFmt = file_[-4:]
    if any(vFmt == _ext for _ext in Ext):
        vFileName = file_[:-4]

        print(vFileName)

        vCapture = cv2.imread(file_)
        vCapture = cv2.resize(vCapture, (1280, 720))
        cv2.imwrite(Dest_Folder + vFileName + ".jpg", vCapture)

