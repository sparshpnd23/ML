#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:26:59 2020

@author: root
"""

import cv2
import numpy as np
img = cv2.imread("Cat03.jpg")
cv2.imshow("ORIGINAL",img)
cv2.waitKey(0)
B,G,R =cv2.split(img)
print(img.shape[:2])
zeros =np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow("RED", cv2.merge([zeros,zeros,R]))
cv2.waitKey(0)
cv2.imshow("GREEN", cv2.merge([zeros,G,zeros]))
cv2.waitKey(0)
cv2.imshow("BLUE", cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)
cv2.destroyAllWindows()