[<img width=900 src="https://github.com/hil-se/fds/blob/master/img/title.png?raw=yes">](https://github.com/hil-se/fds/blob/master/README.md)   
[Syllabus](https://github.com/hil-se/fds/blob/master/README.md) |
[Slides and Assignments](https://github.com/hil-se/fds/blob/master/assignments/README.md) |
[Project](https://github.com/hil-se/fds/blob/master/assignments/project.md) |
[Lecturer](http://zhe-yu.github.io) 

## Logistic Regression Classifier

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the GradientDescent folder. 

### Build your own Logistic Regression classifier (with continuous input)

#### Implement my_Logistic.fit() function in [my_Logistic.py](https://github.com/hil-se/fds/blob/master/assignments/GradientDescent/my_Logistic.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type
- y: list, np.array or pd.Series, dependent variables, each value is a category of int or str type

#### Implement my_Logistic.predict_proba() function in [my_Logistic.py](https://github.com/hil-se/fds/blob/master/assignments/GradientDescent/my_Logistic.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Prediction probabilities of each input data point belonging Class 1. 

### Test my_Logistic with [A9.py](https://github.com/hil-se/fds/blob/master/assignments/GradientDescent/A9.py)
 - Expected output:
 ```
 (base) zhe@Zhe-Yus-MacBook-Pro GradientDescent % python A9.py
1       0.959597
1       0.990158
1       0.987047
1       0.982002
1       0.964758
0       0.022389
0       0.037106
0       0.043690
0       0.035361
0       0.030809
0       0.000313
0       0.006016
0       0.002477
0       0.001903
0       0.007916
 ```

### Do not forget to push your local changes to the Github server.

 
## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A9.py successfully runs and makes predictions.
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.
 
## Hint
 - If my_Logistic.py is too difficult to implement, you can try to complete [my_Logistic_hint.py](https://github.com/hil-se/fds/blob/master/assignments/GradientDescent/my_Logistic_hint.py).
 - Then, remember to rename it as my_Logistic.py before submitting.

