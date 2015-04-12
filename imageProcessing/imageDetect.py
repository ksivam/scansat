import cv2
import numpy as np
import mraa

left = mraa.Gpio(12)
right = mraa.Gpio(13)

left.dir(mraa.DIR_OUT)
right.dir(mraa.DIR_OUT)

def moveLeft():
	left.write(1)
	return

def moveRight():
	right.write(1)
	return;

def stop():
	left.write(0)
	right.write(0)
	return


stop()

# define range of red color in HSV
lower_red = np.array([170,160,60])
upper_red = np.array([180,255,255])
        
cap = cv2.VideoCapture(0)

while 1:
	ret, frame = cap.read()
	# apply HSV mask to filter out other colors
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask= mask)

	# grayscale and then threshold to black and white
	gray_image = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
	ret, thres = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY_INV )

	# canny edge detection
	thres = cv2.Canny(thres, 100, 100)

	# find contours in the threshold image
	contours, hierarchy = cv2.findContours(thres,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

	# finding contour with maximum area and store it as best_cnt
	best_cnt = []
	max_area = 0
	for cnt in contours:
	    area = cv2.contourArea(cnt)
	    if area > max_area:
	        max_area = area
	        best_cnt = cnt
	if(len(best_cnt) == 0):
		print "don't move, nothing found"
		stop()
		continue
	# finding centroids of best_cnt and draw a circle there
	M = cv2.moments(best_cnt)
	cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])


	#cv2.circle(frame,(cx,cy),20,255,-1)
	#cv2.rectangle(frame, (480,270) , (1080,810), 255);

	# Show it, if key pressed is 'Esc', exit the loop
	#cv2.imshow('thresh', frame)

	#im_with_keypoints = cv2.drawKeypoints(thres, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	#cv2.imshow('ImageWindow', im_with_keypoints)
	print cx
	if(cx > 360):
	    print "go right"
	    moveRight()

	elif(cx < 160):
	    print "go left"
	    moveLeft()
	else:
	    print "don't move"
	    stop()
#cv2.waitKey(5)

cap.release()
cv2.destroyAllWindows()
