from my_evaluation import my_evaluation
import pandas as pd
####### Add assignment2 to sys.path to import my_DT #######
import sys
sys.path.insert(0,'../assignment2')
from my_DT import my_DT
##################################################

if __name__ == "__main__":
    # Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm",	"SepalWidthCm",	"PetalLengthCm", "PetalWidthCm"]
    X = data_train[independent]
    y = data_train["Species"]
    # Fit model
    clf = my_DT()
    clf.fit(X, y)
    # Predict on training data
    predictions = clf.predict(X)
    # Predict probabilities
    probs = clf.predict_proba(X)
    # Evaluate results
    metrics = my_evaluation(predictions, y, probs)
    result = {}
    for target in clf.classes_:
        result[target] = {}
        result[target]["prec"] = metrics.prec(target)
        result[target]["recall"] = metrics.recall(target)
        result[target]["f1"] = metrics.f1(target)
        result[target]["fpr"] = metrics.fpr(target)
        result[target]["auc"] = metrics.auc(target)
    print(result)
    f1 = {average: metrics.f1(target=None, average=average) for average in ["macro", "micro", "weighted"]}
    print("Average F1 scores: ")
    print(f1)

    
    

