import sys
import os
import cv2
from moviepy.editor import *

FileList = os.listdir()

for file_ in FileList:
    vFmt = file_[-4:]
    if(vFmt == ".mp4" or vFmt == ".mkv" or vFmt == ".avi"):
        vClip = VideoFileClip(file_)
        vFPS = vClip.fps
        print(file_ + ' to ' + file_[:-4] + '.gif')
        vClip.write_gif(file_[:-4] + '.gif', fps=vFPS*0.70)


# write_gif(self, filename, fps=None, program='imageio', opt='nq', fuzz=1, verbose=True, loop=0, dispose=False, colors=None, tempfiles=False, logger='bar')