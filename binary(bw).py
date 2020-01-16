#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 19:53:23 2020

@author: root
"""

import cv2
img=cv2.imread('Cat03.jpg')
cv2.imshow("cat",img )
cv2.waitKey(0)
ret,bw=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("binary(bw", bw)
cv2.waitKey(0)
cv2.destroyAllWindows()