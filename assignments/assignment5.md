[<img width=900 src="https://github.com/hil-se/fds/blob/master/img/title.png?raw=yes">](https://github.com/hil-se/fds/blob/master/README.md)   
[Syllabus](https://github.com/hil-se/fds/blob/master/README.md) |
[Slides and Assignments](https://github.com/hil-se/fds/blob/master/assignments/README.md) |
[Project](https://github.com/hil-se/fds/blob/master/assignments/project.md) |
[Lecturer](http://zhe-yu.github.io) 


## K Nearest Neighbor

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the NearestNeighbor folder. 

### Build your own kNN classifier (with continuous input)

#### Implement my_KNN.fit() function in [my_KNN.py](https://github.com/hil-se/fds/blob/master/assignments/NearestNeighbor/my_KNN.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type
- y: list, np.array or pd.Series, dependent variables, each value is a category of int or str type

#### Implement my_KNN.predict() function in [my_KNN.py](https://github.com/hil-se/fds/blob/master/assignments/NearestNeighbor/my_KNN.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_KNN.predict_proba() function in [my_KNN.py](https://github.com/hil-se/fds/blob/master/assignments/NearestNeighbor/my_KNN.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Prediction probabilities of each input data point belonging to each categories. pd.DataFrame(list of prob, columns = self.classes_).

Example:
- self.classes_ = {"2", "1"}
- the 5 nearest neighbors for the test data point have labels of {"1":4, "2":1}
- then the prob for that data point is {"1": 4/5, "2": 1/5}
- return probs = pd.DataFrame(list of prob, columns = self.classes_)

### Test my_KNN classifier with [A5.py](https://github.com/hil-se/fds/blob/master/assignments/NearestNeighbor/A5.py)
 - It is expected to perform the same with [sklearn.neighbors.KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) with inputs algorithm = 'brute'.
 - Expected output:
 ```
 (base) zhe@Zhe-Yus-MacBook-Pro NearestNeighbor % python A5.py 
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
Iris-virginica  0.600000
Iris-virginica  1.000000
Iris-virginica  1.000000
Iris-virginica  0.800000
 ```
 


### Do not forget to push your local changes to the Github server.

 
 ## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A5.py successfully runs and makes predictions.
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.

## Hint
 - If my_KNN.py is too difficult to implement, you can try to complete [my_KNN_hint.py](https://github.com/hil-se/fds/blob/master/assignments/NearestNeighbor/my_KNN_hint.py).
 - Then, remember to rename it as my_KNN.py before submitting.
