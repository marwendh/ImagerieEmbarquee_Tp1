import cv2
import matplotlib.pyplot as plt
import numpy as np
# Charger l'image
path1 = r'..\pout.tif'
img1 = cv2.imread(path1,cv2.IMREAD_GRAYSCALE)

plt.hist(img1.ravel(), bins=256, range=[0,256])
plt.show()
imgEq=cv2.equalizeHist(img1)

plt.hist(imgEq.ravel(), bins=256, range=[0,256])
plt.show()

matrix1=np.ones((img1).shape)* 1.2
matrix2=np.ones((img1).shape)* 0.5
eclair=np.uint8(np.clip(cv2.multiply(np.float64(img1),matrix1),0,255))
sombre=np.uint8(np.clip(cv2.multiply(np.float64(img1),matrix2),0,255))
cv2.imshow("eclair",eclair)
cv2.imshow("sombre",sombre)

imgSombreContrast=cv2.equalizeHist(sombre)
cv2.imshow("sombreEnhanced",imgSombreContrast)


cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)