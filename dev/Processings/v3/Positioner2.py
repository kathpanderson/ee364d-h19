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
def Positioner2(x,pixelsX):
	print("Start Positioning")
	positions = []
	xFiltered = FIRwindowFilter(x,4000000.0,5.0) # signal, sampling_rate(Hz) cutoff(Hz)
	x = (x-np.min(x))
	x = x*(pixelsX-1)/max(x)
	x = [int(i) for i in x]
	downsample = 500
	xDown = x[::downsample]
	dx = np.diff(xDown)
	dx = [0 if i < 0 else 1 for i in dx]
	
	y = np.zeros(len(x), dtype=int)
	prevSign = dx[0]
	prevY = 0
	i = 0
	#print("len(dx): ",len(dx))
	for i in range(len(dx)):
		#print("LOOP")
		if (dx[i] > prevSign):
			#print("Last Y: ",prevY)
			prevY = prevY+1
			prevSign = dx[i]
		if (dx[i] < prevSign):
			prevSign = dx[i]
		for j in range(downsample):
			y[j+downsample*i] = prevY
	for k in range(len(x)%downsample):
			y[k+downsample*(i+1)] = prevY
	#plt.plot(y[::250])
	#plt.show()

	positions = [x, y]
	return positions

