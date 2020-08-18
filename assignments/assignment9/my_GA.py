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
        self.selection_rate = selection_rate # applies only to singe-objective
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
        # write your own code below


        ######################
        # check if size of generation is correct
        assert(len(self.generation) == self.generation_size)
        return self.generation

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
    
    def compete(self, pf_best, pf_new):
        # Compare and merge two pareto frontiers
        # If one point y in pf_best is binary dominated by another point x in pf_new
        # exist x and y; self.is_better(x, y) == 1
            # replace that point y in pf_best with the point x in pf_new
        # If one point x in pf_new is not dominated by any point y in pf_best (and does not exist in pf_best)
        # forall y in pf_best; self.is_better(y, x) == -1
            # add that point x to pf_best
        # Return True if pf_best is modified in the process, otherwise return False
        # Write your own code below
        
        

    def select(self):
        # Select which points will survive based on the objectives
        # Update the following:
            # self.pf = pareto frontier (undominated points from self.generation)
            # self.generation = suvived points
                # Multi-objective: self.generation = self.pf
                # Single-objective: len(self.pf) == 1, self.generation keep top self.selection_rate * self.generation_size points
            
        # Write your own code below

    def crossover(self):
        # randomly select two points in self.generation
        # and generate a new point
        # repeat until self.generation_size points were generated
        # Write your own code below
        
        ######################
        # check if size of generation is correct
        assert(len(self.generation) == self.generation_size)
        return self.generation

    def mutate(self):
        # Uniform random mutation:
        # each decision value in each point of self.generation
        # has the same probability self.mutation_rate of being mutated
        # to a random valid value
        # write your own code below
        
        ######################
        # check if size of generation is correct
        assert(len(self.generation) == self.generation_size)
        return self.generation

    def tune(self):
        # Main function of my_GA
        # Stop when self.iter == self.max_generation or self.life == 0
        # Return the best pareto frontier pf_best (list of decisions that never get binary dominated by any candidate evaluated)
        self.initialize()
        while self.life > 0 or self.iter < self.max_generation:
            self.select()      
            if self.compete(self.pf_best, self.pf):
                self.life = self.max_life
            else:
                self.life -= 1
            self.iter += 1
            self.crossover()
            self.mutate()
        return self.pf_best



