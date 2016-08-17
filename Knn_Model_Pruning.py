#!/usr/bin/python
from scipy.spatial.distance import pdist, squareform, euclidean
import numpy as np

from Cal_Formula import Cal_Pruning_Threshold as C_P_T
from Cal_Formula import Cal_Class_Contribution as C_C_C

# KNN-MODEL-PRUNING

def main():
    # Get Pruning Threshold.
    W_S, W_SX = C_P_T.Cal_Pruning_Threshold('./knn-data.txt')

    # get data to pruning.
    data = np.genfromtxt('./knn-data.txt', delimiter=" ", skip_header=False)

    # print W_SX
    print len(data)

    for i, W_X in enumerate(W_SX):
        if W_X < W_S:
            del data[i]

    print len(data)




if __name__ == '__main__':
    main()