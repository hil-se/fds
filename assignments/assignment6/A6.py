from my_KMeans import my_KMeans
import pandas as pd

if __name__ == "__main__":
    #  Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm",	"SepalWidthCm",	"PetalLengthCm",	"PetalWidthCm"]
    X = data_train[independent]
    y = data_train["Species"]
    # Train model
    clf = my_KMeans(n_clusters=3)
    y_p = clf.fit_predict(X)
    # Show training results
    print("Classes:")
    print([(y[i], y_p[i]) for i in range(len(y))])
    print("Centroids:")
    print(clf.cluster_centers_)
    print("Inertia: %f" %clf.inertia_)

    # Load testing data
    data_test = pd.read_csv("../data/Iris_test.csv")
    X_test = data_test[independent]
    # Transform test data to cluster-distance space
    dists = clf.transform(X_test)
    print("Testing data:")
    print(dists)
