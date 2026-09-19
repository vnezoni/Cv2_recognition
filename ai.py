import cv2
video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while 1:
    good, img = video.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("black video", img_gray)


    cv2.imshow("video", img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
