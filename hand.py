from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
# cv2.namedWindow("output", cv2.WINDOW_NORMAL)
# cap.set(3, 1280)
# cap.set(4, 720)
detector = HandDetector(detectionCon=0.5, maxHands=2)

while True:
    #  Get image frame
    success, img = cap.read()
    img = cv2.flip(img, 0)
    # print(img)

    # cv2.imshow("Image", img)
    # cv2.waitKey(1)
    
    total_fingers = 0

    # Find the hand and its landmarks
    hands, img = detector.findHands(img) #with draw
    # hands, img = detector.findHands(img, draw=False) #with draw
    gesture = ""
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"] # List of 21 Landmark points
        bbox1 = hand1["bbox"] # Bound box info x,y,w,h
        centerPoint1 = hand1['center'] # center of the hand cx, cy
        handType1 = hand1["type"] # Handtype Left or Right

        fingers1 = detector.fingersUp(hand1)
        gesture = ""

        total_fingers = sum(fingers1)

        if fingers1 == [0, 0, 0, 1, 1]:
            gesture = "peace"
        elif fingers1 == [0,0,0,0,1]:
            gesture1 = "thumbsup"
        elif fingers1 == [0,1,1,1,1]:
            gesture = "four"

        # print("Fingers detected", fingers1)

        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"] # List of 21 Landmark points
            bbox2 = hand2["bbox"] # Bound box info x,y,w,h
            centerPoint2 = hand2['center'] # center of the hand cx, cy
            handType2 = hand2["type"] # Handtype Left or Right

            fingers2 = detector.fingersUp(hand2)
            total_fingers += sum(fingers2)

            # Find Distance between two Landmarks, could be same hand or different hands
            # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img) # with draw
            # length, info, img = detector.findDistance(lmList1[8], lmList2[8]) # without draw

    # Display
    finger_count = str(total_fingers)
    cv2.putText(img, gesture, (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(img, finger_count, (410,100),cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),6)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
cap.release()
cv2.destroyAllWindows()