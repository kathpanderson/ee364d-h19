# this script will call FreqClusterer with # arguments
# arg 0:	path to the labview generated tdms raw data file
# arg 1: 	name of the tdms file
# arg 2:	number of X pixels in spm text
# arg 3:	number of Y pixels in spm text
# arg 4: 	path to save created files
# arg 5: 	name for created files (will be used for csv and video outputs)
# arg 6:	test being ran (0=current, 1=photodetector)
# arg 7: 	tested noise current
# arg 8: 	expected SNR of current
# arg 9: 	tested noise photodetector 1
# arg 10: 	expected SNR of photodetector 1
# arg 11: 	tested noise photodetector 2
# arg 12: 	expected SNR of photodetector 2
import sys
import os.path

numberOfExpectedArgs = 12
arg = sys.argv[1:]
if len(arg) = numberOfExpectedArgs:	
	InputPath = arg[0]
	InputName = arg[1]
	outPath = arg[4]
	outName = arg[5]
	InputTDMS = os.path.join(InputPath, InputName+".tdms")
	pixelsX = arg[2]
	pixelsY = arg[3]
	noise = arg[9] if arg[6] else arg[7]
	SNR = arg[10] if arg[6] else arg[8]
	select = arg[6]
	OutputCSV = os.path.join(outPath, outName+".csv")
	OutputMP4 = os.path.join(outPath, outName+".mp4")
	FreqClusterer(InputTDMS,pixelsX,pixelsY,noise,SNR,select,OutputCSV,OutputMP4)
else:
	print("insufficent arguments to FrequencyClusterer.py")
print("Processing caller is finished. Returning to graphic interface.")