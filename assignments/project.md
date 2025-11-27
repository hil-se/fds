[<img width=900 src="../img/title.png?raw=yes">](../README.md)   
[Syllabus](../README.md) |
[Slides and Assignments](README.md) |
[Project](project.md) |
[Lecturer](http://zhe-yu.github.io) 

## Predict whether a job posting is real or fake

### Goal
Train a model (in [project.py](project/project.py)) to predict whether a job posting is real or fake on the provided [dataset](data/job_train.csv).

### Requirements

- Can use any model, preprocessing, tuning method. 
- Can use (but do not have to use) all information in [dataset](data/job_train.csv) to train the model.
- Make sure there is no error when executing [test.py](project/test.py) (do not modify this file).
- Total runtime < 30 min (if tuning is performed, its runtime must be included)
- Can only install packages: 
  + scikit-learn, gensim, pandas, joblib
  + packages such as numpy can be used because installing scikit-learn will also install numpy

### Note about parallelism with sklearn

If you use parallelism with sklearn, e.g.
```
self.grid_search = RandomizedSearchCV(self.pipeline, self.params, cv=3, scoring='f1', n_jobs=-1)
self.grid_search.fit(X, y)
```
Then you will need to specify to use threads instead of loky. To do this:
```
from joblib import parallel_config

with parallel_config(backend='threading', n_jobs=-1):
    self.grid_search = RandomizedSearchCV(self.pipeline, self.params, cv=3, scoring='f1', n_jobs=-1)
    self.grid_search.fit(X, y)
```

### Assessment

- F1 score for *fraudulent == 1* 

### Grading

- **Performance**
  + all submissions will be ranked by their F1 score on a test set (not given to you).
  + submissions with higher F1 score will receive higher grades.
  + points will range from 20 to 30 (as long as your algorithm successfully gives predictions, you will earn 20 points).

- **Cost**
  + for submissions with similar performances
  + those with lower runtime will receive higher grades.

- **Innovation**
  + submissions with innovative solutions (different solutions from your classmates) will receive extra points up to 3.
  + submissions with really strong innovative solutions (different solutions from the state-of-the-art) can receive extra points up to 10.
  
- **Violations**
  + submissions with runtime > 30 min on the TA's machine will have (runtime in min - 30) deducted from their earned points.
  + submissions that require extra packages will not be graded.


