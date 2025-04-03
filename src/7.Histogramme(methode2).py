import cv2
import matplotlib.pyplot as plt

# Charger l'image
path1 = r'..\pout.tif'
img1 = cv2.imread(path1)  # Convertir en niveaux de gris
plt.hist(img1.ravel(), bins=32, range=[0,256])
plt.show()
plt.hist(img1.ravel(), bins=64, range=[0,256])
plt.show()
plt.hist(img1.ravel(), bins=128, range=[0,256])
plt.show()
plt.hist(img1.ravel(), bins=256, range=[0,256])
plt.show()