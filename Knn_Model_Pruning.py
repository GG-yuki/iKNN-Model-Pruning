#!/usr/bin/python
from scipy.spatial.distance import pdist, squareform, euclidean
import numpy as np

from Cal_Formula import Cal_Pruning_Threshold as C_P_T
from Cal_Formula import Cal_Class_Contribution as C_C_C

# KNN-MODEL-PRUNING

def main():
    # Get Pruning Threshold.
    W_S = C_P_T.Cal_Pruning_Threshold('./knn-data.txt')

    # get data to pruning.
    data = np.genfromtxt(data_file, delimiter=" ", skip_header=False)




if __name__ == '__main__':
    main()