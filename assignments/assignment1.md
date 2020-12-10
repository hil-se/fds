[<img width=900 src="https://github.com/hil-se/fds/blob/master/img/title.png?raw=yes">](https://github.com/hil-se/fds/blob/master/README.md)   
[Syllabus](https://github.com/hil-se/fds/blob/master/README.md) |
[Slides and Assignments](https://github.com/hil-se/fds/blob/master/assignments/README.md) |
[Project](https://github.com/hil-se/fds/blob/master/assignments/project.md) |
[Lecturer](http://zhe-yu.github.io) 

 ## Assignment 1
 - 0. Watch this repo to get notified for new issues.
 ![](https://github.com/hil-se/fds/blob/master/img/watch.png?raw=yes)
 - 1. Clone this repo to your local machine (Do **NOT** do this inside your DSCI-633 directory):
 ```
 git clone https://github.com/hil-se/fds.git
 ```
 - 2. Copy ONLY the folder [assignments/](https://github.com/hil-se/fse/tree/master/assignments/) from this repo to your repo **DSCI-633** folder. 
 ```
 fds/
 |-- assignments   ---
 |-- ***             |
 DSCI-633/           |
 |-- assignments  <---
 ```
 Inside the **DSCI-633** repo, it should look like [mine](https://github.com/azhe825/DSCI-633).
 **Clarification: this is just for using the assignment code in your own repo. Just copy and paste from local directories, do not try to link these two repos in any way.**
 - 3. Run [A1.py](https://github.com/hil-se/fds/blob/master/assignments/assignment1/A1.py):
 ```
 DSCI-633/assignments/assignment1> python A1.py
 Iris-setosa     1.000000
 Iris-setosa     1.000000
 Iris-setosa     1.000000
 Iris-setosa     1.000000
 Iris-setosa     1.000000
 Iris-versicolor 0.992155
 Iris-versicolor 0.999921
 Iris-versicolor 0.999999
 Iris-versicolor 0.997254
 Iris-versicolor 0.999990
 Iris-virginica  1.000000
 Iris-virginica  0.840581
 Iris-virginica  0.999999
 Iris-virginica  0.999988
 Iris-virginica  0.753482
 ```
 - 4. Modify [A1.py](https://github.com/hil-se/fds/blob/master/assignments/assignment1/A1.py) so that a Decision Tree Classifier is used to make the prediction instead of Gaussian Naive Bayes. Use the [Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier) from scikit-learn directly (without any specific parameters).
 - 5. Run A1.py again and snapshot the output (including the command *python A1.py*). 
 - 6. Save the snapshot as A1.png and put it under *assignments/assignment1/* in your repo. Should look like [this](https://github.com/azhe825/DSCI-633/tree/master/assignments/assignment1). Note: the [example snapshot](https://github.com/azhe825/DSCI-633/tree/master/assignments/assignment1/A1.png) will look different from the correct one since it uses the Gaussian Naive Bayes classifier.
 - 7. Commit to the remote server of Github.
 
 ## Grading Policy
 - 6 (out of 7) points will be received if all the required files can be found in the submitted repo.
 - The rest 1 point will be given based on whether the screenshot A1.png is correct.
 - **Note:** be sure to add your github repo url to the [Google sheet](https://docs.google.com/spreadsheets/d/1Kyuqa3Seh_noWsjBam3bHcfzmbwp7eWhAr-Qw4eCkqI/edit?usp=sharing) since this is how this and all the future assignments will be graded.
 
 
