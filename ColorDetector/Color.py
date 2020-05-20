import cv2
import numpy as np

src = cv2.imread("images/imagen.png")
exit = np.uint16(src)
# Defining the range of red color (the dark and light red)
#dark red
hsv_min_red = np.array([0, 100, 100]) 
hsv_max_red = np.array([10, 255, 255])
#light red
hsv_min_red2 = np.array([160, 100, 100]) 
hsv_max_red2 = np.array([179, 255, 255])

# Applying the Gaussian smoothing function
gauss = cv2.GaussianBlur(src, (5,5), 0)
cv2.imwrite("images/Smooth.jpg", gauss)
# Convert to HSV to get as much background as possible
hsv_red = cv2.cvtColor(gauss, cv2.COLOR_BGR2HSV)
cv2.imwrite("images/HSV.jpg", hsv_red)
# Create the masks for the red color
dark_red = cv2.inRange(hsv_red, hsv_min_red, hsv_max_red)
light_red = cv2.inRange(hsv_red, hsv_min_red2, hsv_max_red2)

# Adding the red masks
masks_red = cv2.add(dark_red, light_red)
res = cv2.bitwise_and(src, src, exit, masks_red)

# Showing the resulting images
cv2.imshow("images/Dark red images", dark_red)
cv2.imshow("Light red images", light_red)
cv2.imshow("Tones of red", masks_red)
cv2.imshow("Exit", res)

print("======END=======")
