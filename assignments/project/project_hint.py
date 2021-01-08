import pandas as pd
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import time
import sys
from pdb import set_trace
##################################
sys.path.insert(0,'../..')
from assignments.assignment8.my_evaluation import my_evaluation
from assignments.assignment9.my_GA import my_GA

class my_model():

    def obj_func(self, predictions, actuals, pred_proba=None):
        # One objectives: higher f1 score
        eval = my_evaluation(predictions, actuals, pred_proba)
        return [eval.f1()]

    def fit(self, X, y):
        # do not exceed 29 mins
        self.preprocessor = TfidfVectorizer(stop_words='english', norm='l2', use_idf=False, smooth_idf=False)
        XX = self.preprocessor.fit_transform(X["description"])
        XX = pd.DataFrame(XX.toarray())
        ga = my_GA(SGDClassifier, XX, y, [("hinge", "log", "perceptron"), ("l2", "l1"), [0.0001, 0.01]], self.obj_func, generation_size=10,
                    crossval_fold=2,
                    max_generation=10, max_life=2)
        best = ga.tune()[0]
        self.clf = SGDClassifier(*best)
        self.clf.fit(XX,y)
        return

    def predict(self, X):
        # remember to apply the same preprocessing in fit() on test data before making predictions
        XX = self.preprocessor.transform(X["description"])
        predictions = self.clf.predict(XX)
        return predictions
