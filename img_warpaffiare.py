#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:49:34 2020

@author: root
"""

import cv2
import numpy as np
img=cv2.imread("Cat03.jpg")
height,width=img.shape[:2]
q_height,q_width = height/5,width/5


T = np.float64([[1,0,q_width],
                [0,1,q_height]])
print(T)

img_transformation = cv2.warpAffine(img, T, (width,height))
cv2.imshow("ORIGINAL", img)
cv2.imshow("IMG_TRANSLATION",img_transformation)
cv2.waitKey(0)
cv2.destroyAllWindows()