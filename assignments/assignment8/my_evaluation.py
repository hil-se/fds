import numpy as np
import pandas as pd

class my_evaluation:
    # Binary class or multi-class classification evaluation
    # Each data point can only belong to one class

    def __init__(self, predictions, actuals, pred_proba=None):
        # inputs:
        # predictions: list of predicted classes
        # actuals: list of ground truth
        # pred_proba: pd.DataFrame of prediction probability of belonging to each class
        self.predictions = predictions
        self.actuals = actuals
        self.pred_proba = pred_proba
        if self.pred_proba:
            self.classes_ = self.pred_proba.keys()
        else:
            self.classes_ = list(set(list(self.predictions)+list(self.actuals)))
        self.confusion = None

    def confusion(self):
        # compute confusion matrix for each class in self.classes_
        # self.confusion = {self.classes_[i]: {"TP":tp, "TN": tn, "FP": fp, "FN": fn}}
        # no return variables
        # write your own code below
        return

    def prec(self, target=None, average = "macro"):
        # compute precision
        # target: target class (str). If not None, then return precision of target class
        # average: {"macro", "micro", "weighted"}. If target==None, return average precision
        # output: prec = float
        # note: be careful for divided by 0
        # write your own code below
        return self.predictions

    def recall(self, target=None, average = "macro"):
        # compute recall
        # target: target class (str). If not None, then return recall of target class
        # average: {"macro", "micro", "weighted"}. If target==None, return average recall
        # output: recall = float
        # note: be careful for divided by 0
        # write your own code below
        return recall

    def f1(self, target=None, average = "macro"):
        # compute f1
        # target: target class (str). If not None, then return f1 of target class
        # average: {"macro", "micro", "weighted"}. If target==None, return average f1
        # output: f1 = float
        # note: be careful for divided by 0
        # write your own code below
        return f1

    def fpr(self, target=None, average = "macro"):
        # compute false positive rate
        # target: target class (str). If not None, then return fpr of target class
        # average: {"macro", "micro", "weighted"}. If target==None, return average fpr
        # output: fpr = float
        # note: be careful for divided by 0
        # write your own code below
        return fpr

    def auc(self, target):
        # compute AUC of ROC curve for each class
        # return auc = {self.classes_[i]: auc_i}, dict
        if self.pred_proba==None:
            return None
        else:
            # write your own code below
            return auc


