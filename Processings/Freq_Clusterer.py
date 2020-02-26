# Main for processing of SPM Data
# May need reformating based on GUI calling structure
# First positions are assigned based on the timestamp of the measurment
# Next The FFT of each time series is taken
# A threshold is then taken to statistically eliminate data points likely to be noise
# The remaining points are clustered in each frequency using meanshift
# The clusters are then visualized with access to the GUI
# Inputs:	SNR for Photdetector #1, Photdetector #2, Current #1, Current #2, Tip Bias
#			number of X pixels, and number of Y pixels
#			Positions.csv
#			RawData.csv
# Outputs:	TimeSpaceData.csv
#			ProcessedData.csv
#			ProcessedData.mp4
from Blocker2 import Blocker2
#from Positioner2 import Positioner2
#from normDFT import normDFT
#from Thresholder import Thresholder
#from ClusterFinder import ClusterFinder
#from Visualizer import Visualizer
#from DataOuter import DataOuter
#from MovieMaker import MovieMaker
#import sys

"""
#(SNRphoto1, SNRphoto2, SNRcurrent1, SNRcurrent2, SNRtipBias, pixelsX, pixelsY):
	# open rawData and place into blocked off 3d array (x,y,t)
	with open('RawData.csv') as csvfile:
		RawData = np.asarray(list(csv.reader(csvfile, delimiter=','))[1:], dtype=np.float32)
		positions = Positioner()
		dataSelect = 2 # 0=Phototdetector(Current) 1,1=Phototdetector(Current) 2=Tip Bias
		blockedData = Blocker(positions, RawData[2*dataSelect], InData[2*dataSelect+1], pixelsX, pixelsY)
		# fourier transform time axis of 3D array into (x,y,f)
		N = blockedData[0][0].length()	#Number of points in time/freq axis
		for i in range(pixelsX):	# blackman window may not be best choice
			for j in range(pixelsY):
				blockedData[i][j] = normDFT(blockedData[i][j]np.blackman(N),N)#np.fft.fft(blockedData[i][j]*np.blackman(N))
		N = N/2

		threshedData = Thresholder(blockedData,N)
		clusterCenterts = ClusterFinder(threshedData,N)
		visual = Visualizer(clusterCenterts)
		DataOuter(visual)
		MovieMaker(visual)
"""
InputLVM = 'sinewave.lvm'
rawData = 'rawData.csv'
processedData = 'processedData.csv'
NumChannels = 4
pixelsX = 128
pixelsY = 128
dataSelect = 1 # 1=Tip Bias, 2=PhototdetectorA(Current) , 3=PhototdetectorB(Current) 

lvm_Reader(InputLVM, rawData, NumChannels)
with open(rawData,'r') as csvfile:
	RawData = np.asarray(list(csv.reader(csvfile, delimiter=','))[1:], dtype=np.float32)	
	BlockedData = Blocker(RawData[0], RawData[1], pixelsX, pixelsY) # positon in 0, data in 1
	ReformData = []
	for t in range(len(BlockedData[0][0])):
		for x in range(len(BlockedData)):
			for y in range(len(BlockedData[x])):
				ReformData.append([x,y,BlockedData[x][y][t]])

	with open(processedData, 'w', newline='') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		for row in ReformData:
			wr.writerow(row)