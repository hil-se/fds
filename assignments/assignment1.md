## Python Basics

### 0. Learn Python basics on [Codecademy](https://www.codecademy.com/learn/learn-python) (free version)
 - Skip this step if you already know how to code in Python.

### 1. Install Python on your local machine.

 - Install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) with Python 3.7 (miniconda or anaconda).
 
### 2. Install required packages.
 - Open terminal.
 ```
 conda install scikit-learn
 conda install matplotlib
 ```
 
### 3. (Optional) Install an IDE.
 - [Pycharm](https://www.jetbrains.com/pycharm/) community version.
 

## Github Basics

### 0. Create your [Github](https://github.com/) account.
 - Skip this step if you already have one.

### 1. Create a new repository called **DSCI-633** under your Github account.
 - (1) Click on the **new** button:
 ![](https://github.com/hil-se/fse/blob/master/img/create_repo.png?raw=yes)
 
 - (2) Initiate the new repo:
 ![](https://github.com/hil-se/fse/blob/master/img/init_repo.png?raw=yes)

### 2. Clone the **DSCI-633** repo to your local machine.

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
 
