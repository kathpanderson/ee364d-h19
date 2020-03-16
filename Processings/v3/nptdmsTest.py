from nptdms import TdmsFile
import numpy as np

def getData(filePath):
	print("Start getData")
	SPM = []
	tdms_file = TdmsFile(filePath)
	#tdms_file = TdmsFile("Analogslow.tdms")
	#tdms_file = TdmsFile("fourChannelSineWave.tdms")
	for group in tdms_file.groups():
		for channel in tdms_file.group_channels(group):
			SPM.append(channel.data)
			#print(len(channel.data), "in channel")''
	return SPM

def main():
	InputTDMS = 'fourChannelSineWave.tdms'
	dataOpened = getData(InputTDMS)
	print("shape of opened data: ", np.shape(dataOpened))

if __name__ == '__main__':
    main()