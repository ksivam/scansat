import mraa
import time

# on at same time to turn right
two = mraa.Gpio(2) 
three = mraa.Gpio(3)

two.dir(mraa.DIR_OUT)
three.dir(mraa.DIR_OUT)

# on at same time to turn left
four = mraa.Gpio(4)
five = mraa.Gpio(5)

four.dir(mraa.DIR_OUT)
five.dir(mraa.DIR_OUT)

# 2,3 are mutually exclusive with 4,5
def resetTwoThree():
	two.write(0)
	three.write(0)
	return

# 2,3 are mutually exclusive with 4,5
def resetFourFive():
	four.write(0)
	five.write(0)
	return


def moveLeft():
	resetTwoThree()
	time.sleep(1)
	four.write(1)
	five.write(1)
	return

def moveRight():
	resetFourFive()
	time.sleep(1)
	two.write(1)
	three.write(1)
	return;

def stop():
	resetTwoThree()
	resetFourFive()
	return


# move left
moveLeft()
time.sleep(3)
stop()

#move right
moveRight()
time.sleep(3)
stop()