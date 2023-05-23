[<img width=900 src="https://github.com/hil-se/fds/blob/master/img/title.png?raw=yes">](https://github.com/hil-se/fds/blob/master/README.md)   
[Syllabus](https://github.com/hil-se/fds/blob/master/README.md) |
[Slides and Assignments](https://github.com/hil-se/fds/blob/master/assignments/README.md) |
[Project](https://github.com/hil-se/fds/blob/master/assignments/project.md) |
[Lecturer](http://zhe-yu.github.io) 

## K-Means Clustering

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the Kmeans folder. 

### Build your own K-Means Clustering Algorithm (with continuous input)

#### Hint: memorize the calculated distances to avoid redundant computations.

#### Implement my_KMeans.fit() function in [my_KMeans.py](https://github.com/hil-se/fds/blob/master/assignments/Kmeans/my_KMeans.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

#### Implement my_KMeans.predict() function in [my_KMeans.py](https://github.com/hil-se/fds/blob/master/assignments/Kmeans/my_KMeans.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_KMeans.transform() function in [my_KMeans.py](https://github.com/hil-se/fds/blob/master/assignments/Kmeans/my_KMeans.py)
Transform to cluster-distance space.
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- dists = list of [dist to centroid 1, dist to centroid 2, ...]

### Test my_KMeans Algorithm with [A8.py](https://github.com/hil-se/fds/blob/master/assignments/Kmeans/A8.py)

 - It is expected to perform the same with [sklearn.cluster.KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) with input (algorithm = "full").
 - Example output:
 ```
 (base) zhe@Zhe-Yus-MacBook-Pro Kmeans % python A8.py 
Classes:
[('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-setosa', 1), ('Iris-versicolor', 0), ('Iris-versicolor', 2), ('Iris-versicolor', 0), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 0), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-versicolor', 2), ('Iris-virginica', 0), ('Iris-virginica', 2), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 2), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 2), ('Iris-virginica', 0), ('Iris-virginica', 2), ('Iris-virginica', 2), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 2), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 2), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 2), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 2), ('Iris-virginica', 0), ('Iris-virginica', 0), ('Iris-virginica', 2)]
Centroids:
[array([6.825     , 3.075     , 5.68055556, 2.06111111]), array([4.97777778, 3.38      , 1.48222222, 0.24      ]), array([5.88333333, 2.75740741, 4.4037037 , 1.43888889])]
Inertia: 67.455130
Testing data:
[[5.586474379038563, 0.8771981208426503, 3.908052869279141], [5.044339664844246, 1.068503048864203, 3.6537027651065976], [4.82261183141907, 1.2601273696155961, 3.498929387499919], [4.965864184486464, 0.7123738788093484, 3.5001993868349057], [4.957914703771791, 0.19924549036828546, 3.3888580245508093], [1.3520874350790932, 3.7021808721180194, 0.7692633606053402], [2.527586989136934, 2.7754336776016526, 0.8517451624010108], [3.2197871546093912, 2.5600626921335974, 1.5372857897773275], [1.8352494195881814, 3.157342217204719, 0.3230459883088073], [2.32303115894559, 3.058454382507044, 0.8245691396832467], [1.3726804228260423, 6.1700647294361595, 2.9815959260298794], [1.0457992100084585, 4.04047974171507, 0.744055085206515], [0.26103722358844833, 4.921554507006105, 1.7546518614833146], [0.5713788283022926, 5.273953702330064, 2.146639796115343], [1.1444680418279174, 3.907873660088038, 0.6241345173499059]]
[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 0, 2, 0, 0, 2]

 ```
 Results can be different due to randomness. Inertias should be similar.

### Do not forget to push your local changes to the Github server.

 
## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A8.py successfully runs and makes predictions.
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.
 
  
## Hint
 - If my_KMeans.py is too difficult to implement, you can try to complete [my_KMeans_hint.py](https://github.com/hil-se/fds/blob/master/assignments/Kmeans/my_KMeans_hint.py).
 - Then, remember to rename it as my_KMeans.py before submitting. 
