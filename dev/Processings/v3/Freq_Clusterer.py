# Main for processing of SPM Data
# May need reformating based on GUI calling structure
# First positions are assigned based on the timestamp of the measurment
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
from Positioner2 import Positioner2
from Blocker2 import Blocker2
from normDFT import normDFT
from Thresholder import thresholder
from ClusterFinder import ClusterFinder
#from Visualizer import Visualizer
#from MovieMaker import MovieMaker

def Freq_Clusterer(InputTDMS,pixelsX,pixelsY,noise,SNR,select,OutputCSV,OutputMP4):
	RawData = getData(InputTDMS)
	positions = Positioner2(RawData[3],pixelsX)
	pixelsYMessured = max(positions[1])+1
	print("pixelsYMessured: ",pixelsYMessured)
	#print("LAST Y: ", positions[1][len(positions[1])-1])
	print("NUMBER OF POSITIONS: ", len(positions[0]))
	print("NUMBER OF DATA 1: ", len(RawData[0]))
	BlockedData = Blocker2(positions, RawData[select], pixelsX, pixelsYMessured) # positon in 3, data in (0=current, 1=photodetector)
	#print("DONE BLOCKING Shape",BlockedData.shape)
	
	# fourier transform time axis of 3D array into (x,y,f)
	N = len(blockedData[0][0])	#Number of points in time/freq axis
	for i in range(pixelsX):	# blackman window may not be best choice
		for j in range(pixelsYMessured):
			blockedData[i][j] = normDFT(blockedData[i][j])#np.blackman(N),N)#np.fft.fft(blockedData[i][j]*np.blackman(N))
	N = N/2

	noiseRejection = 1 
	threshedData = thresholder(noise, SNR, noiseRejection, data)
	clusterCenterts = ClusterFinder(threshedData,N)

	with open(OutputCSV, 'w', newline='') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow(["Clusters"])
			for row in clusterCenterts:
				wr.writerow(row)


def main():
	InputTDMS = 'FourChannelMinute.tdms'
	#InputTDMS = 'fourChannelSineWave.tdms'
	pixelsX = 128
	pixelsY = 128
	noise = -2 #dB
	SNR = 10 #dB
	select = 1
	OutputCSV = 'processedData.csv'
	OutputMP4 = 'processedData.mp4'
	Freq_Clusterer(InputTDMS,pixelsX,pixelsY,noise,SNR,select,OutputCSV,OutputMP4)

if __name__ == '__main__':
    main()