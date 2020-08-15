## AdaBoost (Ensemble Learning)

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the assignment5 folder. 

### Build your own AdaBoost Ensemble Learner (with continuous input)

#### Implement my_AdaBoost.fit() function in [my_AdaBoost.py](https://github.com/hil-se/fds/blob/master/assignments/assignment5/my_AdaBoost.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type
- y: list, np.array or pd.Series, dependent variables, int or str

#### Implement my_AdaBoost.predict() function in [my_AdaBoost.py](https://github.com/hil-se/fds/blob/master/assignments/assignment5/my_AdaBoost.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_AdaBoost.predict_proba() function in [my_AdaBoost.py](https://github.com/hil-se/fds/blob/master/assignments/assignment5/my_AdaBoost.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- probs = pd.DataFrame(list of prob, columns = self.classes_)
- prob: what percentage of the base estimators predict input as class C
- prob(x)[C] = sum(alpha[j] * (base_model[j].predict(x) == C))

### Test my_KMeans Algorithm with [A5.py](https://github.com/hil-se/fds/blob/master/assignments/assignment5/A5.py)

### Do not forget to push your local changes to the Github server.

 
 ## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A5.py successfully runs and makes predictions.
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.
