## Decision Tree Classifier

### Build your own decision tree classifier (with continuous input)

#### Implement my_DT.__init__() function in [my_DT.py](https://github.com/hil-se/fds/blob/master/assignments/assignment2/my_DT.py)
Inputs:
- criterion = {"gini", "entropy"} (implement both)
- Do not split and stop training if (1) depth > max_depth after split (2) the decrease of impurity < min_impurity_decrease
- Only split node with >= min_samples_split samples to leaves with >= min_samples_leaf samples

#### Implement my_DT.fit() function in [my_DT.py](https://github.com/hil-se/fds/blob/master/assignments/assignment2/my_DT.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type
- y: list, np.array or pd.Series, dependent variables, each value is a category of int or str type

#### Implement my_DT.predict() function in [my_DT.py](https://github.com/hil-se/fds/blob/master/assignments/assignment2/my_DT.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_DT.predict_proba() function in [my_DT.py](https://github.com/hil-se/fds/blob/master/assignments/assignment2/my_DT.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Prediction probabilities of each input data point belonging to each categories. List of list.

Example:
- self.classes_ = {"1", "2"}
- the reached node for the test data point has {"1":2, "2":1}
- then the prob for that data point is [2/3, 1/3]
- return probs = list of prob


### Test my_DT decision tree classifier with [A2.py](https://github.com/hil-se/fds/blob/master/assignments/assignment2/A2.py)

