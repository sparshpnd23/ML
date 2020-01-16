
#Learn more or give us feedback
import  cv2

# loading  camera
cap=cv2.VideoCapture(0)
#  motion function
def mymotion(pc1,pc2,pc3):
	
	#  first diff
	result1=cv2.absdiff(pc1,pc2)
	result2=cv2.absdiff(pc2,pc3)
	#  
	finalimg=cv2.bitwise_and(result1,result2)
	return  finalimg

#   taking  3  picture
tp1=cap.read()[1]
tp2=cap.read()[1]
tp3=cap.read()[1]
#  converting into gray scale
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

#  we have to take more pictures
while  True:
	m=mymotion(gray1,gray2,gray3)
	status,frame=cap.read()
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#  checkind  iff
	print(m)
	# show
	cv2.imshow('motion',m)
	if cv2.waitKey(10) &  0xff  == ord('q') :
		break

cv2.destroyAllWindows()
cap.release()

