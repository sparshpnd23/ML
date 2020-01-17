#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:23:38 2020

@author: root
"""

import cv2
#now loading canera driver
cap=cv2.VideoCapture(0)
face_detect=cv2.CascadeClassifier('face1.xml')
eye_detect=cv2.CascadeClassifier('eye1.xml')
smile_detect=cv2.CascadeClassifier('smile.xml')
while cap.isOpened():
    # taking piture
    status,frame = cap.read()
#converting into gray
    grayimg=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face=face_detect.detectMultiScale(grayimg)
    print(face)
    #rectangle
    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0, 255),4)
        onlyface=frame[y:y+h,x:x+w]
        eye=eye_detect.detectMultiScale(onlyface)
        smile=smile_detect.detectMultiScale(onlyface)
        for (ex,ey,ew,eh) in eye:
            
            cv2.rectangle(onlyface, (ex,ey), (ex+ew,ey+eh), (255,0,0),2)
        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(onlyface, (sx,sy), (sx+sw,sy+sh), (255,0,0),2)

    cv2.imshow('face', frame)
    
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()