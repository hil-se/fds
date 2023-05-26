[<img width=900 src="https://github.com/hil-se/fds/blob/master/img/title.png?raw=yes">](https://github.com/hil-se/fds/blob/master/README.md)   
[Syllabus](https://github.com/hil-se/fds/blob/master/README.md) |
[Slides and Assignments](https://github.com/hil-se/fds/blob/master/assignments/README.md) |
[Project](https://github.com/hil-se/fds/blob/master/assignments/project.md) |
[Lecturer](http://zhe-yu.github.io) 

## Decision Tree Classifier

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the DecisionTree folder. 

### Build your own decision tree classifier (with continuous input)

#### Expectation
my_DT.py should behave the same as the [DecisionTreeClassifier in sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier) with the same set of inputs.

#### Implement my_DT.fit() function in [my_DT.py](https://github.com/hil-se/fds/blob/master/assignments/DecisionTree/my_DT.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type
- y: list, np.array or pd.Series, dependent variables, each value is a category of int or str type

#### Implement my_DT.predict() function in [my_DT.py](https://github.com/hil-se/fds/blob/master/assignments/DecisionTree/my_DT.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_DT.predict_proba() function in [my_DT.py](https://github.com/hil-se/fds/blob/master/assignments/DecisionTree/my_DT.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Prediction probabilities of each input data point belonging to each categories. pd.DataFrame(list of prob, columns = self.classes_).

Example:
- self.classes_ = {"2", "1"}
- the reached node for the test data point has {"1":2, "2":1}
- then the prob for that data point is {"2": 1/3, "1": 2/3}
- return probs = pd.DataFrame(list of prob, columns = self.classes_)


### Test my_DT decision tree classifier with [A6.py](https://github.com/hil-se/fds/blob/master/assignments/DecisionTree/A6.py)
 - It is expected to perform the same with [sklearn.tree.DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html).
 - Expected output:
 ```
 (base) zhe@Zhe-Yus-MacBook-Pro DecisionTree % python A6.py
['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-versicolor', 'Iris-virginica', 'Iris-virginica', 'Iris-virginica', 'Iris-virginica', 'Iris-virginica']
Iris-setosa     1.000000
Iris-setosa     1.000000
Iris-setosa     1.000000
Iris-setosa     1.000000
Iris-setosa     1.000000
Iris-versicolor 1.000000
Iris-versicolor 1.000000
Iris-versicolor 1.000000
Iris-versicolor 1.000000
Iris-versicolor 1.000000
Iris-virginica  1.000000
Iris-virginica  1.000000
Iris-virginica  1.000000
Iris-virginica  1.000000
Iris-virginica  1.000000

 ```

### Do not forget to push your local changes to the Github server.

 
## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A6.py successfully runs and makes predictions.
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.
 
## Hint
 - If my_DT.py is too difficult to implement, you can try to complete [my_DT_hint.py](https://github.com/hil-se/fds/blob/master/assignments/DecisionTree/my_DT_hint.py).
 - [my_DT_hint.py](https://github.com/hil-se/fds/blob/master/assignments/DecisionTree/my_DT_hint.py) has the main functions already implemented. Students only need to complete two functions---find_best_split() and impurity().
 - Then, remember to rename it as my_DT.py before submitting.

