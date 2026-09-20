# Face recognition using cv2
# 1) <i>pip install opencv-python</i>
# 2) <i>pull this repository in your project</i>
# 3) <i>launch your project</i>

OpenCV (Open Source Computer Vision Library) is a free, open-source software library packed with more than 2,500 optimized algorithms for real-time computer vision, image processing, and machine learning.

In this repository I used haar's cascades which allow detect a specific object in the frame.
If you want to change the detected object use:
# <i>object_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + '(object)')</i>
I added a black-and-white image as an example of what the program sees when processing a frame using cascades.

If detecting sometimes work bad, try to change minNeighbours(last parametr of <em>face_cascade.detectMultiScale</em>) to bigger number

# To stop the program click button <b><kbd>q</kbd></b>
