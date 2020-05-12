from nptdms import TdmsFile

def getData(filePath):
	print("Start getData")
	SPM = []
	tdms_file = TdmsFile(filePath)
	#tdms_file = TdmsFile("Analogslow.tdms")
	#tdms_file = TdmsFile("fourChannelSineWave.tdms")
	for group in tdms_file.groups():
		for channel in tdms_file.group_channels(group):
			SPM.append(channel.data)
#print(len(channel.data))''
	return SPM