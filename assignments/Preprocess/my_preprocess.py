import numpy as np
from scipy.linalg import svd


class my_normalizer:
    def __init__(self, norm="Min-Max", axis = 1):
        #     norm = {"L1", "L2", "Min-Max", "Standard_Score"}
        #     axis = 0: normalize rows
        #     axis = 1: normalize columns
        self.norm = norm
        self.axis = axis

    def fit(self, X):
        #     X: input matrix
        #     Calculate offsets and scalers which are used in transform()
        X_array  = np.asarray(X)
        # Write your own code below

    def transform(self, X):
        # Transform X into X_norm
        X_norm = deepcopy(np.asarray(X))
        # Write your own code below
        return X_norm

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

class my_pca:
    def __init__(self, n_components = 5):
        #     n_components: number of principal components to keep
        self.n_components = n_components

    def fit(self, X):
        #  Use svd to perform PCA on X
        #  Inputs:
        #     X: input matrix
        #  Calculates:
        #     self.principal_components: the top n_components principal_components
        U, s, Vh = svd(X)
        # Write your own code below

    def transform(self, X):
        #     X_pca = X.dot(self.principal_components)
        X_array = np.asarray(X)
        # Write your own code below

        return X_pca

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

def stratified_sampling(y, ratio, replace = True):
    #  Inputs:
    #     y: class labels
    #     0 < ratio < 1: number of samples = len(y) * ratio
    #     replace = True: sample with replacement
    #     replace = False: sample without replacement
    #  Output:
    #     sample: indices of stratified sampled points
    #             (ratio is the same across each class,
    #             samples for each class = int(np.ceil(ratio * # data in each class)) )

    if ratio<=0 or ratio>=1:
        raise Exception("ratio must be 0 < ratio < 1.")
    y_array = np.asarray(y)
    # Write your own code below


    return sample.astype(int)
