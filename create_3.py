import cv2
import numpy as np

image = cv2.imread('C:/pdg/crawling/lena.png')
image = image.astype(np.float32) / 255
print('Shape: ', image.shape)
print('Data type: ', image.dtype)
image[:,:,[0,2]] = image[:,:,[2,0]]
cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()