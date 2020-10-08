import my_preprocess
import pandas as pd
from collections import Counter
from sklearn.tree import DecisionTreeClassifier

##################################################

if __name__ == "__main__":
    # Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    X = data_train[independent]
    y = data_train["Species"]
    # Preprocess (train)
    X_norm = my_preprocess.normalize(X)
    principal_components = my_preprocess.pca(X_norm, n_components=2)
    X_pca = X_norm.dot(principal_components)
    sample = my_preprocess.stratified_sampling(y, ratio=0.5, replace=False)

    X_sample = X_pca[sample]
    y_sample = y[sample].to_numpy()
    print(X_pca)
    print(Counter(y_sample))
    print(Counter(y))
    # Fit model
    clf = DecisionTreeClassifier()
    clf.fit(X_sample, y_sample)
    # Load testing data
    data_test = pd.read_csv("../data/Iris_test.csv")
    X_test = data_test[independent]
    # Preprocess (test)
    X_test_norm = my_preprocess.normalize(X_test)
    X_test_pca = X_test_norm.dot(principal_components)
    # Predict
    predictions = clf.predict(X_test_pca)
    # Output predictions on test data
    print(predictions)



