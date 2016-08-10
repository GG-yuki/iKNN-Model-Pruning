#!usr/bin/python
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
	et_list = class_contribution.Cal_Class_Contribution('./knn-data.txt')

	print et_list


if __name__ == '__main__':
	main()