import numpy as np
import matplotlib.pyplot as plt
import csv

#lvmName = "DtTest.lvm"
lvmName = "Sinewaves.lvm"
numOfChannels = 3
Channels = []
for i in range(0,numOfChannels):
	Channels.append([])

file = open(lvmName, "r")
endIndex = 0
for line in file:
	lineClean = line.strip()
	if endIndex == 2:
		if lineClean =='':
			endIndex +=1
			break
		lineSplit = lineClean.split(',')
		#print(lineSplit)
		Channels[0].append(lineSplit[1])
		#Channels[1].append(lineSplit[2])
		#Channels[2].append(lineSplit[3])
		#Channels[3].append(lineSplit[4])
	if lineClean.find('***')!=-1:
		endIndex += 1
#print(len(Channels[1]))
#print(Channels[0][1::5][0:2000])
#fig = plt.figure(figsize=(10,10))
#plt.plot(Channels[0][1::5][0:2000])
#plt.show()

with open('csvOUT.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(Channels[0])