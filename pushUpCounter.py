import cv2
import numpy as np
import time
import poseEstimationModule as pem

cap = cv2.VideoCapture(0)
pTime = 0

detector = pem.poseDetector(detectionCon=0.8)

count, dir, bar, per = 0, 0, 0, 0

while True:
    success, img = cap.read()
    
    # img = cv2.resize((cv2.imread("PushUpCounter/reference.jpg")), (640, 480))
    img = cv2.resize(img, (1366, 780))  # Resize the image to a standard size
    img = detector.findPose(img, draw=False)
    
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
    if (len(lmList)):
        print(lmList[31][2], lmList[29][2])  # Print the z-coordinates of the left and right hands
        if (lmList[31][2] + 50 > lmList[29][2] and lmList[32][2] + 50 > lmList[30][2]):
            # Left Arm
            angle = detector.findAngle(img, 11, 13, 15)
            # Right Arm
            detector.findAngle(img, 12, 14, 16)
            detector.findAngle(img, 27, 29, 31)
            detector.findAngle(img, 28, 30, 32)
            
            per = -1.25 * angle + 212.5  # Linear equation to convert angle to percentage
            per = (0 if per < 0 else 100 if per > 100 else per)
            bar = np.interp(per, (0, 100), (650, 100))  # Interpolate percentage to bar height
            # print(angle, per)
            
            # Check for the body movement
            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            elif per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0
                    
            img = cv2.flip(img, 1)
            
            if (per == 100 or per == 0):
                cv2.putText(img, f'{int(per)}%', (1200, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            else:
                cv2.putText(img, f'{int(per)}%', (1200, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                
            cv2.rectangle(img, (1200, 100), (1275, 650), (0, 0, 255), 3)
            cv2.rectangle(img, (1200, int(bar)), (1275, 650), (0, 0, 255), cv2.FILLED)
    else:
        img = cv2.flip(img, 1)
        cv2.rectangle(img, (430, 740), (1335, 620), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, 'Take your position.', (440, 710), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)
        
    cv2.rectangle(img, (12, 6), (425, 100), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'count: {int(count)}', (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 5)
            
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 730), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)