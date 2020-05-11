import cv2  
import time 

image = cv2.imread("test.png") 
scale_percent = 70
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA) 
cv2.imwrite('new1.png',image)
image = cv2.copyMakeBorder(image, 100, 100, 105, 100, cv2.BORDER_CONSTANT) 
cv2.imwrite('new.png',image)
