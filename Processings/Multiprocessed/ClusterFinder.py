# data has been threshholded such that the 
# new structur is [[[x,y,fvalue], ...]] for the list of different frequencies indexing the internal list
import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets import make_blobs
import csv
from multiprocessing import Pool
import os

def mainFinder(element):
	ms = MeanShift()
	ms.fit(np.asarray(element))
	print("Hi I'm process " + str(os.getpid()))
	return ms.cluster_centers_

def ClusterFinder(threshedData,N):
	print("Start ClusterFinder")
	clusterCenterts = []
	for i in range(N):
		clusterCenterts.append([])
	
# 	for i in range(N):
# 		ms = MeanShift()
# 		ms.fit(np.asarray(threshedData[i]))
# 		clusterCenterts[i] = ms.cluster_centers_
	with Pool() as pool:
		clusterCenterts = pool.map(mainFinder, (threshedData[i] for i in range(N)))

	return clusterCenterts

def main():
	centers1 = [[1,1,1],[5,5,5],[3,9,10]]
	X1, _ = make_blobs(n_samples = 100, centers = centers1, cluster_std = 1.5)
	centers2 = [[3,3,3],[8,8,8],[2,3,1]]
	X2, _ = make_blobs(n_samples = 100, centers = centers2, cluster_std = 1.5)
	centers3 = [[2, 4, 7], [6, 6, 6], [9, 9, 9]]
	X3, _ = make_blobs(n_samples = 100, centers = centers3, cluster_std = 1.5)
	centers4 = [[3,3,3],[8,8,8],[2,3,1]]
	X4, _ = make_blobs(n_samples = 100, centers = centers4, cluster_std = 1.5)
	centers5 = [[3,3,3],[8,8,8],[2,3,1]]
	X5, _ = make_blobs(n_samples = 100, centers = centers5, cluster_std = 1.5)
	centers6 = [[3,3,3],[8,8,8],[2,3,1]]
	X6, _ = make_blobs(n_samples = 100, centers = centers6, cluster_std = 1.5)
	centers7 = [[3,3,3],[8,8,8],[2,3,1]]
	X7, _ = make_blobs(n_samples = 100, centers = centers7, cluster_std = 1.5)
	centers8 = [[3,3,3],[8,8,8],[2,3,1]]
	X8, _ = make_blobs(n_samples = 100, centers = centers8, cluster_std = 1.5)

	threshedData = [centers1,centers2,centers3,centers4,centers5,centers6,centers7,centers8]
	N =8
	OutputCSV = "TESTING_CVS_HERE.csv"
	clusterCenterts = ClusterFinder(threshedData,N)

	with open(OutputCSV, 'w', newline='') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow(["TEST DATA"])
			for row in clusterCenterts:
				wr.writerow(row)

if __name__ == '__main__':
    main()