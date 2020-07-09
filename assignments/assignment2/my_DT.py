import pandas as pd

class my_DT:

    def __init__(self, criterion="gini", max_depth=8, min_impurity_decrease=0, min_samples_split=2, min_samples_leaf=1):
        # criterion = {"gini", "entropy"},
        # Do not split and stop training if
        # (1) depth > max_depth after split (when only the root, depth = 0)
        # (2) the decrease of impurity < min_impurity_decrease
        # Only split node with >= min_samples_split samples
        # to leaves with >= min_samples_leaf samples
        self.criterion = criterion
        self.max_depth = int(max_depth)
        self.min_impurity_decrease = min_impurity_decrease
        self.min_samples_split = int(min_samples_split)
        self.min_samples_leaf = int(min_samples_leaf)

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
        # Eample:
        # self.classes_ = {"2", "1"}
        # the reached node for the test data point has {"1":2, "2":1}
        # then the prob for that data point is {"2": 1/3, "1": 2/3}
        # return probs = pd.DataFrame(list of prob, columns = self.classes_)
        # write your code below

        ##################
        assert(all(probs.keys()==self.classes_))
        return probs



