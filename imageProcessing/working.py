import cv2
import time
import numpy as np

# initialize blob detector
detector = cv2.SimpleBlobDetector()

# define range of red color in HSV
lower_red = np.array([170,160,60])
upper_red = np.array([180,255,255])
        
cap = cv2.VideoCapture(0)

i = 0;
while i < 10:
	ret, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_red, upper_red)

	res = cv2.bitwise_and(frame,frame, mask= mask)
	#cv2.imshow('ImageWindow',res)
	cv2.imwrite("frame"+ str(i)+".jpg",res)
	#cv2.waitKey(5)
	time.sleep(2)
	i = i+1

cap.release()
#cv2.destroyAllWindows()

