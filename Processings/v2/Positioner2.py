import numpy as np
from FIRwindowFilter import FIRwindowFilter
import matplotlib.pyplot as plt
# function returns list of tuples for the descrete positions
# highest list is x direction
# next highest is y directio
# time series is inside each xy corrdinate
# Inputs:	x = postions taken at the same time as the data
#		  	pixelsX and pixelsY are the dementions of the test
# Output:	list of tuples for the descrete positions
def Positioner2(x,pixelsX,pixelsY):
	print("Start Positioning")
	positions = []
	xFiltered = FIRwindowFilter(x,4000000.0,5.0) # signal, sampling_rate(Hz) cutoff(Hz)
	x = (x-np.min(x))
	x = x*pixelsX/max(x)
	x = [int(i) for i in x]
	downsample = 50
	xDown = x[::downsample]
	dx = np.diff(xDown)
	dx = [0 if i < 0 else 1 for i in dx]
	
	y = np.zeros(len(x))
	prevSign = dx[0]
	prevY = 0
	#print("len(dx): ",len(dx))
	for i in range(len(dx)):
		#print("LOOP")
		if (dx[i] > prevSign):
			#print("change")
			prevY = prevY+1
		prevSign = dx[i]
		for j in range(downsample+len(x)%downsample):
			y[j+downsample*i] = prevY
	y = y*pixelsY/max(y)
	y = [int(i) for i in y]
	#plt.plot(y)
	#plt.show()
	
	positions = [x, y]
	return positions
	#print("x position max: ",np.max(x)," min: ", np.min(x))
	#print("y position max: ",np.max(y)," min: ", np.min(y))
	#print(positions[0:2])
	
	"""
	print("x position max: ",np.max(x)," min: ", np.min(x))
	
	print("dx length: ",len(dx))
	print("x length: ",len(x))
	"""

