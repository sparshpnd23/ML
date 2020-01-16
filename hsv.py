#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:12:47 2020

@author: root
"""

import cv2
img=cv2.imread("Cat03.jpg")
img_HSV =cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV IMAGE",img_HSV)
cv2.imshow("HUE", img_HSV[:,:,0])
cv2.imshow("SATURATION", img_HSV[:,:,1])
cv2.imshow("VALUE", img_HSV[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()