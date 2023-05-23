from my_NB import my_NB
import pandas as pd

if __name__ == "__main__":
    #  Load training data
    data_train = pd.read_csv("../data/audiology_train",header=None)
    # Separate independent variables and dependent variables
    independent = range(69)
    X = data_train[independent]
    y = data_train[70]
    # Train model
    clf = my_NB()
    clf.fit(X,y)
    # Load testing data
    data_test = pd.read_csv("../data/audiology_test",header=None)
    X_test = data_test[independent]
    # Predict
    predictions = clf.predict(X_test)
    # Predict probabilities
    probs = clf.predict_proba(X_test)
    # Print results
    for i,pred in enumerate(predictions):
        print("%s\t%f" % (pred, probs[pred][i]))