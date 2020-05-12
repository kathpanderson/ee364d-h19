import numpy as np
# function returns list BlockedData, a space-time seperated verstion of the data
# highest list is x direction
# next highest is y direction
# time series is inside each xy corrdinate
# Inputs: postions = the timestamped and postion data x than y {np.array}
#		  timeD = timestamps of data collected
#		  InData = value of data collected
#		  pixelsX and pixelsY are the dementions of the test
def Blocker(positions, timeD, InData, pixelsX, pixelsY):
	# normalize position ~ this may need to be facier but will work if positions cover full scale
	timeP = (positions[:,0])
	X = (positions[:,1])
	X = X*pixelsX/np.maximum(X)
	X = X.astype(int)
	Y = (positions[:,2])
	Y = Y*pixelsY/np.maximum(Y)
	Y = Y.astype(int)

	# create data structure
	BlockedData = []
	for x in range(0,pixelsX):
    	BlockedData.append([])
    	for y in range(0,pixelsY):
        	BlockedData[x].append([])

	# match each data point with a position through time stamp
	# place matched data into position's time series 
	posIndex = 0
	dataIndex = 0
	while (dataIndex < inData.size-1):
		while np.abs(timeD[dataIndex]-timeP[posIndex]) > np.abs(timeD[dataIndex]-timeP[posIndex+1]):
				posIndex += 1
		BlockedData[X[posIndex]][Y[posIndex]].append(inData[dataIndex])
		dataIndex += 1
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
