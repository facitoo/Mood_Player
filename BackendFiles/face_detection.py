import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)
facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret, frame = video_capture.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) 
    clahe_image = clahe.apply(gray) 

    face = facecascade.detectMultiScale(clahe_image, scaleFactor=1.1, minNeighbors=10, minSize=(10, 10), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in face: 
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2) #draw it on "frame", (coordinates), (size), (RGB color), thickness 2
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
