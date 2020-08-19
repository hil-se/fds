## Python Basics

### 0. Learn Python basics on [Codecademy](https://www.codecademy.com/learn/learn-python) (free version) and the [tutorial from the textbook](http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial1/tutorial1.html)
 - Skip this step if you already know how to code in Python.

### 1. Install Python on your local machine.

 - Install [conda](https://docs.conda.io/en/latest/miniconda.html) with Python 3.7+.
 
### 2. Install required packages.
 - Open terminal.
 ```
 conda install scikit-learn
 conda install pandas
 ```
 
### 3. (Optional) Install an IDE.
 - [Pycharm](https://www.jetbrains.com/pycharm/) community version.
 

## Github Basics

### 0. Install [Git](https://git-scm.com/downloads) and create your [Github](https://github.com/) account.
 - Skip this step if you already have one.

### 1. Create a new repository called **DSCI-633** under your Github account.
 - (1) Click on the **new** button:
 ![](https://github.com/hil-se/fse/blob/master/img/create_repo.png?raw=yes)
 
 - (2) Initiate the new repo:
 ![](https://github.com/hil-se/fse/blob/master/img/init_repo.png?raw=yes)

### 2. Clone the **DSCI-633** repo to your local machine.
 ![](https://github.com/hil-se/fse/blob/master/img/clone_repo.png?raw=yes)
 ```
 git clone THE-COPIED-URL
 ```

### 3. Save username and password in git.
 - In terminal:
 ```
 git config --global credential.helper store
 ```
 - When running this command, the first time you pull or push from the remote repository, you'll get asked about the username and password. Afterwards, for consequent communications with the remote repository you don't have to provide the username and password.

### 4. Working with a github repo.
 - (1) Go to the local directory of the **DSCI-633** repo.
 - (2) Pull from Github so that the content on your local machine is updated with the remote server of Github:
 ```
 DSCI-633> git pull
 ```
 - (3) Work on your local machine (add/remove/edit files under DSCI-633/).
 - (4) Commit to the remote server of Github (upload local changes).
 ```
 DSCI-633> git add .
 DSCI-633> git commit -m "YOUR COMMIT MESSAGE"
 DSCI-633> git push
 ```
 
 ## Assignment 1
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
 Inside the **DSCI-633** repo, it should look like the following:
 ![](https://github.com/hil-se/fse/blob/master/img/download_A1.png?raw=yes)
 - 3. Run [A1.py](https://github.com/hil-se/fds/blob/master/assignments/assignment1/A1.py):
 ```
 DSCI-633/assignment1> python A1.py
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
 - 7. Commit to the remote server of Github and add your github repo url (along with your RIT identifiers) to the [Google sheet](https://docs.google.com/spreadsheets/d/1bl-qhYIAlT9cBOxcNEQP3vyrwQL2ejUSg4kb2XoUNxM/edit?usp=sharing).
 
 ## Grading Policy
 - 6 (out of 7) points will be received if all the required files can be found in the submitted repo.
 - The rest 1 point will be given based on whether the screenshot A1.png is correct.
 - **Note:** be sure to add your github repo url to the [Google sheet](https://docs.google.com/spreadsheets/d/1bl-qhYIAlT9cBOxcNEQP3vyrwQL2ejUSg4kb2XoUNxM/edit?usp=sharing) since this is how this and all the future assignments will be graded.
 
 
