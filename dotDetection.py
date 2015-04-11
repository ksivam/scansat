from  cv2 import *

# initialize blob detector
detector = cv2.SimpleBlobDetector()

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
while True:
	ret, frame = cam.read()
	if ret:    # frame captured without any errors
		imwrite("filename.jpg",frame) #save image
