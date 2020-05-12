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
	"""BlockedData = []
	for x in range(pixelsX):
		BlockedData.append([])
		for y in range(pixelsYMessured):
			BlockedData[x].append([])"""

	lenArray = np.zeros((pixelsX, pixelsYMessured), dtype=int)

	maxLen = 0

	for k in range(len(InData)):
		lenArray[positions[0][k]][positions[1][k]] = lenArray[positions[0][k]][positions[1][k]] + 1

	# If you still want an arbitrary maxLen, this would be the for loop to do it in @Vic
	for x in range(pixelsX):
		for y in range(9,10):
			if(lenArray[x][y] > maxLen):
				maxLen = lenArray[x][y]

	"""for k in range(len(InData)):
		#print(positions[0][k],positions[1][k],InData[k])
		BlockedData[positions[0][k]][positions[1][k]].append(InData[k])
	print("DONE WITH NON-Norm BLOCKING")"""

	# Find the maximum length of a time series
	"""maxLen = 0
	for i in range(pixelsX):
		maxLenNew = len(BlockedData[i][9])
		if maxLenNew > maxLen: # choose arbitrary y for max len find
			maxLen = maxLenNew
	print("maxLen: ", maxLen)"""

	try:
		BlockedData = np.zeros((pixelsX,pixelsYMessured), dtype=np.float32)
	except Exception as ex:
		# Memory error. Will have to use file I/O
		print(ex)
		return(-1)

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

	"""for i in range(pixelsX):
		for j in range(pixelsYMessured):
			minLength = min(len(BlockedData[i][j]), maxLen)
			for e in range(minLength):
				newArray[i][j][e] = BlockedData[i][j][e]"""

	"""The way I see it, there are 4 options for adding the InData to BlockedData now:
		1) I sort the positions array and then I can add the InData to each position one
			by one in order. That's risky cause the arrays are obviously big, but mostly
			because the InData indices would have to be switched around too to the correct
			positions as the positions array was sorted. This option however uses the least
			memory at the cost of time.
		2) I use an extra numpy array of pixelsX by pixelsYMessured size to store what index
			we're on in each position where the next bit of InData will go in that part. Drawback:
			uses way more memory.
		3) We make the next position where an InData will get added float32.max. Drawbacks:
			each time you want to add something, you have to iterate through the array to find
			where the float32.max is. Also at the end all the float32.maxes have to be removed.
			Also there is added complexity with if you actually fill up that position with maxLen
			values.
		4) I make BlockedData a 2D numpy array of pixelsX by pixelsYMessured, and then somehow
			for the first value at each position I'd have to create a numpy array of size one
			there for it, and then append the rest of the values as they come. And then we'd
			have to append 0s all the way to maxLen as before. However, I don't know how to
			manipulate numpy arrays well enough to figure out how to create the initial data
			structure for this."""

	for k in range(len(InData)):
		if(BlockedData[positions[0][k]][positions[1][k]] == 0):
			# the first element to be added to this position
			BlockedData[positions[0][k]][positions[1][k]] = np.array([InData[k]], dtype=np.float32)
		else:
			np.append(BlockedData[positions[0][k]][positions[1][k]], [InData[k]])

	for i in range(pixelsX):
		for j in range(pixelsYMessured):
			# dataLength = BlockedData[positions[0][k]][positions[1][k]].size
			dataLength = BlockedData[i][j].size
			if maxLen > dataLength:
				for e in range(maxLen-dataLength):
					# np.append(BlockedData[positions[0][k]][positions[1][k]], [0])
					np.append(BlockedData[i][j], [0])
			elif maxLen < dataLength:
				print("BlockedData[" + str(i) + "][" + str(j) + "] = " + str(BlockedData[i][j]))
				print("dataLength = " + str(dataLength))
				print("maxLen = " + str(maxLen))
				print("BlockedData[positions[0][k]][positions[1][k]] = " + str(BlockedData[positions[0][k]][positions[1][k]]))
				BlockedData[i][j] = BlockedData[i][j][:maxLen]


	print("done with blocking")
	return BlockedData