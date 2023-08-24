[<img width=900 src="https://github.com/hil-se/fds/blob/master/img/title.png?raw=yes">](https://github.com/hil-se/fds/blob/master/README.md)   
[Syllabus](https://github.com/hil-se/fds/blob/master/README.md) |
[Slides and Assignments](https://github.com/hil-se/fds/blob/master/assignments/README.md) |
[Project](https://github.com/hil-se/fds/blob/master/assignments/project.md) |
[Instructor](http://zhe-yu.github.io) 

## Predict whether a job posting is real or fake

### Goal
Train a model (in [project.py](https://github.com/hil-se/fds/blob/master/assignments/project/project.py)) to predict whether a job posting is real or fake on the provided [dataset](https://github.com/hil-se/fds/blob/master/assignments/data/job_train.csv).

### Requirements

- Can use any model, preprocessing, tuning method. 
- Can use (but do not have to use) all information in [dataset](https://github.com/hil-se/fds/blob/master/assignments/data/job_train.csv) to train the model.
- Make sure there is no error when executing [test.py](https://github.com/hil-se/fds/blob/master/assignments/project/test.py) (do not modify this file).
- Total runtime < 30 min (if tuning is performed, its runtime must be included)
- Can only install packages: 
  + scikit-learn, gensim, pandas 
  + packages such as numpy can be used because installing scikit-learn will also install numpy
  
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


