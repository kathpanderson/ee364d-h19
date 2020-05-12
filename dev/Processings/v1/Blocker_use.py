import numpy as np

pixelsX = 20
pixelsY = 20
# function returns Blocking data, a space time seperated verstion of the data
# highest list is x direction
# next highest is y direction
# time series is inside each xy corrdinate
BlockedData = []
for x in range(0,pixelsX):
    BlockedData.append([])
    for y in range(0,pixelsY):
        BlockedData[x].append([])
#print(BlockedData)

with open('BlockerTest_sin.csv') as csvfile:
		readCSV = np.asarray(list(csv.reader(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)))
	
		timeP = (readCSV[:,0])
		X = (readCSV[:,1])
		Y = (readCSV[:,2])
		timeD = (readCSV[:,3])
		inData = (readCSV[:,4])

		# match each data point with a position through time stamp
		# place matched data into position's time series 
		posIndex = 0
		dataIndex = 0
		while (dataIndex < inData.size-1):
			while np.abs(timeD[dataIndex]-timeP[posIndex]) > np.abs(timeD[dataIndex]-timeP[posIndex+1]):
					posIndex += 1
			BlockedData[int(X[posIndex])][int(Y[posIndex])].append(inData[dataIndex])
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
		
