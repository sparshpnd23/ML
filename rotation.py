

import cv2
import numpy as np
img=cv2.imread("Cat03.jpg")
height,width=img.shape[:2]
rotation_matrix=cv2.getRotationMatrix2D((height/2,width/2), 70, 0.5)


img_transformation = cv2.warpAffine(img, rotation_matrix, (width,height))
cv2.imshow("ORIGINAL", img)
cv2.imshow("IMG_TRANSLATION",img_transformation)
cv2.waitKey(0)
cv2.destroyAllWindows()