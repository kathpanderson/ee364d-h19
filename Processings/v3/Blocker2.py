import numpy as np
# function returns list BlockedData, a space-time seperated verstion of the data
# highest list is x direction
# next highest is y direction
# time series is inside each xy corrdinate
# Inputs:	posIn = taken at the same time as the data
#		  	InData = value of data collected
#		  	pixelsX and pixelsY are the dementions of the test
# Output:	list of spacially shaped data
def Blocker2(positions, InData, pixelsX, pixelsYMessured):
	print("Start Blocking")
	BlockedData = []
	for x in range(pixelsX):
		BlockedData.append([])
		for y in range(pixelsYMessured):
			BlockedData[x].append([])

	for k in range(len(InData)):
		#print(positions[0][k],positions[1][k],InData[k])
		BlockedData[positions[0][k]][positions[1][k]].append(InData[k])
	print("DONE WITH NON-Norm BLOCKING")
	# Find the maximum length of a time series
	maxLen = 0
	for i in range(pixelsX):
		maxLenNew = len(BlockedData[i][9])
		if maxLenNew > maxLen: # choose arbitrary y for max len find
			maxLen = maxLenNew
	#print("maxLen: ", maxLen)
	# zero pad all shorter time series
	for i in range(pixelsX):
		for j in range(pixelsYMessured):
				dataLength = len(BlockedData[i][j])
				if maxLen > dataLength:
					BlockedData[i][j].extend([0]*(maxLen-dataLength))
				elif maxLen < dataLength:
					BlockedData[i][j] = BlockedData[i][j][:maxLen]
	return BlockedData
