import cv2
import numpy as np
from pytictoc import TicToc

img = np.zeros((1280, 720, 1), np.uint8)

contours = [np.array( [[127, 245], [190, 230], [280, 245], [280, 650], [127, 650]], np.int32)]
img = cv2.fillPoly(img, contours, (255))

size = np.size(img)
skel = np.zeros(img.shape, np.uint8)

element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))

t = TicToc()

t.tic()

while True:
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
    temp = cv2.subtract(img, open)
    eroded = cv2.erode(img, element)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()

    if cv2.countNonZero(img)==0:
        break

t.toc()

# Displaying the final skeleton
cv2.imshow("Skeleton",skel)
cv2.waitKey(0)
cv2.destroyAllWindows()