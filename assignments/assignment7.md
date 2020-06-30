## Preprocessing

### Build your own preprocessors

#### Implement my_KMeans.fit() function in [my_KMeans.py](https://github.com/hil-se/fds/blob/master/assignments/assignment6/my_KMeans.py)
Inputs:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

#### Implement my_KMeans.predict() function in [my_KMeans.py](https://github.com/hil-se/fds/blob/master/assignments/assignment6/my_KMeans.py)
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- Predicted categories of each input data point. List of str or int.

#### Implement my_KMeans.transform() function in [my_KMeans.py](https://github.com/hil-se/fds/blob/master/assignments/assignment6/my_KMeans.py)
Transform to cluster-distance space.
Input:
- X: pd.DataFrame, independent variables, each value is a continuous number of float type

Output:
- dists = list of [dist to centroid 1, dist to centroid 2, ...]

### Test my_KMeans Algorithm with [A6.py](https://github.com/hil-se/fds/blob/master/assignments/assignment6/A6.py)

