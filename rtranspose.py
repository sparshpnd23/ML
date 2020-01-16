#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 22:10:30 2020

@author: root
"""
import cv2
import numpy as np
img=cv2.imread("Cat03.jpg")
cv2.imshow("ORIGINAL", img)
cv2.waitKey(0)
rotate_img=cv2.transpose(img)

cv2.imshow("ROTATION",rotate_img)
cv2.waitKey(0)
cv2.destroyAllWindows()