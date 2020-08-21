## K-Means Clustering

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the assignment6 folder. 

### Build your own K-Means Clustering Algorithm (with continuous input)

#### Hint: memorize the calculated distances to avoid redundant computations.

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

### Do not forget to push your local changes to the Github server.

 
 ## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A6.py successfully runs and makes predictions.
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.
