from  cv2 import *

# initialize blob detector
detector = cv2.SimpleBlobDetector()

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera

while True:
	ret, frame = cam.read()
	if ret is not True:    # frame captured without any errors
		continue	
	keypoints = detector.detect(frame)
	imwrite("filename.jpg",frame) #save image
