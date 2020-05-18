import cv2

src = cv2.imread("images/coins.jpg", 1)
img = cv2.imwrite("images/Original.png",src)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Applying the Gaussian smoothing
gauss = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imwrite("images/Gauss.png", gauss)
thresh = 50 
		
# Detecting the borders with a threshold ( min = 50 & max = 150 )
canny_output = cv2.Canny(gauss, thresh, thresh * 3)

# Show the detected borders with Canny
cv2.imwrite("images/Borders.png", canny_output)

# Find the contours of the image, they are stored in contours
contours,hierarchy = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Show the modified image by the findContours function
cv2.imwrite("images/Modified.png", canny_output)

# Draw the found contours => number of images
print("\nObjects found: ", len(contours),"....")
for i in range(len(contours)):
    color = (255,0,0)
    cv2.drawContours(src, contours, -1, color, 2)

# Show the final image
cv2.imwrite("images/Contours.png", src)
print("\nFinalized...")  
