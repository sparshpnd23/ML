import  cv2  #  after  installing  opencv  
#  now  time  for  loading  image 
#  if u want to connect  camera  --
cap=cv2.VideoCapture(0)   #  define  camera 
#  start / on  

while True:
	status_camera,img=cap.read()   #  start camera  to take picture 

	print(type(img))
	
	cv2.rectangle(img,(0,200),(100,400),(255,0,0),2)
	cv2.imshow('live2',img)
	if cv2.waitKey(30) & 0xff == 'q' :
		break

