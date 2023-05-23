[<img width=900 src="https://github.com/hil-se/fds/blob/master/img/title.png?raw=yes">](https://github.com/hil-se/fds/blob/master/README.md)   
[Syllabus](https://github.com/hil-se/fds/blob/master/README.md) |
[Slides and Assignments](https://github.com/hil-se/fds/blob/master/assignments/README.md) |
[Project](https://github.com/hil-se/fds/blob/master/assignments/project.md) |
[Lecturer](http://zhe-yu.github.io) 

## Naive Bayes Classifier

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the NaiveBayes folder. 

### Do NOT treat "?" as missing values in this assignment. Treat it as a regular value that X can take.

### Build your own categorical Naive Bayes classifier

#### Implement my_NB.fit() function in [my_NB.py](https://github.com/hil-se/fds/blob/master/assignments/NaiveBayes/my_NB.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a category of str type
- y: list, np.array or pd.Series, dependent variables, each value is a category of int or str type

#### Implement my_NB.predict() function in [my_NB.py](https://github.com/hil-se/fds/blob/master/assignments/NaiveBayes/my_NB.py)
Input:
- X: pd.DataFrame, independent variables, each value is a category of str type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_NB.predict_proba() function in [my_NB.py](https://github.com/hil-se/fds/blob/master/assignments/NaiveBayes/my_NB.py)
Input:
- X: pd.DataFrame, independent variables, each value is a category of str type

Output:
- Prediction probabilities of each input data point belonging to each categories. pd.DataFrame(list of prob, columns = self.classes_).

### Test my_NB classifier with [A4.py](https://github.com/hil-se/fds/blob/master/assignments/NaiveBayes/A4.py)
Expected output:
```
(base) zhe@Zhe-Yus-MacBook-Pro NaiveBayes % python A4.py 
cochlear_age    0.999408
cochlear_age    0.999408
cochlear_age    0.875175
cochlear_age    0.484233
cochlear_age    0.992703
cochlear_age    0.997401
cochlear_age    0.998318
cochlear_age    0.998318
cochlear_poss_noise     0.902857
cochlear_unknown        0.611369
mixed_cochlear_unk_fixation     0.832907
mixed_cochlear_unk_fixation     0.755148
normal_ear      0.507668
normal_ear      0.990685
cochlear_age    0.997749
cochlear_age    0.992896
normal_ear      0.997311
mixed_cochlear_unk_fixation     0.930178
cochlear_age    0.982908
cochlear_age    0.996372
cochlear_age    0.959620
mixed_cochlear_unk_fixation     0.397127
normal_ear      0.997311
mixed_cochlear_unk_fixation     0.983080
cochlear_age_and_noise  0.619968
cochlear_poss_noise     0.601495
```

### Do not forget to push your local changes to the Github server.

 
 ## Grading Policy 
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A4.py successfully runs and makes predictions.
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.
 
  
## Hint
 - If my_NB.py is too difficult to implement, you can try to complete [my_NB_hint.py](https://github.com/hil-se/fds/blob/master/assignments/NaiveBayes/my_NB_hint.py).
 - [my_NB_hint.py](https://github.com/hil-se/fds/blob/master/assignments/NaiveBayes/my_NB_hint.py) has the predict() and predict_proba() functions already implemented. Students only need to complete the fit() functions.
 - Then, remember to rename it as my_NB.py before submitting.
