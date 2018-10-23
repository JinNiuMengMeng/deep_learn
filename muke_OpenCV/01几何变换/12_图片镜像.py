import numpy as np
import cv2

img = cv2.imread("../../Picture/water.png", 1)
imgInfo = img.shape
print("imgInfo.shape:", imgInfo)
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow("src", img)

# 水平镜像
newImg_Level = np.zeros((height, width * 2, 3), np.uint8)
print("newImg_Level.shape:", newImg_Level.shape)
newImgInfo = newImg_Level.shape
newHeight = newImgInfo[0]
newWidth = newImgInfo[1]

for i in range(0, height):
    for j in range(0, width):
        newImg_Level[i, j] = img[i, j]
    for k in range(width - 1, 0, -1):
        newImg_Level[i, width + (width - k)] = img[i, k]
cv2.imshow("Level_image", newImg_Level)

# 垂直镜像
newImg_Vertical = np.zeros((height * 2, width, 3), np.uint8)
print("newImg_Vertical.shape:", newImg_Vertical.shape)
vertical_img_info = newImg_Vertical.shape
vertical_img_height = newImg_Vertical[0]
vertical_img_weight = newImg_Vertical[1]

for i in range(0, height):
    for j in range(0, width):
        newImg_Vertical[i, j] = img[i, j]

for m in range(height, height * 2):
    for n in range(0, width):
        newImg_Vertical[m, n] = img[height * 2 - m -1, n]

cv2.imshow("newImg_Vertical", newImg_Vertical)
cv2.waitKey(0)
