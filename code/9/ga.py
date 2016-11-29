#!/usr/bin/env python
# All the imports
from __future__ import print_function, division
from math import *
import random
import sys
import matplotlib.pyplot as plt
from Model import *
from de1 import de_1
from hypervolume_runner import *

def refresh_objectives(problem, population):
    for i, obj in enumerate(problem.objectives):
        scores = [point.objectives[i] for point in population]
        obj.low = min(obj.low, min(scores))
        obj.high = max(obj.high, max(scores))

def ga(pop_size = 100, gens = 250):
    from DTLZ import DTLZ1
    problem = DTLZ1(4,20)
    
    #population = populate(problem, pop_size)
    population = de_1(mode=DTLZ1)
    [problem.evaluate(point) for point in population]
    initial_population = [point.clone() for point in population]
    gen = 0 
    while gen < gens:
        say(".")
        children = []
        for _ in range(pop_size):
            mom = random.choice(population)
            dad = random.choice(population)
            while (mom == dad):
                dad = random.choice(population)
            child = mutate(problem, crossover(mom, dad))
            if problem.is_valid(child) and child not in population+children:
                children.append(child)
        population += children
        population = elitism(problem, population, pop_size)
        gen += 1
    print("")
    return initial_population, population, problem

# in order to run hypervolume you need to write the results of at least 1 run of GA or NSGA
def write_results(filename, problem, population):
    refresh_objectives(problem, population)
    f = open('Pareto_Fronts/' + filename, 'w')
    for point in population:
        for i, obj in enumerate(point.objectives):
            f.write(str(problem.objectives[i].normalize(obj)) + " ")
        f.write("\n")
    f.close()


# this will run hypervolume on all of the previously saved results in the Pareto Fronts folder
# returns a list of hypervolumes
def get_hypervolume_list():
    from hypervolume_runner import HyperVolume_wrapper
    hypervol = HyperVolume_wrapper()
    # clean up files
    for f in os.listdir('./Pareto_Fronts/'):
        os.remove('./Pareto_Fronts/' + f)
    return hypervol

def plot_pareto(initial, final):
    initial_objs = [point.objectives for point in initial]
    final_objs = [point.objectives for point in final]
    initial_x = [i[0] for i in initial_objs]
    initial_y = [i[1] for i in initial_objs]
    final_x = [i[0] for i in final_objs]
    final_y = [i[1] for i in final_objs]
    plt.scatter(initial_x, initial_y, color='b', marker='+', label='initial')
    plt.scatter(final_x, final_y, color='r', marker='o', label='final')
    plt.title("Scatter Plot between initial and final population of GA")
    plt.ylabel("Total Surface Area(T)")
    plt.xlabel("Curved Surface Area(S)")
    plt.legend(loc=9, bbox_to_anchor=(0.5, -0.175), ncol=2)
    plt.show()
    
#initial, final = ga()
#plot_pareto(initial, final)

initial, final, problem = ga(gens=50)
f = open('a.out', 'w')

for i in xrange(len(problem.objectives)):
    f.write(problem.objectives[i].name + "\n")
    for j in xrange(len(final)):
        f.write("{0} ".format(problem.objectives[i].normalize(final[j].objectives[i])))
    f.write("\n")
f.close()

try:
    os.mkdir('results')
except Exception:
    pass

results_file = open('results/results.txt', 'w')
write_results('GA_DTLZ1_1.txt', problem, final)
results_file.write('GA_DTLZ1_1\n')
h_list = get_hypervolume_list()
for item in h_list:
    results_file.write(str(item) + " ")
results_file.flush()
say("Hypervolumes: ")
print(h_list)

plot_pareto(initial, final)
