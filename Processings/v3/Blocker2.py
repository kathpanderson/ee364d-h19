import numpy as np
from Positioner2 import Positioner2
# function returns list BlockedData, a space-time seperated verstion of the data
# highest list is x direction
# next highest is y direction
# time series is inside each xy corrdinate
# Inputs:	posIn = taken at the same time as the data
#		  	InData = value of data collected
#		  	pixelsX and pixelsY are the dementions of the test
# Output:	list of spacially shaped data
def Blocker2(InPos, InData, pixelsX, pixelsY):
	print("Start Blocking")
	BlockedData = []
	for x in range(0,pixelsX):
		BlockedData.append([])
		for y in range(0,pixelsY):
			BlockedData[x].append([])

	positions = Positioner2(InPos,pixelsX,pixelsY)
	for k in range(len(InData)):
		BlockedData[positions[0][k]][positions[1][k]].append(InData[k])
		# Find the maximum length of a time series
		maxLen = 0
		for i in range(pixelsX):
			for j in range(pixelsY):
				if len(BlockedData[i][j]) > maxLen:
					maxLen = len(BlockedData[i][j])
		# zero pad all shorter time series
		for i in range(pixelsX):
			for j in range(pixelsY):
					BlockedData[i][j].extend([0]*(maxLen-len(BlockedData[i][j])))
	return BlockedData