import cv2
import numpy as np
import random

# Add salt and pepper noise to image
def sp_noise(src,prob):
    output = np.zeros(src.shape,np.uint8)
    thres = 1 - prob 
    for i in range(src.shape[0]):
        for j in range(src.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = src[i][j]
    return output

src = cv2.imread('images/lena.png') 
noise_img = sp_noise(src,0.05)
cv2.imwrite('images/sp_noise.jpg', noise_img)
print("End Salt and pepper")

### Negative
m = src.copy()
img_neg = 255 - m
cv2.imwrite('images/Negative.png',img_neg)
print("End Negative")

