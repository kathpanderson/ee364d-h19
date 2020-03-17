import numpy as np
import sys
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
	# print("Maxsize: " + str(sys.maxsize))
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
	print("maxLen: ", maxLen)

	newArray = np.zeros((pixelsX,pixelsYMessured,maxLen), dtype=float32)
	# zero pad all shorter time series
	"""for i in range(pixelsX):
		for j in range(pixelsYMessured):
				dataLength = len(BlockedData[i][j])
				print("DATALENGTH:" + str(i) + " " + str(j) + " " + str(dataLength))
				if maxLen > dataLength:
					# BlockedData[i][j].extend([0]*(maxLen-dataLength))
					# print("ADD:" + str(i) + " " + str(j) + " " + str(maxLen-dataLength))
					for e in range(maxLen-dataLength):
						BlockedData[i][j].append(0)
				elif maxLen < dataLength:
					BlockedData[i][j] = BlockedData[i][j][:maxLen]"""

	for i in range(pixelsX):
		for j in range(pixelsYMessured):
			minLength = min(len(BlockedData[i][j]), maxLen)
			for e in range(minLength):
				newArray[i][j][e] = BlockedData[i][j][e]
	print("done with blocking")
	return newArray