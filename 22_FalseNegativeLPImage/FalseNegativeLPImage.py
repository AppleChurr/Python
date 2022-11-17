import os
import shutil

fPATH = os.getcwd()+"\\"
Ext = [".jpg", ".bmp", ".png"] 

dPATH = fPATH + "FalseNegativeImage\\"

if not(os.path.isdir(dPATH)):
    os.makedirs(os.path.join(dPATH))

FileList = os.listdir()

for _File in FileList:
    vFmt = _File[-4:]
    if any(vFmt == _ext for _ext in Ext):
        vFileName = _File[:-4]
        if vFileName[-1] == '_':
            shutil.copy(_File, dPATH)
            os.remove(_File)