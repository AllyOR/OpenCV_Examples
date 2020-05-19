import cv2
import numpy as np

src = cv2.imread("images/shapes.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gauss = cv2.medianBlur(gray, 5)
canny = cv2.Canny(gauss, 50, 5)

circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

color1 = (10, 100, 100)
color2 = (100, 200, 0)
for i in circles[0,:]:
    # Draw the borders
    cv2.circle(src, (i[0], i[1]), i[2], color1, 2)
    # Draw the contours
    cv2.circle(src, (i[0], i[1]), 2, color2, 3)

# Show the final image
cv2.imshow("detected circles", src)

cv2.waitKey(0)
print('Done')
cv2.destroyAllWindows()
print("\nFinalized...")  
