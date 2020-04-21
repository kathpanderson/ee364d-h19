# Main for processing of SPM Data
# Data is opened using nptdms
# blocking of the selected data is based on x psotion channel 3 from 0-3
# Next The FFT of each time series is taken
# A threshold is then taken to statistically eliminate data points likely to be noise
# The remaining points are clustered in each frequency using meanshift
# The clusters are then visualized with access to the GUI
# CURRENTLY PROCESSES ONE CHANNEL
# Inputs:	SNR for Photdetector #1, Photdetector #2, Current
#			number of X pixels, and number of Y pixels
#			Positions.csv
#			RawData.csv
# Outputs:	TimeSpaceData.csv
#			ProcessedData.csv
#			ProcessedData.mp4
from nptdmsTest import getData
from Blocker3 import Blocker3
from normDFT import normDFT
from Thresholder import Thresholder
from ClusterFinder import ClusterFinder
from multiprocessing import Pool
import csv
import time
#from Visualizer import Visualizer
#from MovieMaker import MovieMaker

def Freq_Clusterer(InputTDMS,pixelsX,pixelsY,noise,SNR,select,OutputCSV,OutputMP4):
	startGetData = time.perf_counter()
	RawData = getData(InputTDMS)
	stopGetData = time.perf_counter()
	print(f"GetData ran in {((stopGetData-startGetData)/60):0.10f} minutes")
	#print("NUMBER OF POSITIONS: ", len(positions[0]))
	#print("NUMBER OF DATA 1: ", len())
	startBlocker3 = time.perf_counter()
	BlockedData = Blocker3(RawData[3], RawData[select], pixelsX, pixelsY) # positon in 3, data in (0=current, 1=photodetector)
	stopBlocker3 = time.perf_counter()
	print(f"Blocker3 ran in {((stopBlocker3-startBlocker3)/60):0.10f} minutes")
	print("BLOCKING SHAPE X: ",len(BlockedData), "Y: ",len(BlockedData[0]),"T: ",len(BlockedData[0][0]))
	print("starting fourier Transform")
	# fourier transform time axis of 3D array into (x,y,f)
	N = len(BlockedData[0][0])	#Number of points in time/freq axis
	# for i in range(pixelsX):	# blackman window may not be best choice
		# for j in range(pixelsY):
			# for item in BlockedData[0][0]:
    			# float(item)
			# BlockedData[i][j] = normDFT(BlockedData[i][j],N)#*np.blackman(N),N)#
	startFourierTransform = time.perf_counter()
	with Pool() as pool:
		BlockedDataResults = pool.starmap(normDFT, [(BlockedData[i][j], N) for i in range(pixelsX) for j in range(pixelsY)])
		index = 0
		for x in range(pixelsX):
			for y in range(pixelsY):
				BlockedData[x][y] = BlockedDataResults[index]
				index += 1
		pool.close()
		pool.join()
	N = int(N/2)
	stopFourierTransform = time.perf_counter()
	print(f"Fourier Transform ran in {((stopFourierTransform-startFourierTransform)/60):0.10f} minutes")

	noiseRejection = 1
	startThresholder = time.perf_counter()
	threshedData = Thresholder(noise, SNR, noiseRejection, BlockedData)
	stopThresholder = time.perf_counter()
	print(f"Thresholder ran in {((stopThresholder-startThresholder)/60):0.10f} minutes")
	startClusterFinder = time.perf_counter()
	clusterCenterts = ClusterFinder(threshedData,N)
	stopClusterFinder = time.perf_counter()
	print(f"ClusterFinder ran in {((stopClusterFinder-startClusterFinder)/60):0.10f} minutes")

	print("saving cluster to file --", OutputCSV,"--")
	with open(OutputCSV, 'w', newline='') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow(["Clusters"])
			for row in clusterCenterts:
				wr.writerow(row)

def main():
	InputTDMS = 'fourChannelMinute.tdms'
	#InputTDMS = 'fourChannelSineWave.tdms'
	pixelsX = 128
	pixelsY = 128
	noise = -2 #dB
	SNR = 10 #dB
	select = 1
	OutputCSV = 'processedData.csv'
	OutputMP4 = 'processedData.mp4'
	startFreqClusterer = time.perf_counter()
	Freq_Clusterer(InputTDMS,pixelsX,pixelsY,noise,SNR,select,OutputCSV,OutputMP4)
	stopFreqClusterer = time.perf_counter()
	print(f"Program ran in {(((stopFreqClusterer-startFreqClusterer)/60)/60):0.10f} hours")

if __name__ == '__main__':
    main()