import pandas as pd
import numpy as np
import csv
import time
"""
with open('Position.csv') as posFile:
	

	

"""
start_time = time.time()
with open('Position.csv') as csvfile:
	readCSV = np.asarray(list(csv.reader(csvfile, delimiter=','))[1:], dtype=np.float32)
	#readCSV = pd.read_csv(csvfile,converters={"ï»¿TimeX":float, "X":float,"TimeY":float, "Y":float}).to_numpy()
	#print(readCSV[1])
elapsed_time = time.time() - start_time
print(elapsed_time)