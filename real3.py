import cv2
import numpy as np
import pyautogui as au


au.FAILSAFE=False

(sx,sy)=au.size()
#image resizing
(capx,capy)=(320,240)

cap=cv2.VideoCapture(0)
cap.set(3,capx)
cap.set(4,capy)

#detect green
greenmin=np.array([33,80,40])
greenmax=np.array([102,255,255])

kernelopen=np.ones((5,5))
kernelclose=np.ones((20,20))

while True:
        
    success,img = cap.read()
    img=cv2.flip(img,1)
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(imghsv,greenmin,greenmax)

    maskopen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelopen)
    maskc=cv2.morphologyEx(maskopen,cv2.MORPH_CLOSE,kernelclose)
    maskfinal=maskc
    _,conts,h=cv2.findContours(maskfinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #cv2.imshow('maskclose',maskc)
    #cv2.imshow('maskopen',maskopen)
    #cv2.imshow('mask1',imghsv)
    #cv2.imshow('mask',mask)
    #cv2.imshow('maskopen',maskopen)
    #cv2.imshow('maskclose',maskclose)
    cv2.imshow('capcont',conts)
    cv2.imshow('cap',img)
    cv2.waitKey(5)

cap.release()
cv2.destroyAllWindows()
    
