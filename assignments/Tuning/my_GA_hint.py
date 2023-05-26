import numpy as np
import pandas as pd
from pdb import set_trace


class my_GA:
    # Tuning with Genetic Algorithm for model parameters

    def __init__(self, model, data_X, data_y, decision_boundary, obj_func, generation_size=100, selection_rate=0.5,
                 mutation_rate=0.01, crossval_fold=5, max_generation=100, max_life=3):
        # inputs:
        # model: class object of the learner under tuning, e.g. my_DT
        # data_X: training data independent variables (pd.Dataframe, csr_matrix or np.array)
        # data_y: training data dependent variables (pd.Series or list)
        # decision_boundary: a dictionary of boundaries of each decision variable,
        # e.g. decision_boundary = {"criterion": ("gini", "entropy"), "max_depth": [1, 16], "min_impurity_decrease": [0, 0.1]} for my_DT means:
        # the first argument criterion can be chosen as either "gini" or "entropy"
        # the second argument max_depth can be any number 1 <= max_depth < 16
        # the third argument min_impurity_decrease can be any number 0 <= min_impurity_decrease < 0.1
        # obj_func: generate objectives, all objectives are higher the better
        # generation_size: number of points in each generation
        # selection_rate: percentage of survived points after selection, only affect single objective
        # mutation_rate: probability of being mutated for each decision in each point
        # crossval_fold: number of fold in cross-validation (for evaluation)
        # max_generation: early stopping rule, stop when reached
        # max_life: stopping rule, stop when max_life consecutive generations do not improve
        self.model = model
        self.data_X = data_X
        self.data_y = data_y
        # self.decision_keys stores keys of decision_boundary
        self.decision_keys = list(decision_boundary.keys())
        # self.decision_boundary stores values of decision_boundary
        self.decision_boundary = list(decision_boundary.values())
        self.obj_func = obj_func
        self.generation_size = int(generation_size)
        self.selection_rate = selection_rate  # applies only to singe-objective
        self.mutation_rate = mutation_rate
        self.crossval_fold = int(crossval_fold)
        self.max_generation = int(max_generation)
        self.max_life = int(max_life)
        self.life = self.max_life
        self.iter = 0
        self.generation = []
        self.pf_best = []
        self.evaluated = {None: -1}

    def initialize(self):
        # Randomly generate generation_size points to self.generation
        # If boundary in self.decision_boundary is integer, the generated
        #  value must also be integer.

        self.generation = []
        for _ in range(self.generation_size):
            x = []
            for boundary in self.decision_boundary:
                if type(boundary) == list:
                    val = np.random.random() * (boundary[1] - boundary[0]) + boundary[0]
                    if type(boundary[0]) == int:
                        val = round(val)
                    x.append(val)
                else:
                    x.append(boundary[np.random.randint(len(boundary))])
            self.generation.append(tuple(x))
        ######################
        # check if size of generation is correct
        assert (len(self.generation) == self.generation_size)
        return self.generation

    def evaluate(self, decision):
        # Evaluate a certain point
        # decision: tuple of decisions
        # Avoid repetitive evaluations
        if decision not in self.evaluated:
            # evaluate with self.crossval_fold fold cross-validation on self.data_X and self.data_y
            dec_dict = {key: decision[i] for i, key in enumerate(self.decision_keys)}
            clf = self.model(**dec_dict)
            # write your own code below
            # Cross validation:
            indices = [i for i in range(len(self.data_y))]
            np.random.shuffle(indices)
            size = int(np.ceil(len(self.data_y) / float(self.crossval_fold)))
            objs_crossval = []
            for fold in range(self.crossval_fold):
                start = int(fold * size)
                end = start + size
                test_indices = indices["write your own code"]
                train_indices = indices["write your own code"] + indices["write your own code"]
                X_train = self.data_X.loc[train_indices]
                X_train.index = range(len(X_train))
                X_test = self.data_X.loc[test_indices]
                X_test.index = range(len(X_test))
                y_train = self.data_y.loc[train_indices]
                y_train.index = range(len(y_train))
                y_test = self.data_y.loc[test_indices]
                y_test.index = range(len(y_test))
                clf.fit(X_train, y_train)
                predictions = "write your own code"
                try:
                    pred_proba = "write your own code"
                except:
                    pred_proba = None
                actuals = "write your own code"
                objs = np.array(self.obj_func(predictions, actuals, pred_proba))
                objs_crossval.append(objs)
            # Take a mean of each fold of the cross validation result
            # objs_crossval should become an 1-d array of the same size as objs
            objs_crossval = "write your own code"
            self.evaluated[decision] = objs_crossval
        return self.evaluated[decision]

    def is_better(self, a, b):
        # Check if decision a binary dominates decision b
        # Return 0 if a == b,
        # Return 1 if a binary dominates b,
        # Return -1 if a does not binary dominates b.
        if a == b:
            return 0
        obj_a = self.evaluate(a)
        obj_b = self.evaluate(b)
        # write your own code below
        if "write your own code":
            return 1
        else:
            return -1

    def compete(self, pf_new, pf_best):
        # Compare and merge two pareto frontiers
        # If one point y in pf_best is binary dominated by another point x in pf_new
        # (exist x and y; self.is_better(x, y) == 1)
        # replace that point y in pf_best with the point x in pf_new
        # If one point x in pf_new is not dominated by any point y in pf_best (and does not exist in pf_best)
        # (forall y in pf_best; self.is_better(y, x) == -1)
        # add that point x to pf_best
        # Return True if pf_best is modified in the process, otherwise return False
        # Write your own code below
        modified = False
        for i in range(len(pf_best)):
            for j in range(len(pf_new)):
                if "write your own code":
                    pf_best[i] = pf_new[j]
                    pf_new.pop(j)
                    modified = True
                    break
        to_add = []
        for j in range(len(pf_new)):
            not_dominated = True
            for i in range(len(pf_best)):
                if "write your own code":
                    not_dominated = False
                    break
            if not_dominated:
                to_add.append(j)
                modified = True
        for j in to_add:
            pf_best.append(pf_new[j])
        return modified

    def select(self):
        # Select which points will survive based on the objectives
        # Update the following:
        # self.pf = pareto frontier (undominated points from self.generation)
        # self.generation = survived points

        # single-objective:
        if len(self.evaluate(self.generation[0])) == 1:
            selected = np.argsort([self.evaluate(x)[0] for x in self.generation])[::-1][
                       :int(np.ceil(self.selection_rate * self.generation_size))]
            self.pf = [self.generation[selected[0]]]
            self.generation = [self.generation[i] for i in selected]
        # multi-objective:
        else:
            self.pf = []
            for x in self.generation:
                if not np.array([self.is_better(y, x) == 1 for y in self.generation]).any():
                    self.pf.append(x)
            # remove duplicates
            self.pf = list(set(self.pf))
            # Add second batch undominated points into next generation if only one point in self.pf
            if len(self.pf) == 1:
                self.generation.remove(self.pf[0])
                next_pf = []
                for x in self.generation:
                    if not np.array([self.is_better(y, x) == 1 for y in self.generation]).any():
                        next_pf.append(x)
                next_pf = list(set(next_pf))
                self.generation = self.pf + next_pf
            else:
                self.generation = self.pf[:]

    def crossover(self):
        # randomly select two points in self.generation
        # and generate a new point
        # repeat until self.generation_size points were generated
        # Write your own code below
        def cross(a, b):
            new_point = []
            for i in range(len(a)):
                if "write your own code":
                    new_point.append(a[i])
                else:
                    new_point.append(b[i])
            return tuple(new_point)

        to_add = []
        for _ in range(self.generation_size - len(self.generation)):
            ids = np.random.choice(len(self.generation), 2, replace=False)
            new_point = cross(self.generation[ids[0]], self.generation[ids[1]])
            to_add.append(new_point)
        self.generation.extend(to_add)
        ######################
        # check if size of generation is correct
        assert (len(self.generation) == self.generation_size)
        return self.generation

    def mutate(self):
        # Uniform random mutation:
            # each decision value in each point of self.generation
            # has the same probability self.mutation_rate of being mutated
            # to a random valid value
        # If boundary in self.decision_boundary is integer, the mutated
        #  value must also be integer.
        # write your own code below

        for i, x in enumerate(self.generation):
            new_x = list(x)
            for j in range(len(x)):
                if np.random.random() < self.mutation_rate:
                    boundary = self.decision_boundary[j]
                    if type(boundary) == list:
                        val = "write your own code"
                        if type(boundary[0]) == int:
                            val = round(val)
                        new_x[j] = val
                    else:
                        new_x[j] = "write your own code"
            self.generation[i] = tuple(new_x)
        return self.generation

    def tune(self):
        # Main function of my_GA
        # Stop when self.iter == self.max_generation or self.life == 0
        # Return the best pareto frontier pf_best (list of decisions that never get binary dominated by any candidate evaluated)
        self.initialize()
        while self.life > 0 and self.iter < self.max_generation:
            self.select()
            # If any better than current best
            if self.compete(self.pf, self.pf_best):
                self.life = self.max_life
            else:
                self.life -= 1
            self.iter += 1
            self.crossover()
            self.mutate()
        return self.pf_best



