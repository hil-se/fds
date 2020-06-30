import my_preprocess
import pandas as pd
from collections import Counter

if __name__ == "__main__":
    #  Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm",	"SepalWidthCm",	"PetalLengthCm",	"PetalWidthCm"]
    X = data_train[independent]
    y = data_train["Species"]

    X_norm = my_preprocess.normalize(X)
    X_pca = my_preprocess.pca(X_norm, n_components=2)
    sample = my_preprocess.stratified_sampling(y, ratio = 0.5, replacement = False)
    X_sample = X_pca[sample]
    y_sample = np.asarray(y)[sample]
    print(X_sample)
    print(Counter(y_sample))

