import cv2
import matplotlib.pyplot as plt

# Charger l'image
image = cv2.imread('..\coins.png', cv2.IMREAD_GRAYSCALE)  # Charger l'image en niveaux de gris
cv2.imshow('Image Originale', image)
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Afficher l'histogramme
plt.plot(histogram)
plt.title('Histogramme de l\'image')
plt.xlabel('Intensité des pixels')
plt.ylabel('Nombre de pixels')
plt.show()

# Choisir un seuil
thresholdValue = 87
maxVal = 255
# Appliquer le seuillage
_, binary_image = cv2.threshold(image, thresholdValue, maxVal, cv2.THRESH_BINARY)
# Afficher l'image binaire
cv2.imshow('Image Binaire', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
