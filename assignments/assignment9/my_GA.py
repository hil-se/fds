import numpy as np
import pandas as pd


class my_GA:
    # Tuning with Genetic Algorithm for model parameters

    def __init__(self, model, data_X, data_y, decision_boundary, obj_func, generation_size=100, selection_rate=0.5, mutation_rate=0.01, crossval_fold=5, max_generation=100, max_life=3):
        # inputs:
        # model: class object of the learner under tuning, e.g. my_DT
        # data_X: training data independent variables (pd.Dataframe)
        # data_y: training data dependent variables (pd.Series or list)
        # decision_boundary: list of boundaries of each decision variable,
        # obj_func: generate objectives, all objectives are higher the better
        # e.g. decision_boundary = [("gini", "entropy"), [1, 16], [0, 0.1]] for my_DT means:
        # the first argument criterion can be chosen as either "gini" or "entropy"
        # the second argument max_depth can be any number 1 <= max_depth < 16
        # the third argument min_impurity_decrease can be any number 0 <= min_impurity_decrease < 0.1
        # generation_size: number of points in each generation
        # selection_rate: percentage of survived points after selection, only affect single objective
        # mutation_rate: probability of being mutated for each decision in each point
        # crossval_fold: number of fold in cross-validation (for evaluation)
        # max_generation: early stopping rule, stop when reached
        # max_life: stopping rule, stop when max_life consecutive generations do not improve
        self.model = model
        self.data_X = data_X
        self.data_y = data_y
        self.decision_boundary = decision_boundary
        self.obj_func = obj_func
        self.generation_size = int(generation_size)
        self.selection_rate = selection_rate
        self.mutation_rate = mutation_rate
        self.crossval_fold = int(crossval_fold)
        self.max_generation = int(max_generation)
        self.max_life = int(max_life)
        self.life = self.max_life
        self.iter = 0
        self.generation = []
        self.best = None # for single objective only
        self.evaluated = {None: -1}

    def initialize(self):
        # Randomly generate generation_size points to self.generation
        # write your own code below


        ######################
        # check if size of generation is correct
        assert(len(self.generation) == self.generation_size)

    def evaluate(self, decision):
        # Evaluate a certain point
        # decision: tuple of decisions
        # Avoid repetitive evaluations
        if decision not in self.evaluated:
            # evaluate with self.crossval_fold fold cross-validation on self.data_X and self.data_y            
            clf = self.model(*decision)
            # write your own code below
            objs = self.obj_func(predictions, actuals, pred_proba)
            ######################
            self.evaluated[decision] = objs_crossval
        return self.evaluated[decision]

    def selection(self):
        # Select which points will survive based on the objectives
        # Evaluate all points in current generation
        objs = [self.evaluate(decision) for decision in self.generation]
        if len(objs[0]) == 1:
            objs = [obj[0] for obj in objs]
        if type(objs[0])==list:
            # multi-objective, binary domination, all undominated points survive
            # update self.generation
            # write your own code below

            ###############
            # For multi-objective, if generation stays unchanged, reduce life
            if len(self.generation)==self.generation_size:
                self.life -= 1
            else:
                self.life = self.max_life
        else:
            # single objective, keep top self.selection_rate * self.generation_size points
            # update self.generation and self.best
            # write your own code below

            ################
            # For single objective, if best point stays unchanged, reduce life
            if self.evaluate(new_best) <= self.evaluate(self.best):
                self.life -= 1
            else:
                self.best = new_best
                self.life = self.max_life
        self.iter += 1
        return

    def crossover(self):
        # randomly select two points in self.generation
        # and generate a new point, add it to self.generation
        # repeat until len(self.generation) == self.generation_size
        # write your own code below
        return

    def mutate(self):
        # Uniform random mutation:
        # each decision value in each point of self.generation
        # has the same probability self.mutation_rate of being mutated
        # to a random valid value
        # write your own code below
        return

    def tune(self):
        # Main function of my_GA
        # Stop when self.iter == self.max_generation or self.life == 0
        # write your own code below

        ###################
        if self.best:
            return self.best
        else:
            return self.generation



