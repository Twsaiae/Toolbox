import cv2
import numpy as np

src = 'k1.png'
img = cv2.imread(src, -1)
h, w = img.shape
blank = np.zeros_like(img, dtype=np.uint8)

for y in range(h):
    for x in range(w):
        print(blank[y][x])
        if blank[y][x] >= 156:
            blank[y][x] = 255
cv2.imwrite('k2.png', blank)
