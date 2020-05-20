import cv2
import numpy as np

src = cv2.imread("images/image.png")
exit_src = np.uint16(src)

# Defining the range of the colors (the dark and light red, blue and green)
#dark red
hsv_min_red = np.array([0, 100, 100]) 
hsv_max_red = np.array([10, 255, 255])
#light red
hsv_min_red2 = np.array([160, 100, 100]) 
hsv_max_red2 = np.array([179, 255, 255])
#blue
hsv_min_blue = (100,65,75)
hsv_max_blue = (130,255,255)
#green
hsv_min_green = (49,50,50)
hsv_max_green = (107,255,255)

# Applying the Gaussian smoothing function
gauss = cv2.GaussianBlur(src, (5,5), 0)
cv2.imwrite("images/Smooth.jpg", gauss)

# Convert to HSV to get as much background as possible
hsv_color = cv2.cvtColor(gauss, cv2.COLOR_BGR2HSV)
cv2.imwrite("images/HSV.jpg", hsv_color)

# Create the masks for the red color
dark_red = cv2.inRange(hsv_color, hsv_min_red, hsv_max_red)
light_red = cv2.inRange(hsv_color, hsv_min_red2, hsv_max_red2)
blue = cv2.inRange(hsv_color, hsv_min_blue, hsv_max_blue)
green = cv2.inRange(hsv_color, hsv_min_green, hsv_max_green)

# Adding the red masks
masks_red = cv2.add(dark_red, light_red)
res_red = cv2.bitwise_and(src, src, exit_src, masks_red)

# Getting the blue and red masks
masks_rb = cv2.add(masks_red, blue)
res_rb = cv2.bitwise_and(src, src, exit_src, masks_rb)

# Showing the resulting images
cv2.imshow("images/Dark red images", dark_red)
cv2.imshow("Light red images", light_red)
cv2.imshow("Tones of red", masks_red)
cv2.imshow("Exit RED", res_red)

cv2.imshow("Exit RED-BLUE", res_rb)

print("======END=======")

