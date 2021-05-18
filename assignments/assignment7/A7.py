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
    normalizer = my_preprocess.my_normalizer(norm="L2", axis=1)
    X_norm = normalizer.fit_transform(X)
    pca = my_preprocess.my_pca(n_components=2)
    X_pca = pca.fit_transform(X_norm)
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
    X_test_norm = normalizer.transform(X_test)
    X_test_pca = pca.transform(X_test_norm)
    # Predict
    predictions = clf.predict(X_test_pca)
    # Output predictions on test data
    print(predictions)



