## Preprocessing

### Make sure your repo is up-to-date

Assignment codes might be modified during the semester so please pull from this repo first and overwrite your repo with the assignment7 folder. 

### Build your own preprocessors

#### Implement pca() function in [my_preprocess.py](https://github.com/hil-se/fds/blob/master/assignments/assignment7/my_preprocess.py)
Use svd to perform PCA on X

Inputs:
- X: input matrix
- n_components: number of principal components to keep

Output:
- X_pca: output matrix of n_components columns (numpy.array)

#### Implement normalize() function in [my_preprocess.py](https://github.com/hil-se/fds/blob/master/assignments/assignment7/my_preprocess.py)
Inputs:
 - X: input matrix
 - norm = {"L1", "L2", "Min-Max", "Standard_Score"}
 - axis = 0: normalize rows
 - axis = 1: normalize columns
 
Output:
 - X_norm: normalized matrix (numpy.array)

#### Implement stratified_sampling() function in [my_preprocess.py](https://github.com/hil-se/fds/blob/master/assignments/assignment7/my_preprocess.py)
Inputs:
 - y: class labels
 - 0 < ratio < 1: number of samples = len(y) * ratio
 - replacement = True: sample with replacement
 - replacement = False: sample without replacement
 
Output:
 - sample: indices of stratified sampled points
         (ratio is the same across each class)

### Test my_preprocess with [A7.py](https://github.com/hil-se/fds/blob/master/assignments/assignment7/A7.py)

### Do not forget to push your local changes to the Github server.

 
 ## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A7.py successfully runs and makes predictions
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.
