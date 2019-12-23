import cv2
import numpy as np

image = cv2.imread('C:/pdg/crawling/lena.png')
image = image.astype(np.float32) / 255
print('Shape: ', image.shape)
print('Data type: ', image.dtype)
gray = cv2.cvtColor((image, cv2.COLOR_BGR2GRAY))
cv2.imshow('image', gray)
cv2.waitKey()
cv2.destroyAllWindows()