[<img width=900 src="https://github.com/hil-se/fds/blob/master/img/title.png?raw=yes">](https://github.com/hil-se/fds/blob/master/README.md)   
[Syllabus](https://github.com/hil-se/fds/blob/master/README.md) |
[Slides and Assignments](https://github.com/hil-se/fds/blob/master/assignments/README.md) |
[Project](https://github.com/hil-se/fds/blob/master/assignments/project.md) |
[Lecturer](http://zhe-yu.github.io) 

## Hyperparameter Tuning

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the Tuning folder. 

### Make sure your A8 are correct

A10 utilizes my_evaluation in A8. Make sure they are correct before working on A10.

### Build your own Genetic Algorithm for tuning model parameters

#### Implement every function in [my_GA.py](https://github.com/hil-se/fds/blob/master/assignments/Tuning/my_GA.py)
Hint: check how [A10.py](https://github.com/hil-se/fds/blob/master/assignments/Tuning/A10.py) utilizes my_GA.py to tune my_DT learner.

### Test my_evaluation Algorithm with [A10.py](https://github.com/hil-se/fds/blob/master/assignments/Tuning/A10.py)
Example output:
```
(base) zhe@Zhe-Yus-MacBook-Pro Tuning % python A10.py
[array([0.9553351 , 0.95858508]), array([0.95626124, 0.95786008]), array([0.95663662, 0.95663662])]
[0.95776608]
```
Results can be quite different due to randomness. You can try executing it multiple times.

### Do not forget to push your local changes to the Github server.
 
## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A10.py successfully runs and finds a parameter set.
 - The rest 3 points will be given based on the correctness of the implementation (TA will examine it manually).

## Hint
 - If my_GA.py is too difficult to implement, you can try to complete [my_GA_hint.py](https://github.com/hil-se/fds/blob/master/assignments/Tuning/my_GA_hint.py).
 - Then, remember to rename it as my_GA.py before submitting. 
 
 


