import cv2

src  = cv2.imread("images/coins.jpg", 1)
img  = cv2.imwrite("images/Original.png",src)
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
print("\nObjects found: ", len(contours), "....")
five_p = 0
two_p = 0
one_p = 0
twenty_c = 0
ten_c = 0
two_c = 0
one_c = 0
for i in range(len(contours)):
    color = (255,0,0)
    cv2.drawContours(src, contours, -1, color, 2)
    area = cv2.contourArea(contours[i])
    if area < 5500 and area > 4500:
        two_p += 1
    elif area < 4500 and area > 4000:
        one_p += 1
    elif area < 3500 and area > 3300:
        five_p += 1
    elif area < 3300 and area > 3000:
        twenty_c += 1
    elif area < 3000 and area > 2500:
        ten_c += 1
    elif area < 2500 and area > 2000:
        two_c += 1
    else:
        one_c += 1

# Show the final image
cv2.imwrite("images/Contours.png", src)

# Shows the total value of the money
print("Total: FivePounds:", five_p,"TwoPounds:",two_p,"OnePound:",one_p,"TwentyCents:",twenty_c,"TenCents:",ten_c,"TwoCents:",two_c,"OneCents",one_c)
res = (five_p * 5) + (two_p * 2) + (one_p) + (twenty_c * 0.2) + (ten_c * 0.1) + (two_c * 0.02) + (one_c * 0.01)
print("{:.2f}".format(res))
print("\nFinalized...") 
