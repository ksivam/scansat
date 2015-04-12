import mraa
import time

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

# move left
moveLeft()
time.sleep(3)
stop()

#move right
moveRight()
time.sleep(3)
stop()