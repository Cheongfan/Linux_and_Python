import cv2
img = cv2.imread("image/1.png")
imgCropped = img[0:150,0:300]
shape = imgCropped.shape
print(shape[0])
imgCropped = cv2.resize(imgCropped,(shape[0]*14//4,shape[1]))
cv2.imshow("Image cropped",imgCropped)
cv2.imshow("Image",img)
cv2.waitKey(0)
