# import the necessary packages
import numpy as np
import argparse
import cv2

# load the image
image = cv2.imread("pic.jpg")


# define the list of boundaries
red1 = ([0, 0, 255], [0, 0, 255])
red2 = ([0, 0, 130], [43, 43,130])
red3 = ([25, 146, 190], [62, 174, 250])
grey = ([103, 86, 65], [145, 133, 128])
boundaries = [red1, red2]

#upper = np.array([50, 56, 200], dtype = "uint8")
#lower = np.array([17, 15, 100], dtype = "uint8")

lower = np.array([17, 15, 100], dtype = "uint8")
upper = np.array([50, 56, 200], dtype = "uint8")

mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)

cv2.imshow("images", np.hstack([output]))
cv2.waitKey(0)
# loop over the boundaries
#for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	#lower = np.array(lower, dtype = "uint8")
	#upper = np.array(upper, dtype = "uint8")
 
	# find the colors within the specified boundaries and apply
	# the mask
	#mask = cv2.inRange(image, lower, upper)
	#output = cv2.bitwise_and(image, image, mask = mask)
 
	# show the images
	#cv2.imshow("images", np.hstack([image, output]))
	#cv2.waitKey(0)