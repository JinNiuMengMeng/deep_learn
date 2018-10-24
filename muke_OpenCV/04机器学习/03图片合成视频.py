import cv2

img = cv2.imread('image1.jpg')
imgInfo = img.shape
size = (imgInfo[1], imgInfo[0])
print(size)
videoWrite = cv2.VideoWriter('2.mp4', -1, 5, size)  # 写入对象 1 file name
# 2 编码器 3 帧率 4 size
for i in range(1, 11):
    fileName = 'image' + str(i) + '.jpg'
    img = cv2.imread(fileName)
    videoWrite.write(img)  # 写入方法 1 jpg data
print('end!')
