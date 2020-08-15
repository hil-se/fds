## K Nearest Neighbor

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the assignment4 folder. 

### Build your own kNN classifier (with continuous input)

#### Implement my_KNN.fit() function in [my_KNN.py](https://github.com/hil-se/fds/blob/master/assignments/assignment4/my_KNN.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type
- y: list, np.array or pd.Series, dependent variables, each value is a category of int or str type

#### Implement my_KNN.predict() function in [my_KNN.py](https://github.com/hil-se/fds/blob/master/assignments/assignment4/my_KNN.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_KNN.predict_proba() function in [my_KNN.py](https://github.com/hil-se/fds/blob/master/assignments/assignment4/my_KNN.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Prediction probabilities of each input data point belonging to each categories. pd.DataFrame(list of prob, columns = self.classes_).

Example:
- self.classes_ = {"2", "1"}
- the 5 nearest neighbors for the test data point have labels of {"1":4, "2":1}
- then the prob for that data point is {"1": 4/5, "2": 1/5}
- return probs = pd.DataFrame(list of prob, columns = self.classes_)

### Test my_KNN classifier with [A4.py](https://github.com/hil-se/fds/blob/master/assignments/assignment4/A4.py)


### Do not forget to push your local changes to the Github server.

 
 ## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A4.py successfully runs and makes predictions.
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.

