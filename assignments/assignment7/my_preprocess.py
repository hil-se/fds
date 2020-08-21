import numpy as np
from scipy.linalg import svd

def pca(X, n_components = 5):
    #  Use svd to perform PCA on X
    #  Inputs:
    #     X: input matrix
    #     n_components: number of principal components to keep
    #  Output:
    #     X_pca: output matrix of n_components columns (numpy.array)
    #  Write your own code below:
    U, s, Vh = svd(X)
    return X_pca

def normalize(X, norm="Min-Max", axis = 1):
    #  Inputs:
    #     X: input matrix
    #     norm = {"L1", "L2", "Min-Max", "Standard_Score"}
    #     axis = 0: normalize rows
    #     axis = 1: normalize columns
    #  Output:
    #     X_norm: normalized matrix (numpy.array)
    #  Write your own code below:
    X_array = np.asarray(X)
    return X_norm

def stratified_sampling(y, ratio, replacement = True):
    #  Inputs:
    #     y: class labels
    #     0 < ratio < 1: number of samples = len(y) * ratio
    #     replacement = True: sample with replacement
    #     replacement = False: sample without replacement
    #  Output:
    #     sample: indices of stratified sampled points
    #             (ratio is the same across each class, 
    #             samples for each class = np.ceil(ratio * # data in each class) )
    #  Write your own code below:
    y_array = np.asarray(y)
    return sample
