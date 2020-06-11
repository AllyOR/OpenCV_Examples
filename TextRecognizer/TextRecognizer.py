import cv2 
import pytesseract 
  
# The installed location of Tesseract-OCR in your system 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
 
# Read image with text
src = cv2.imread("images/text.png") 
  
# Convert the image to gray scale 
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imwrite("images/gray.png", gray)
cv2.imshow("Image", gray)

result = pytesseract.image_to_string(gray) 
print("Text:\n", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
