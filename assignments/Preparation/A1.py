from sklearn.naive_bayes import GaussianNB
import pandas as pd

if __name__ == "__main__":
    #  Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm",	"SepalWidthCm",	"PetalLengthCm",	"PetalWidthCm"]
    X = data_train[independent]
    Y = data_train["Species"]
    # Train model
    clf = GaussianNB()
    clf.fit(X,Y)
    # Load testing data
    data_test = pd.read_csv("../data/Iris_test.csv")
    X_test = data_test[independent]
    # Predict
    predictions = clf.predict(X_test)
    # Predict probabilities
    probs = clf.predict_proba(X_test)
    # Print results
    for i,pred in enumerate(predictions):
        print("%s\t%f" %(pred,max(probs[i])))