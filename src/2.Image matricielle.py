import cv2
from skimage.measure import profile_line
import matplotlib.pyplot as plt

# image path
path = r'..\shape2R.jpg'
# using imread()
img = cv2.imread(path)
# get dimensions of image
dimensions = img.shape
# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
print('Image Dimension : ', dimensions)
print('Image Height: ', height)
print('Image Width: ', width)
print('Number of Channels : ', channels)
# Total number of pixels on the image
sizeImage=img.size
print('number of pixels   : ', sizeImage)
# reading image to be resized
# using imread()
path2 = r'..\Savednature.png'
img2 = cv2.imread(path2)
# resize image then display
img2Res=cv2.resize(img2,(width,height))
cv2.imshow('img2Res', img2Res)
# région d’intérêt
ROI=img[8:100,100:200]
cv2.imshow("partie",ROI)
#Profil d’intensité
p=profile_line(img,(0,0),(height,width))

plt.plot(p)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)