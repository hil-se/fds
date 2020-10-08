## Evaluation

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the assignment8 folder. 

### Build your own evaluation methods

#### Implement every function in [my_evaluation.py](https://github.com/hil-se/fds/blob/master/assignments/assignment8/my_evaluation.py)
Hint: compute self.confusion once and use it to calculate other metrics (except for auc).

### Test my_evaluation Algorithm with [A8.py](https://github.com/hil-se/fds/blob/master/assignments/assignment8/A8.py)

Expected output:
```
(base) zhe@Zhe-Yus-MacBook-Pro assignment8 % python A8.py 
{'Iris-setosa': {'prec': 1.0, 'recall': 0.8823529411764706, 'f1': 0.9375, 'auc': 1.0}, 'Iris-versicolor': {'prec': 0.8979591836734694, 'recall': 0.9777777777777777, 'f1': 0.9361702127659575, 'auc': 0.98}, 'Iris-virginica': {'prec': 0.975609756097561, 'recall': 0.8888888888888888, 'f1': 0.9302325581395349, 'auc': 0.9587654320987653}}
Average F1 scores: 
{'macro': 0.9366382634408452, 'micro': 0.9555555555555556, 'weighted': 0.9366382634408452}

```

### Do not forget to push your local changes to the Github server.

 
 ## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A7.py successfully runs and evaluates the performance.
 - The rest 3 points will be given based on the percentage of the same performance metrics with the correct implementation.

## Hint
 - If my_evaluation.py is too difficult to implement, you can try to complete [my_evaluation_hint.py](https://github.com/hil-se/fds/blob/master/assignments/assignment8/my_evaluation_hint.py).
 - Then, remember to rename it as my_evaluation_hint.py before submitting. 
