import pandas as pd
import time

class my_model():
    def fit(self, X, y):
        # do not exceed 29 mins
        return

    def predict(self, X):
        # remember to apply the same preprocessing in fit() on test data before making predictions
        return predictions

if __name__ == "__main__":
    start = time.time()
    # Load data
    data = pd.read_csv("../data/job_train.csv")
    # Replace missing values with empty strings
    data = data.fillna("")
    y = data["fraudulent"]
    X = data.drop(['fraudulent'], axis=1)
    # Train model
    clf = my_model()
    clf.fit(X, y)
    runtime = (time.time() - start) / 60.0
    print(runtime)
    predictions = clf.predict(X)
    print(predictions)






