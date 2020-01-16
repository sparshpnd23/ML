#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:22:46 2020

@author: root
"""

import cv2
img = cv2.imread('Cat03.jpg')

#gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Cat',img)
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()