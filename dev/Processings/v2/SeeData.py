from nptdms import TdmsFile
import matplotlib.pyplot as plt

#Open and Read tdms file
SPM = []
InputLVM = 'XData02282020_2.tdms'
tdms_file = TdmsFile(InputLVM)
#tdms_file = TdmsFile("Analogslow.tdms")
#tdms_file = TdmsFile("fourChannelSineWave.tdms")
for group in tdms_file.groups():
	for channel in tdms_file.group_channels(group):
		SPM.append(channel.data)

#plot
sToPlot = 1000
numberOfPlots = len(SPM[0])/sToPlot
plt.ion()
for i in range(int(numberOfPlots)):
	plt.plot(SPM[0][sToPlot*i:sToPlot*(i+1)])
	plt.draw()
	plt.pause(0.5)
	plt.clf()