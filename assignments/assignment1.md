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
 - 3. Run [A1.py](https://github.com/hil-se/fds/blob/master/assignments/Preparation/A1.py):
 ```
 DSCI-633/assignments/assignment1> python A1.py
SepalLengthCm            5.0
SepalWidthCm             3.0
PetalLengthCm            1.6
PetalWidthCm             0.2
Species          Iris-setosa
Name: 20, dtype: object
0         Iris-setosa
1         Iris-setosa
2         Iris-setosa
3         Iris-setosa
4         Iris-setosa
            ...
130    Iris-virginica
131    Iris-virginica
132    Iris-virginica
133    Iris-virginica
134    Iris-virginica
Name: Species, Length: 135, dtype: object
    SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species
0             5.1           3.5            1.4           0.2  Iris-setosa
1             4.9           3.0            1.4           0.2  Iris-setosa
2             4.7           3.2            1.3           0.2  Iris-setosa
3             4.6           3.1            1.5           0.2  Iris-setosa
4             5.0           3.6            1.4           0.2  Iris-setosa
5             5.4           3.9            1.7           0.4  Iris-setosa
6             4.6           3.4            1.4           0.3  Iris-setosa
7             5.0           3.4            1.5           0.2  Iris-setosa
8             4.4           2.9            1.4           0.2  Iris-setosa
9             4.9           3.1            1.5           0.1  Iris-setosa
10            5.4           3.7            1.5           0.2  Iris-setosa
11            4.8           3.4            1.6           0.2  Iris-setosa
12            4.8           3.0            1.4           0.1  Iris-setosa
13            5.7           3.8            1.7           0.3  Iris-setosa
14            5.1           3.8            1.5           0.3  Iris-setosa
15            5.4           3.4            1.7           0.2  Iris-setosa
16            5.1           3.7            1.5           0.4  Iris-setosa
17            4.6           3.6            1.0           0.2  Iris-setosa
18            5.1           3.3            1.7           0.5  Iris-setosa
19            4.8           3.4            1.9           0.2  Iris-setosa
20            5.0           3.0            1.6           0.2  Iris-setosa
21            5.0           3.4            1.6           0.4  Iris-setosa
22            5.2           3.5            1.5           0.2  Iris-setosa
23            5.2           3.4            1.4           0.2  Iris-setosa
24            4.7           3.2            1.6           0.2  Iris-setosa
25            4.8           3.1            1.6           0.2  Iris-setosa
26            5.4           3.4            1.5           0.4  Iris-setosa
27            5.2           4.1            1.5           0.1  Iris-setosa
28            5.5           4.2            1.4           0.2  Iris-setosa
29            4.9           3.1            1.5           0.1  Iris-setosa
30            5.0           3.2            1.2           0.2  Iris-setosa
31            5.5           3.5            1.3           0.2  Iris-setosa
32            4.9           3.1            1.5           0.1  Iris-setosa
33            4.4           3.0            1.3           0.2  Iris-setosa
34            5.1           3.4            1.5           0.2  Iris-setosa
35            5.0           3.5            1.3           0.3  Iris-setosa
36            4.5           2.3            1.3           0.3  Iris-setosa
37            4.4           3.2            1.3           0.2  Iris-setosa
38            5.0           3.5            1.6           0.6  Iris-setosa
39            5.1           3.8            1.9           0.4  Iris-setosa
40            4.8           3.0            1.4           0.3  Iris-setosa
41            5.1           3.8            1.6           0.2  Iris-setosa
42            4.6           3.2            1.4           0.2  Iris-setosa
43            5.3           3.7            1.5           0.2  Iris-setosa
44            5.0           3.3            1.4           0.2  Iris-setosa
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
 - 4. Modify [A1.py](https://github.com/hil-se/fds/blob/master/assignments/Preparation/A1.py) to print out the 12th training data point.
 - 5. Modify [A1.py](https://github.com/hil-se/fds/blob/master/assignments/Preparation/A1.py) to print out the "SepalWidthCm" column.
 - 6. Modify [A1.py](https://github.com/hil-se/fds/blob/master/assignments/Preparation/A1.py) to print out training data points with "SepalWidthCm" < 2.5.
 - 7. Modify [A1.py](https://github.com/hil-se/fds/blob/master/assignments/Preparation/A1.py) so that a Decision Tree Classifier is used to make the prediction instead of Gaussian Naive Bayes. Use the [Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier) from scikit-learn directly (without any specific parameters).
 - 8. Run A1.py again and snapshot the output (including the command *python A1.py*). 
 - 9. Save the snapshot as A1.png and put it under *assignments/assignment1/* in your repo. Should look like [this](https://github.com/azhe825/DSCI-633/tree/master/assignments/Preparation). Note: the [example snapshot](https://github.com/azhe825/DSCI-633/tree/master/assignments/Preparation/A1.png) will look different from the correct one.
 - 10. Commit to the remote server of Github.
 
 ## Grading Policy
 - 6 (out of 7) points will be received if all the required files can be found in the submitted repo.
 - The rest 1 point will be given based on whether the screenshot A1.png is correct.
 - **Note:** be sure to add your github repo url to the [Google sheet](https://docs.google.com/spreadsheets/d/1K-6ivZQALvivG2IOwIXAXR3Vh46nlwasxV0KAIZVzCM/edit?usp=sharing) since this is how this and all the future assignments will be graded.
 
 
