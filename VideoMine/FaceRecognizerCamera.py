import cv2

faceDetector = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

def detectAndDisplay(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("images/original.png",frame)
    cv2.imwrite("images/gray.png", gray)
    
    frame_gray = cv2.equalizeHist(gray)
    cv2.imwrite("images/equalized.png", frame_gray)
    
    faces = faceDetector.detectMultiScale(frame_gray)
    print("Faces detected: ", len(faces))
    
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        cv2.rectangle(src, (x,y), (x+w, y+h),(0,255,0), 2)
    cv2.imshow('Capture - Face detection', src)

while True:
    ret, src = cam.read()
    detectAndDisplay(src)
    if cv2.waitKey(10) == 27:
        break
