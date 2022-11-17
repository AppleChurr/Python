import os
import shutil

print("Start ... ")

fPATH = os.getcwd()+"\\"
Ext = [".jpg", ".bmp", ".png"] 

dPATH = fPATH + "FalseNegativeImage\\"

if not(os.path.isdir(dPATH)):
    os.makedirs(os.path.join(dPATH))

FileList = os.listdir()
ii = 0
for _File in FileList:
    print(str(ii) + " / " + str(len(FileList)), end = '\r')
    vFmt = _File[-4:]
    if any(vFmt == _ext for _ext in Ext):
        vFileName = _File[:-4]
        if vFileName[-1] == '_':
            shutil.copy(_File, dPATH)
            os.remove(_File)
    ii += 1

print("")
print("End ... ")