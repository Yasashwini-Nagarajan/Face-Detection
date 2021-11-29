import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
while True:
	check,frame=video.read()
	gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray_img,1.1,4)
	for x,y,w,h in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
	cv2.imshow("Capture",frame)
	key=cv2.waitKey(10)
	if key== ord('q'):
		break
video.release()
cv2.destroyAllWindows()
