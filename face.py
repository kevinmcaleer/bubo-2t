# On Raspberry Pi 4 or 5 with Libcamera2 installed use
# `libcamerify python` to start python 

from cvzone import FaceDetectionModule
import cv2

cap = cv2.VideoCapture(0)
# cv2.namedWindow("output", cv2.WINDOW_NORMAL)
# cap.set(3, 1280)
# cap.set(4, 720)
face_detector = FaceDetectionModule.FaceDetector()

while True:
    #  Get image frame
    success, img = cap.read()
    img, list_faces = face_detector.findFaces(img)
    cv2.imshow("Face Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break