from my_evaluation import my_evaluation
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

##################################################

if __name__ == "__main__":
    # Load training data
    data_train = pd.read_csv("../data/Iris_train.csv")
    # Separate independent variables and dependent variables
    independent = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]
    X = data_train[independent]
    y = data_train["Species"]
    # Fit model
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=2)
    clf.fit(X, y)
    # Predict on training data
    predictions = clf.predict(X)
    print(predictions)
    # Predict probabilities
    probs = clf.predict_proba(X)
    probs = pd.DataFrame({key: probs[:, i] for i, key in enumerate(clf.classes_)})
    # Evaluate results
    metrics = my_evaluation(predictions, y, probs)
    result = {}
    for target in clf.classes_:
        result[target] = {}
        result[target]["prec"] = metrics.precision(target)
        result[target]["recall"] = metrics.recall(target)
        result[target]["f1"] = metrics.f1(target)
        result[target]["auc"] = metrics.auc(target)
    print(result)
    f1 = {average: metrics.f1(target=None, average=average) for average in ["macro", "micro", "weighted"]}
    print("Average F1 scores: ")
    print(f1)




