import numpy as np
from sklearn.cluster import MeanShift
# data has been threshholded such that the 
# new structur is [[[x,y,fvalue], ...]] for the list of different frequencies indexing the internal list
def ClusterFider(threshedData,N):
	clusterCenterts = []
	for i in range(N):
    	clusterCenterts.append([])

	for i in range(N):
		ms = MeanShift()
		ms.fit(threshedData[i])
		clusterCenterts[i] = ms.cluster_centers_
	return clusterCenterts
