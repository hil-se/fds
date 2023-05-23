[<img width=900 src="https://github.com/hil-se/fds/blob/master/img/title.png?raw=yes">](https://github.com/hil-se/fds/blob/master/README.md)   
[Syllabus](https://github.com/hil-se/fds/blob/master/README.md) |
[Slides and Assignments](https://github.com/hil-se/fds/blob/master/assignments/README.md) |
[Project](https://github.com/hil-se/fds/blob/master/assignments/project.md) |
[Lecturer](http://zhe-yu.github.io) 

## AdaBoost (Ensemble Learning)

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the Ensemble folder. 

### Build your own AdaBoost Ensemble Learner (with continuous input)

#### Implement my_AdaBoost.fit() function in [my_AdaBoost.py](https://github.com/hil-se/fds/blob/master/assignments/Ensemble/my_AdaBoost.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type
- y: list, np.array or pd.Series, dependent variables, int or str

#### Implement my_AdaBoost.predict() function in [my_AdaBoost.py](https://github.com/hil-se/fds/blob/master/assignments/Ensemble/my_AdaBoost.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_AdaBoost.predict_proba() function in [my_AdaBoost.py](https://github.com/hil-se/fds/blob/master/assignments/Ensemble/my_AdaBoost.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- probs = pd.DataFrame(list of prob, columns = self.classes_)
- prob: what percentage of the base estimators predict input as class C
- prob(x)[C] = sum(alpha[j] * (base_model[j].predict(x) == C))

### Test AdaBoost Algorithm with [A7.py](https://github.com/hil-se/fds/blob/master/assignments/Ensemble/A7.py)

 - It is expected to perform the same with [sklearn.ensemble.AdaBoostClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html) with inputs algorithm = 'SAMME'.
 - Example output:
 ```
 (base) zhe@Zhe-Yus-MacBook-Pro Ensemble % python A7.py 
Iris-setosa     0.609665
Iris-setosa     0.609665
Iris-setosa     0.609665
Iris-setosa     0.609665
Iris-setosa     0.609665
Iris-versicolor 0.687878
Iris-versicolor 0.597522
Iris-versicolor 0.597522
Iris-versicolor 0.687878
Iris-versicolor 0.687878
Iris-virginica  0.612101
Iris-virginica  0.501838
Iris-virginica  0.612101
Iris-virginica  0.612101
Iris-virginica  0.501838
 ```
**Results can be slightly different due to randomness.**

### Do not forget to push your local changes to the Github server.

 
## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A7.py successfully runs and makes predictions.
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.
 

## Hint
 - If my_AdaBoost.py is too difficult to implement, you can try to complete [my_AdaBoost_hint.py](https://github.com/hil-se/fds/blob/master/assignments/Ensemble/my_AdaBoost_hint.py).
 - Then, remember to rename it as my_AdaBoost.py before submitting. 
