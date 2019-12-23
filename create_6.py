import cv2
import numpy as np

image = cv2.imread('C:/pdg/crawling/lena.png',0)
image = image.astype(np.float32) / 255
gamma = 0.5
corrected_image = np.power(image, gamma)

cv2.imshow('image', image)
cv2.imshow('corrected_image', corrected_image)
cv2.waitKey()
cv2.destroyAllWindows()