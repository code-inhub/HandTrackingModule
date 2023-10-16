import cv2
import time
import HandTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
fingerPoint=8
while True:
    success, img = cap.read()
    img = detector.findHands(img,True)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[fingerPoint])
        lmList=lmList[fingerPoint]
        cv2.circle(img, (lmList[1],lmList[2]), 15, (255, 0, 255), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
    # (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
