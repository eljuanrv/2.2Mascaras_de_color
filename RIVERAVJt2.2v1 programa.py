#JUAN RIVERA VARGAS
import cv2
import numpy as np


cap = cv2.VideoCapture(0)


azulClaro = np.array([60,0,0],np.uint8) #237,241,73
azulOscuro = np.array([120,255,255],np.uint8)
while(True):
    ret,frame = cap.read()


    if (ret == True):
        frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV,azulClaro,azulOscuro)
        cv2.imshow('maskAzul',mask)        
        cv2.imshow('frame',frame)
        if( cv2.waitKey(1) & 0xFF == ord('s')):
            break
cap.release()
cv2.destroyAllWindows()