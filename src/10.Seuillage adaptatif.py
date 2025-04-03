import cv2
import matplotlib.pyplot as plt


image = cv2.imread('..\coins.png', cv2.IMREAD_GRAYSCALE)

mean_thresholded = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

gaussian_thresholded = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

plt.figure(figsize=(12, 6))

#  l'image originale
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Image originale')
plt.axis('off')

#  méthode de moyenne
plt.subplot(1, 3, 2)
plt.imshow(mean_thresholded, cmap='gray')
plt.title('Seuillage Mean')
plt.axis('off')

# méthode gaussienne
plt.subplot(1, 3, 3)
plt.imshow(gaussian_thresholded, cmap='gray')
plt.title('Seuillage Gaussian')
plt.axis('off')

plt.show()
