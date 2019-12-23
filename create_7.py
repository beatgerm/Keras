import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:/pdg/crawling/lena.png',0)
# image = image.astype(np.float32) / 255

otsu_thr, otsu_mask = cv2.threshold(image, -1,1,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('Estimated thre')



plt.figure(figsize=(6,3))
plt.subplot(121)
plt.axis('off')
plt.title('orginal')
plt.imshow(image, cmap = 'gray')
plt.subplot(122)
plt.axis('off')
plt.title('Otsu threshold')
plt.imshow(otsu_mask, cmap = 'gray')
plt.tight_layout()
plt.show()
