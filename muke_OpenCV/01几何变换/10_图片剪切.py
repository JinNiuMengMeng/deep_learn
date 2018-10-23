import cv2

img = cv2.imread('../../Picture/water.jpg', 1)
imgInfo = img.shape
print("imgInfo:", imgInfo)
dst = img[100:170, 100:361]  # 高度不变,宽度范围取100-300
print("dstInfo:", dst.shape)
cv2.imshow("image", dst)
cv2.imshow("src", img)
cv2.waitKey(0)
