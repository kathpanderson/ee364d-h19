# this 

import sys
import os.path

numberOfExpectedArgs = 7
arg = sys.argv[1:]
if len(arg) = numberOfExpectedArgs:	
	save_path = arg[0]
	name_of_file = arg[1]
	Xpixels = arg[2]
	Ypixels = arg[3]
	SNRs = arg[4:]
	completeName = os.path.join(save_path, name_of_file+".tdms")
	FrequencyClusterer(completeName,Xpixels,Ypixels,SNRs)
else:
	print("insufficent arguments to FrequencyClusterer.py")
print("Processing caller is finished. Returning to graphic interface.")
