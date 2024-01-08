import cv2 as cv
import  numpy as np
import time
import HandTrackingModule as htm
import math
from cvzone.SerialModule import SerialObject
import serial


arduino = SerialObject("COM6")
cap =cv.VideoCapture(0)
pTime=0
cTime=0
detector=htm.handDetector(detection_conf=0.7)
while True:
    success,frame=cap.read()
    frame,list=detector.findHands(frame)
    # print(list)
    if len(list) !=0:
        x1,y1=list[4][1],list[4][2]
        x2, y2 = list[8][1],list[8][2]
        x3,y3=(x1+x2)//2,(y1+y2)//2
        cv.circle(frame,(x1,y1),15,(255,0,255),-1)
        cv.circle(frame, (x2, y2), 15, (255, 0, 255), -1)
        cv.circle(frame,(x3,y3),15,(255,0,255),-1)
        cv.line(frame,(x1,y1),(x2,y2),(255, 0, 255),3)
        length=math.hypot((x2-x1),(y2-y1))
        g=int(np.interp(length,[40,270],[0,255]))
        print(g)
        arduino.sendData([g])
    #FPS calculations
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv.putText(frame,f'FPS:{int(fps)}',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)



    cv.imshow("Video",frame)
    if cv.waitKey(1) & 0xFF==ord("d"):
        break
cap.release()
cv.destroyAllWindows()
