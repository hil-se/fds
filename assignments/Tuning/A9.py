from my_GA import my_GA
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
####### import my_evaluation#######
import sys
sys.path.insert(0, '../..')
from assignments.Evaluation.my_evaluation import my_evaluation

##################################################

def obj_func1(predictions, actuals, pred_proba=None):
    # Two objectives: higher recall, higher precision
    eval = my_evaluation(predictions, actuals, pred_proba)
    return [eval.recall(), eval.precision()]

def obj_func2(predictions, actuals, pred_proba=None):
    # One objectives: higher f1 score
    eval = my_evaluation(predictions, actuals, pred_proba)
    return [eval.f1()]

if __name__ == "__main__":
    # Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    X = data_train[independent]
    y = data_train["Species"]
    # Multi-objective
    ga = my_GA(DecisionTreeClassifier, X, y,
               {"criterion": ("gini", "entropy"), "max_depth": [1, 16], "min_impurity_decrease": [0, 0.1]}, obj_func1,
               generation_size=10, crossval_fold=2, max_generation=10, max_life=2)
    frontier = ga.tune()
    objs = [ga.evaluate(decision) for decision in frontier]
    print(objs)
    # Single objective
    ga2 = my_GA(DecisionTreeClassifier, X, y,
                {"criterion": ("gini", "entropy"), "max_depth": [1, 16], "min_impurity_decrease": [0, 0.1]}, obj_func2,
                generation_size=10, crossval_fold=2,
                max_generation=10, max_life=2)
    best = ga2.tune()
    print(ga2.evaluate(best[0]))




