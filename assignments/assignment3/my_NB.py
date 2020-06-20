import pandas as pd

class my_NB:

    def __init__(self):
        pass

    def fit(self, X, y):
        # X: pd.DataFrame, independent variables, float
        # y: list, np.array or pd.Series, dependent variables, int or str
        self.classes_ = list(set(list(y)))
        # write your code below
        return

    def predict(self, X):
        # X: pd.DataFrame, independent variables, float
        # return predictions: list
        # write your code below
        return predictions

    def predict_proba(self, X):
        # X: pd.DataFrame, independent variables, float
        # prob is a list of probabilities following the order of self.classes_
        # return probs = list of prob
        # write your code below
        return probs



