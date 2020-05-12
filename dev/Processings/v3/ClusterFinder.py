import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets import make_blobs
import csv
# data has been threshholded such that the 
# new structur is [[[x,y,fvalue], ...]] for the list of different frequencies indexing the internal list
def ClusterFinder(threshedData,N):
	print("Start ClusterFinder")
	clusterCenterts = []
	for i in range(N):
		clusterCenterts.append([])
	
	for i in range(N):
		ms = MeanShift()
		ms.fit(np.asarray(threshedData[i]))
		clusterCenterts[i] = ms.cluster_centers_
	return clusterCenterts

def main():
	centers1 = [[1,1,1],[5,5,5],[3,9,10]]
	X1, _ = make_blobs(n_samples = 100, centers = centers1, cluster_std = 1.5)
	centers2 = [[3,3,3],[8,8,8],[2,3,1]]
	X2, _ = make_blobs(n_samples = 100, centers = centers2, cluster_std = 1.5)

	threshedData = [centers1,centers2]
	N =2
	OutputCSV = "TESTING_CVS_HERE.csv"
	clusterCenterts = ClusterFinder(threshedData,N)

	with open(OutputCSV, 'w', newline='') as myfile:
			wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
			wr.writerow(["TEST DATA"])
			for row in clusterCenterts:
				wr.writerow(row)

if __name__ == '__main__':
    main()
