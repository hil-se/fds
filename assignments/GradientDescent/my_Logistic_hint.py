import pandas as pd
import numpy as np

class my_Logistic:

    def __init__(self, learning_rate = 0.1, batch_size = 10, max_iter = 100, shuffle = False):
        # Logistic regression: f(x) = 1 / (1+exp(-(w0+w*x))})
        # Loss function is sum (f(x)-y)**2
        # learning_rate: Learning rate for each weight update.
        # batch_size: Number of training data points in each batch.
        # max_iter: The maximum number of passes over the training data (aka epochs). Note that this is not max batches.
        # shuffle: Whether to shuffle the data in each epoch.
        self.learning_rate = learning_rate
        self.batch_size = batch_size
        self.max_iter = max_iter
        self.shuffle = shuffle

    def fit(self, X, y):
        # X: pd.DataFrame, independent variables
        # y: list, np.array or pd.Series, dependent variables
        data = X.to_numpy()
        d = data.shape[1]
        # Initialize weights as all zeros
        self.w = np.array([0.0]*d)
        self.w0 = 0.0
        n = len(y)
        for epoch in range(self.max_iter):
            # Generate batches (list of list of indices)
            batches = self.generate_batches(n)
            for batch in batches:
                X_train = data[batch]
                y_train = y[batch]
                # Update weights
                self.w, self.w0 = self.sgd(X_train, y_train, self.w, self.w0)


    def generate_batches(self, n):
        # write your code below
        return batches

    def sgd(self, X, y, w, w0):
        # write your code below
        return w, w0


    def predict_proba(self, X):
        # X: pd.DataFrame, independent variables
        # prob is a dict of prediction probabilities belonging to each categories
        # return probs = f(x) = 1 / (1+exp(-(w0+w*x))}); a list of float values in [0.0, 1.0]
        data = X.to_numpy()
        wx = np.dot(self.w, data.transpose()) + self.w0
        fx = 1.0 / (1 + np.exp(-wx))
        return fx

    def predict(self, X):
        # X: pd.DataFrame, independent variables, str
        # return predictions: list of int values in {0, 1}
        # write your code below
        probs = self.predict_proba(X)
        predictions = [1 if prob >=0.5 else 0 for prob in probs]
        return predictions





