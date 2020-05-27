import cv2

print("Detection of faces with OpenCV")
faceDetector = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
src = cv2.imread("images/photo.jpg")
faceDetections = faceDetector.detectMultiScale(src)

print("Faces detected: ", len(faceDetections))
for (x,y,w,h) in faceDetections:
    cv2.rectangle(src, (x,y), (x+w, y+h),(0,255,0), 2)

cv2.imwrite("images/Image_with_faces.png", src)
