import cv2
import numpy as np

img = cv2.imread("../../Picture/girl.png", 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

newImg = np.zeros(imgInfo, np.uint8)
for i in range(0, height):
    for j in range(0, width):
        newImg[i, j] = img[i, j]

cv2.imshow("newImg", newImg)
cv2.waitKey(0)