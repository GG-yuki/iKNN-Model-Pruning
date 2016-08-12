#!usr/bin/python
from __future__ import division  
from scipy.spatial.distance import pdist, squareform, euclidean
from sklearn.cross_validation import KFold
import numpy as np
import time

from Cal_Formula import Cal_Class_Contribution as class_contribution

# Calculate Pruning Threshold ==> W(S) / m
# 
# Step 1: Calculate each of data to W(xi)
# Step 2: W(S) / m = W(x1) + W(x2) + W(x3)... + W(xm)

# Input  : et_list[[n+1][T]] from file `Cal_Class_Contribution.py`
#		 : data from file `./knn-data.txt`
#
# Output : W(S) / m  which is KNN-MODEL Pruning Threshold.

def main():

	et_list,feature_hash_table = class_contribution.Cal_Class_Contribution('./knn-data.txt')

	data = np.genfromtxt('./knn-data.txt', delimiter=" ", skip_header=False)
	m = len(data)

	# autosum in Format 5. 
	# autosum means from c,d = 1,1 to R,n ==> 1/etij
	autosum = np.sum(et_list)

	w_sx = []
	i = 0

	for labels in data:
		label = int(labels[-1])
		w_x = 0
		n = len(labels) - 1

    	for j,feature in enumerate(labels[:-1]):
    		# midsum means tij / R * n
    		midsum = feature_hash_table.get("{0} {1}".format(label, j)) / (m * n)
    		# rightsum means (1/etij) / autosum
    		if et_list[i][j] == 0:
    			continue
    		else:
    			rightsum = (1 / et_list[i][j]) / autosum
    			w_sx.append(1+midsum+rightsum)
        i+=1


	# sum of W(S) / m
	w_sum = 0
	for x in w_sx:
		w_sum += x

	print w_sum / m

	# return W(S)
	return w_sum / m


if __name__ == '__main__':
	main()