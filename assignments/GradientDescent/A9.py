from my_Logistic import my_Logistic
import pandas as pd
import numpy as np

if __name__ == "__main__":
    #  Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm",	"SepalWidthCm",	"PetalLengthCm", "PetalWidthCm"]
    X = data_train[independent]
    # Learn a binary classifier to predict whether Species = Iris-setosa
    y = np.array([1 if label == "Iris-setosa" else 0 for label in data_train["Species"]])
    # Train model
    clf = my_Logistic()
    clf.fit(X,y)
    # Load testing data
    data_test = pd.read_csv("../data/Iris_test.csv")
    X_test = data_test[independent]
    # Predict
    predictions = clf.predict(X_test)
    # Predict probabilities
    probs = clf.predict_proba(X_test)
    # Print results
    for i,pred in enumerate(predictions):
        print("%s\t%f" %(pred, probs[i]))