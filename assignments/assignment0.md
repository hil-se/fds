[<img width=900 src="../img/title.png?raw=yes">](../README.md)   
[Syllabus](../README.md) |
[Slides and Assignments](README.md) |
[Project](project.md) |
[Lecturer](http://zhe-yu.github.io) 


## Java Basics


### 1. Install Java on your local machine.

 - Install [java](https://www.oracle.com/java/technologies/downloads/).
 

### 2. (Optional) Install an IDE.
 - [IntelliJ](https://lp.jetbrains.com/intellij-idea-promo/).
 

## Github Basics

### 0. Install [Git](https://git-scm.com/downloads) and create your [Github](https://github.com/) account.
 - Skip this step if you already have one.

### 1. Create a new PRIVATE repository called **DSCI-640** under your Github account.
 - (1) Click on the **new** button
 
 - (2) Initiate the new private repo
 
 - (3) Invite the instructor and the TA as collaborators (GitHub ID: **azhe825, manojb01**):
 ![](../img/invite.png?raw=yes)

### 2. Clone the created private repo to your local machine.
 ```
 git clone THE-COPIED-URL
 ```
### 3. Clone this repo to your local machine (Do **NOT** do this inside your DSCI-640 directory):
 ```
 git clone https://github.com/hil-se/DSCI-640-Neural-Networks.git
 ```
 - 2. Copy ONLY the folder [assignments/](./) from this repo to your repo **DSCI-640** folder. 
 ```
 DSCI-640-Neural-Networks/
 |-- assignments   ---
 |-- ***             |
 DSCI-640/           |
 |-- assignments  <---
 ```
 Inside the **DSCI-640** repo, it should look like [mine](https://github.com/azhe825/DSCI-640).
 **Clarification: this is just for using the assignment code in your own repo. Just copy and paste from local directories, do not try to link these two repos in any way.**

### 3. Save username and token in git.
 - Create your personal access token on [this page](https://github.com/settings/tokens)
 - Copy the generated token.
 - In terminal:
 ```
 git config --global credential.helper manager
 ```
 - When running this command, the first time you pull or push from the remote repository, you'll get asked about the username and your token (NOT Password!). Afterwards, for consequent communications with the remote repository you don't have to provide the username and password.

### 4. Working with a github repo.
 - (1) Go to the local directory of the **DSCI-640** repo.
 - (2) Pull from Github so that the content on your local machine is updated with the remote server of Github:
 ```
 DSCI-640> git pull
 ```
 - (3) Work on your local machine (add/remove/edit files under DSCI-633/).
 - (4) Commit to the remote server of Github (upload local changes).
 ```
 DSCI-640> git add .
 DSCI-640> git commit -m "YOUR COMMIT MESSAGE"
 DSCI-640> git push
 ```
 
 ### 5. Add your information to [Google sheet](https://docs.google.com/spreadsheets/d/17XxiRqrSp0bvztRgT61FM9p2riNgRTXacuDON0dml0U/edit?usp=sharing)
 - Add your github repo url (along with your RIT identifier and Github ID) to the Google sheet.
 - Make a self-evaluation on your current knowledge/expertise in coding, Python, and machine learning. This information will ONLY be used to decide your study group.
