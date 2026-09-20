import cv2
from cv2 import data
video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    good, img = video.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("black video", img_gray)
    faces = face_cascade.detectMultiScale(img_gray, 1.3, 1)
    print(faces)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("video", img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
