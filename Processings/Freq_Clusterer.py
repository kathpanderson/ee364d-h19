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
from Blocker import Blocker
from Positioner import Positioner
from normDFT import normDFT
from Thresholder import Thresholder
from ClusterFinder import ClusterFinder
from Visualizer import Visualizer
from DataOuter import DataOuter
from MovieMaker import MovieMaker


def Positioner(SNRphoto1, SNRphoto2, SNRcurrent1, SNRcurrent2, SNRtipBias, pixelsX, pixelsY):
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
		return 1
	return 0