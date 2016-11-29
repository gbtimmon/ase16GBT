#!/usr/bin/env python
# All the imports
from __future__ import print_function, division
from math import *
import random
import sys
import matplotlib.pyplot as plt
from Model import *
from de1 import de
from hypervolume_runner import *
from DTLZ import *
from hypervolume_helper import *


def ga(pop_size=100, gens=250, problem=DTLZ1, mutation=0.01, crossover_rate=0.9):
    population = populate(problem, pop_size)
    [problem.evaluate(point) for point in population]
    initial_population = [point.clone() for point in population]
    gen = 0 
    while gen < gens:
        say(".")
        children = []
        for _ in range(pop_size):
            mom = random.choice(population)
            dad = random.choice(population)
            while mom == dad:
                dad = random.choice(population)
            child = mutate(problem, crossover(mom, dad, crossover_rate), mutation)
            if problem.is_valid(child) and child not in population+children:
                children.append(child)
        population += children
        population = elitism(problem, population, pop_size)
        gen += 1
    print("")
    return initial_population, population



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

if __name__ == "__main__":
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
