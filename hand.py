import cvzone
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = cvzone.HandDetector(detectionCon=0.5, maxHands=1)

while True:
    #  Get image frame
    success, img = cap.read()
    
    # Find the hand and its landmarks
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    