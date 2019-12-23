import cv2
import numpy as np

image = cv2.imread('C:/pdg/crawling/lena.png')
print('Shape: ', image.shape)
print('Data type: ', image.dtype)

image = image.astype(np.float32) / 255
print('Shape', image.shape)
print('Data type', image.dtype)

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()