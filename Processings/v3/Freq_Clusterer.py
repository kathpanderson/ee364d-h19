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
from Blocker2 import Blocker2
from normDFT import normDFT
from Thresholder import thresholder
from ClusterFinder import ClusterFinder
#from Visualizer import Visualizer
#from MovieMaker import MovieMaker

def Freq_Clusterer(InputTDMS,pixelsX,pixelsY,noise,SNR,select,OutputCSV,OutputMP4):
	RawData = getData(InputTDMS)
	blockedData = Blocker2(RawData[2], RawData[select], pixelsX, pixelsY) # positon in 2, data in (0=current, 1=photodetector) ////Change with what Clara Tells me!!!!!
	print("DONE BLOCKING Shape",BlockedData.shape)
	
	# fourier transform time axis of 3D array into (x,y,f)
	N = len(blockedData[0][0])	#Number of points in time/freq axis
	for i in range(pixelsX):	# blackman window may not be best choice
		for j in range(pixelsY):
			blockedData[i][j] = normDFT(blockedData[i][j])#np.blackman(N),N)#np.fft.fft(blockedData[i][j]*np.blackman(N))
	N = N/2

	noiseRejection = 1 
	threshedData = thresholder(noise, SNR, noiseRejection, blockedData)
	clusterCenterts = ClusterFinder(threshedData,N)

	with open(OutputCSV, 'w', newline='') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			for row in clusterCenterts:
				wr.writerow(row)


def main():
	InputTDMS = 'fourChannelSineWave.tdms'
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

    	#plt.plot(dataSPM[0][0:1000])

sToPlot =1000
numberOfPlots = len(dataSPM[0])/sToPlot
plt.ion()
for i in range(int(numberOfPlots)):
	plt.plot(dataSPM[0][sToPlot*i:sToPlot*(i+1)])
	plt.draw()
	plt.pause(1)
	plt.clf()
"""
#for channel in dataSPM:
#	print(len(channel))