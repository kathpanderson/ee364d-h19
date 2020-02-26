import numpy as np
# function returns list of tuples for the descrete positions
# highest list is x direction
# next highest is y directio
# time series is inside each xy corrdinate
# Inputs:	x = postions taken at the same time as the data
#		  	pixelsX and pixelsY are the dementions of the test
# Output:	list of tuples for the descrete positions
def Positioner2(x,pixelsX,pixelsY):
	positions = []
	x = (x*pixelsX/(2*np.maximum(x))).astype(int)
	dx = np.diff(x)
	dx = [0 if i < 0 else 1 for i in dx]
	y = np.zeros(len(dx))
	prevSign = dx[0]
	prevY = y[0]
	for i in range(dx):
		if (dx[i] != prevSign) & dx[i]:
			prevY += prevY
		y[i] = prevY
	y = (y*pixelsY/(np.maximum(x))).astype(int)
	positions = [x, y]
	return positions

