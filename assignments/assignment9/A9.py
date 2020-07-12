from my_GA import my_GA
import pandas as pd
####### import my_DT and my_evaluation#######
import sys
sys.path.insert(0,'..')
from assignment2.my_DT import my_DT
from assignment8.my_evaluation import my_evaluation
##################################################

def obj_func1(predictions, actuals, pred_proba=None):
    # Two objectives: higher recall and lower false positive rate
    eval = my_evaluation(predictions, actuals, pred_proba)
    return [eval.recall(), - eval.fpr()]

def obj_func2(predictions, actuals, pred_proba=None):
    # Two objectives: higher recall and lower false positive rate
    eval = my_evaluation(predictions, actuals, pred_proba)
    return eval.f1()

if __name__ == "__main__":
    # Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm",	"SepalWidthCm",	"PetalLengthCm", "PetalWidthCm"]
    X = data_train[independent]
    y = data_train["Species"]
    # Multi-objective
    ga = my_GA(my_DT, X, y, [("gini", "entropy"), [1, 16], [0, 0.1]], obj_func1, generation_size = 10, crossval_fold = 2, max_generation = 10, max_life = 2)
    frontier = ga.tune()
    objs = [ga.evaluate(decision) for decision in frontier]
    print(objs)
    # Single objective
    ga2 = my_GA(my_DT, X, y, [("gini", "entropy"), [1, 16], [0, 0.1]], obj_func2, generation_size=10, crossval_fold=2,
               max_generation=10, max_life=2)
    best = ga2.tune()
    print(ga2.evaluate(best))

    
    

