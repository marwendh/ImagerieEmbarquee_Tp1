import cv2
import numpy as np
# image path
path = r'..\shape2R.jpg'
# using imread()
imgI = cv2.imread(path)
b,g,r =cv2.split(imgI)

blue=imgI[0:360,0:640,0]
green=imgI[0:360,0:640,1]
red=imgI[0:360,0:640,2]

cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
cv2.imshow('imgI',imgI)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
