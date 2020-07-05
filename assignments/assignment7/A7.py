import my_preprocess
import pandas as pd
from collections import Counter
####### Add assignment2 to sys.path to import my_DT #######
import sys
sys.path.insert(0,'../assignment2')
from my_DT import my_DT
##################################################

if __name__ == "__main__":
    # Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm",	"SepalWidthCm",	"PetalLengthCm", "PetalWidthCm"]
    X = data_train[independent]
    y = data_train["Species"]
    # Preprocess (train)
    X_norm = my_preprocess.normalize(X)
    X_pca = my_preprocess.pca(X_norm, n_components=2)
    sample = my_preprocess.stratified_sampling(y, ratio = 0.5, replacement = False)
    X_sample = X_pca[sample]
    y_sample = np.asarray(y)[sample]
    print(X_sample)
    print(Counter(y_sample))
    print(Counter(y))
    # Fit model
    clf = my_DT()
    clf.fit(X_sample, y_sample)
    # Load testing data
    data_test = pd.read_csv("../data/Iris_test.csv")
    X_test = data_test[independent]
    # Preprocess (test)
    X_test_norm = my_preprocess.normalize(X_test)
    X_test_pca = my_preprocess.pca(X_test_norm, n_components=2)
    # Predict
    predictions = clf.predict(X_test_pca)
    # Predict probabilities
    probs = clf.predict_proba(X_test_pca)
    # Print results
    for i, pred in enumerate(predictions):
        print("%s\t%f" % (pred, probs[pred][i]))
    
    

