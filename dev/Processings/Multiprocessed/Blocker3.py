import numpy as np
from FIRwindowFilter import FIRwindowFilter
from nptdmsTest import getData
import matplotlib.pyplot as plt
from multiprocessing import Pool


def rounding(element):
	return int(round(element))


def zerosAndOnes(element):
	if(element < 0):
		return 0
	else:
		return 1

def extendWithZeros(element, maxLength):
	# BlockedData[i][j].extend([0.0]*(maxLen-len(BlockedData[i][j])))
	element.extend([0.0]*(maxLength-len(element)))
	return element

# function returns list of tuples for the descrete positions
# highest list is x direction
# next highest is y directio
# time series is inside each xy corrdinate
# Inputs:	x = postions taken at the same time as the data
#		  	pixelsX and pixelsY are the dementions of the test
# Output:	list of tuples for the descrete positions
def Blocker3(x,InData,pixelsX,pixelsY):
	print("Start X positioning")

	BlockedData = []
	for i in range(pixelsX):
		BlockedData.append([])
		for j in range(pixelsY):
			BlockedData[i].append([])

	xFil = FIRwindowFilter(x,4000000.0,5.0) # signal, sampling_rate(Hz) cutoff(Hz)
	xFil = (xFil-np.min(xFil))
	xFil = xFil*(pixelsX-1)/max(xFil)
	# xFil = [int(round(i)) for i in xFil]
	with Pool() as pool:
		xFil = pool.map(rounding, (i for i in xFil))
		pool.close()
		pool.join()
	downsample = 50000                    # Assuming trace is 1Hz, DS=400000 gives 10 points/trace
	xDown = xFil[::downsample]
	dx = np.diff(xDown)
	# dx = [0 if i < 0 else 1 for i in dx]
	with Pool() as pool:
		dx = pool.map(zerosAndOnes, (i for i in dx))
		pool.close()
		pool.join()
	print("Start blockering in X and Y")
	prevSign = dx[0]
	prevY = 0
	i = 0
	forward = 1
	runs = 0
	for i in range(len(dx)):
		if (dx[i] > prevSign):
			runs = runs +1
			if forward:
				prevY = prevY+1
				if prevY==pixelsY-1:
					forward = 0
			else:
				prevY = prevY-1
				if prevY==0:
					forward = 1
		prevSign = dx[i]
		for j in range(downsample):
			BlockedData[xFil[j+downsample*i]][prevY].append(InData[j+downsample*i])
	for k in range(len(x)%downsample):
			BlockedData[xFil[k+downsample*(i+1)]][prevY].append(InData[k+downsample*(i+1)])
	print("Find largest length")
	maxLen = 0
	for i in range(pixelsX):
		for j in range(pixelsY):
			maxLenNew = len(BlockedData[i][j])
			if maxLenNew > maxLen:
				maxLen = maxLenNew
	print("Extend with zeros")
	for i in range(pixelsX):
		for j in range(pixelsY):
			BlockedData[i][j].extend([0.0]*(maxLen-len(BlockedData[i][j])))
	# CAUSES MEMORY ERROR; I THINK IT IS BECAUSE OF PASSING DATA TO AND FROM FUNCTION
	# with Pool() as pool:
		# BlockedDataResults = pool.starmap(extendWithZeros, [(BlockedData[i][j], maxLen) for i in range(pixelsX) for j in range(pixelsY)])
		# index = 0
		# for x in range(pixelsX):
			# for y in range(pixelsY):
				# BlockedData[x][y] = BlockedDataResults[index]
				# index +=1
		# pool.close()
		# pool.join()

	return BlockedData

def main():
	InputTDMS = 'fourChannelMinute.tdms'
	#InputTDMS = 'fourChannelSineWave.tdms'
	pixelsX = 128
	pixelsY = 128
	RawData = getData(InputTDMS)
	BlockedData = Blocker3(RawData[3],RawData[1],pixelsX,pixelsY)
	print("LENGTH X: ",len(BlockedData), "\nLENGTH Y: ",len(BlockedData[0]))
	plt.figure(1)
	plt.plot(BlockedData[12][125])
	plt.show()

if __name__ == '__main__':
	main()