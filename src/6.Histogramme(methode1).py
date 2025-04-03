import cv2
import matplotlib.pyplot as plt

# Charger l'image
path1 = r'..\pout.tif'
img1 = cv2.imread(path1)  # Convertir en niveaux de gris

histB=cv2.calcHist([img1], [0], None, [256], [0,256])
histG=cv2.calcHist([img1], [1], None, [256], [0,256])
histR=cv2.calcHist([img1], [2], None, [256], [0,256])

plt.plot(histB, color='b')
plt.show()
plt.plot(histG, color='g')
plt.show()
plt.plot(histR, color='r')
plt.show()
plt.plot(histB, color='b')
plt.plot(histG, color='g')
plt.plot(histR, color='r')
plt. title('Image Histogram For  Channels BFG')
plt.show()