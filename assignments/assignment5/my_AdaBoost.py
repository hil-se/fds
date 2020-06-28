import pandas as pd

class my_AdaBoost:

    def __init__(self, base_estimator = None, n_estimators = 50):
        # base_estimator: the base classifier class, e.g. my_DT
        # n_estimators: # of base_estimator rounds
        self.base_estimator = base_estimator
        self.n_estimators = n_estimators

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
        # prob: what percentage of the base estimators predict input as class i
        # prob(x)[i] = sum(alpha[j] * (base_model[j].predict(x) == self.classes_[i]))
        # return probs = list of prob(x)
        # write your code below
        return probs





