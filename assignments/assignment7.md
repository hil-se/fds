[<img width=900 src="https://github.com/hil-se/fds/blob/master/img/title.png?raw=yes">](https://github.com/hil-se/fds/blob/master/README.md)   
[Syllabus](https://github.com/hil-se/fds/blob/master/README.md) |
[Slides and Assignments](https://github.com/hil-se/fds/blob/master/assignments/README.md) |
[Project](https://github.com/hil-se/fds/blob/master/assignments/project.md) |
[Lecturer](http://zhe-yu.github.io) 

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
Expected output:
```
(base) zhe@zhe-yus-mbp assignment7 % python A7.py 
[[-4.02412365e-01 -5.53625050e-01]
 [-2.80684541e-01 -3.28001783e-01]
 [-2.81780612e-01 -4.24248126e-01]
 [-2.68275973e-01 -3.69891801e-01]
 [-4.07711338e-01 -5.99373471e-01]
 [-5.94194937e-01 -6.92860481e-01]
 [-3.38909190e-01 -4.97354462e-01]
 [-3.79405850e-01 -5.04018225e-01]
 [-1.93757318e-01 -2.84926652e-01]
 [-2.85666050e-01 -3.81750613e-01]
 [-4.90535728e-01 -6.38144650e-01]
 [-3.61698309e-01 -5.00159822e-01]
 [-2.43655785e-01 -3.41642788e-01]
 [-5.92681332e-01 -6.59416420e-01]
 [-4.92049332e-01 -6.71588711e-01]
 [-4.52828434e-01 -4.92737031e-01]
 [-4.96569699e-01 -6.13090381e-01]
 [-3.15285005e-01 -6.20153666e-01]
 [-4.63382771e-01 -4.09184432e-01]
 [-3.90203934e-01 -4.85911322e-01]
 [-3.13293000e-01 -3.18057234e-01]
 [-4.35755821e-01 -4.72877811e-01]
 [-4.25518949e-01 -5.48430001e-01]
 [-3.97113392e-01 -5.07876628e-01]
 [-3.10286238e-01 -4.09999625e-01]
 [-3.04987265e-01 -3.64251204e-01]
 [-4.80672779e-01 -4.75845117e-01]
 [-5.15516989e-01 -8.33442696e-01]
 [-5.89156968e-01 -8.68962966e-01]
 [-2.85666050e-01 -3.81750613e-01]
 [-3.13092862e-01 -4.27660980e-01]
 [-4.47329323e-01 -5.56592356e-01]
 [-2.85666050e-01 -3.81750613e-01]
 [-2.03159125e-01 -3.34979025e-01]
 [-3.93010559e-01 -5.03572677e-01]
 [-4.02729829e-01 -5.45624641e-01]
 [-1.07862111e-01 -4.21790960e-03]
 [-2.40966488e-01 -4.25584771e-01]
 [-5.01507598e-01 -4.91789769e-01]
 [-5.53480880e-01 -6.39395253e-01]
 [-2.90503881e-01 -3.15251874e-01]
 [-4.78127160e-01 -6.80034668e-01]
 [-2.77677779e-01 -4.19944174e-01]
 [-4.76931020e-01 -6.38590198e-01]
 [-3.51000294e-01 -4.63464853e-01]
 [-1.19884123e+00 -9.41720187e-02]
 [-1.12163328e+00 -9.31488530e-02]
 [-1.20876064e+00 -2.66202369e-02]
 [-7.34700299e-01  2.60428651e-01]
 [-1.06912514e+00  9.32576871e-02]
 [-9.03937498e-01  5.85528844e-02]
 [-1.16936005e+00 -1.16202817e-01]
 [-5.35190462e-01  1.39619615e-01]
 [-1.01968781e+00  3.77266631e-02]
 [-8.23719595e-01 -2.99410382e-02]
 [-1.11061780e+00 -6.44542919e-02]
 [-9.74988248e-01 -6.10749549e-03]
 [-7.90358882e-01  4.57169338e-02]
 [-9.05387047e-01  3.58988779e-01]
 [-7.29762400e-01  1.39128039e-01]
 [-1.15238750e+00 -4.15417237e-02]
 [-9.10846956e-01  3.65875779e-02]
 [-1.01371030e+00  2.42523709e-01]
 [-9.53936034e-01  5.66386217e-02]
 [-9.99070388e-01  6.86985099e-03]
 [-1.07810941e+00 -1.95969675e-02]
 [-1.10551896e+00  9.08978758e-02]
 [-1.21899751e+00  4.89319533e-02]
 [-1.01050340e+00  4.09775715e-02]
 [-7.00839241e-01  6.20772573e-02]
 [-6.87752135e-01  1.79235864e-01]
 [-6.54826212e-01  1.61290906e-01]
 [-8.18203227e-01  6.26088479e-02]
 [-1.05313134e+00  1.73275775e-01]
 [-9.47778832e-01 -6.99859254e-03]
 [-1.12844586e+00 -1.72341336e-01]
 [-1.16254747e+00 -3.70103343e-02]
 [-8.81545466e-01  2.82991040e-01]
 [-8.90132652e-01 -5.14964104e-02]
 [-7.72507662e-01  1.69822905e-01]
 [-8.05994796e-01  1.30322576e-01]
 [-1.02908962e+00 -1.23257099e-02]
 [-8.08801420e-01  1.12661221e-01]
 [-5.29891488e-01  1.85368036e-01]
 [-8.42923483e-01  8.91617084e-02]
 [-8.89815188e-01 -5.94968189e-02]
 [-8.94335554e-01 -9.98488837e-04]
 [-9.71860971e-01  5.97875394e-03]
 [-5.76221982e-01  9.41547955e-02]
 [-8.65929998e-01  3.95548839e-02]
 [-1.50370085e+00  6.42997993e-02]
 [-1.09619406e+00  2.11971050e-01]
 [-1.45262941e+00  1.46241477e-01]
 [-1.22611029e+00  1.34145090e-01]
 [-1.38492333e+00  1.52014143e-01]
 [-1.58716608e+00  1.81715721e-01]
 [-8.32084979e-01  2.43678943e-01]
 [-1.42867050e+00  1.71847076e-01]
 [-1.22391815e+00  3.26637776e-01]
 [-1.69235615e+00 -6.28493824e-02]
 [-1.30936948e+00  1.77098219e-03]
 [-1.19682606e+00  2.24143341e-01]
 [-1.37380779e+00  1.25906831e-01]
 [-1.05870416e+00  3.10577204e-01]
 [-1.23221798e+00  2.32645463e-01]
 [-1.38504066e+00  5.04108054e-02]
 [-1.26272152e+00  8.49838141e-02]
 [-1.78492616e+00 -1.62316756e-01]
 [-1.60050978e+00  4.04012176e-01]
 [-9.25687006e-01  3.81845182e-01]
 [-1.49107170e+00  7.16365486e-02]
 [-1.09230862e+00  1.69473537e-01]
 [-1.15129143e+00  5.47046192e-02]
 [-1.29108346e+00  2.19479883e-01]
 [-1.33961201e+00  7.59602399e-02]
 [-1.42779183e+00  2.21291955e-01]
 [-1.73678186e+00 -2.02065074e-01]
 [-1.31450751e+00  2.32675340e-01]
 [-1.08942509e+00  1.16114091e-01]
 [-1.04849364e+00  2.16380783e-01]
 [-1.60010951e+00  1.84804683e-01]
 [-1.46117299e+00 -1.31965313e-02]
 [-1.26802049e+00  3.92353927e-02]
 [-1.12818485e+00  4.95095705e-02]
 [-1.39681430e+00  7.63000067e-02]
 [-1.45888078e+00  1.24494281e-01]
 [-1.41515677e+00  8.84424207e-02]
 [-1.09619406e+00  2.11971050e-01]
 [-1.49647074e+00  8.06900004e-02]
 [-1.52961406e+00  5.18334930e-02]
 [-1.37854555e+00  1.37603697e-01]
 [-1.11690837e+00  3.00055038e-01]
 [-1.28106399e+00  9.71262281e-02]
 [-1.40514048e+00 -3.63365372e-02]
 [-1.14308577e+00  6.33125224e-02]]
Counter({'Iris-setosa': 23, 'Iris-versicolor': 23, 'Iris-virginica': 23})
Counter({'Iris-setosa': 45, 'Iris-versicolor': 45, 'Iris-virginica': 45})
['Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa'
 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor' 'Iris-versicolor'
 'Iris-versicolor' 'Iris-virginica' 'Iris-virginica' 'Iris-virginica'
 'Iris-virginica' 'Iris-virginica']

```
Predictions results can be a little bit different due to randomness in stratified sampling (but should be very similar).


### Do not forget to push your local changes to the Github server.

 
 ## Grading Policy
 - importing additional packages such as sklearn is not allowed.
 - 4 (out of 7) points will be received if A7.py successfully runs and makes predictions
 - The rest 3 points will be given based on the percentage of same predictions with the correct implementation.
 
   
## Hint
 - If my_preprocess.py is too difficult to implement, you can try to complete [my_preprocess_hint.py](https://github.com/hil-se/fds/blob/master/assignments/assignment7/my_preprocess_hint.py).
 - Then, remember to rename it as my_preprocess_hint.py before submitting. 
