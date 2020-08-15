## Naive Bayes Classifier

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the assignment3 folder. 

### Build your own categorical Naive Bayes classifier

#### Implement my_NB.fit() function in [my_NB.py](https://github.com/hil-se/fds/blob/master/assignments/assignment3/my_NB.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a category of str type
- y: list, np.array or pd.Series, dependent variables, each value is a category of int or str type

#### Implement my_NB.predict() function in [my_NB.py](https://github.com/hil-se/fds/blob/master/assignments/assignment3/my_NB.py)
Input:
- X: pd.DataFrame, independent variables, each value is a category of str type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_NB.predict_proba() function in [my_NB.py](https://github.com/hil-se/fds/blob/master/assignments/assignment3/my_NB.py)
Input:
- X: pd.DataFrame, independent variables, each value is a category of str type

Output:
- Prediction probabilities of each input data point belonging to each categories. pd.DataFrame(list of prob, columns = self.classes_).

### Test my_NB classifier with [A3.py](https://github.com/hil-se/fds/blob/master/assignments/assignment3/A3.py)

### Do not forget to push your local changes to the Github server.

 
 ## Grading Policy 
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A3.py successfully runs and makes predictions.
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.
