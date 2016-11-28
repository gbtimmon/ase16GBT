#%matplotlib inline
# All the imports
from __future__ import print_function, division
import matplotlib.pyplot as plt
import os.path
from Model import *
from DTLZ import *


# def crossover(mom, dad):
#     decisions = []
#     for i in xrange(len(mom.decisions)):
#         if random.random() > 0.5:
#             decisions.append(mom.decisions[i])
#         else:
#             decisions.append(dad.decisions[i])
#     return Point(decisions)


def reproduce(problem, population, pop_size):
    children = []
    # for i, p1 in enumerate(population):
    #     if (i % 2 == 0):
    #         p2 = population[i+1]
    #     else:
    #         p2 = population[i-1]
    #     if i == len(population) - 1:
    #         p2 = population[0]
    #     child = mutate(problem, crossover(p1, p2))
    #     children.append(child)
    #     if(len(children) >= pop_size):
    #         break
    # return children

    for _ in xrange(pop_size):
        mom = random.choice(population)
        dad = random.choice(population)
        while (mom == dad):
            dad = random.choice(population)
        child = mutate(problem, crossover(mom, dad))
        if problem.is_valid(child) and child not in population + children:
            children.append(child)
    return children


def fast_non_dominated_sort(problem, population, dom_func=bdom):
    fronts = []
    first_front = []
    for p in population:
        p.dom_set = []
        p.dom_count = 0
        for q in population:
            if(dom_func(problem, p, q)):
                p.dom_set.append(q)
            elif(dom_func(problem, q, p)):
                p.dom_count += 1
        if(p.dom_count == 0):
            p.rank = 0
            first_front.append(p)
    fronts.append(first_front)

    curr = 0
    while(curr < len(fronts)):
        next_front = []
        for p1 in fronts[curr]:
            for p2 in p1.dom_set:
                p2.dom_count -= 1
                if(p2.dom_count == 0):
                    p2.rank = curr + 1
                    next_front.append(p2)
        curr += 1
        if(len(next_front) > 0):
            fronts.append(next_front)
    return fronts


def calculate_crowding_distance(problem, population):
    for point in population:
        point.dist = 0.0
    for i in xrange(len(problem.objectives)):
        min_point = min(population, key=lambda point: point.objectives[i])
        max_point = max(population, key=lambda point: point.objectives[i])
        rge = max_point.objectives[i] - min_point.objectives[i]
        population[0].dist = float("inf")
        population[-1].dist = float("inf")
        if(rge == 0):
            continue
        for j in xrange(1, len(population) - 1):
            population[j].dist += (population[j+1].objectives[i] - population[j-1].objectives[i]) / rge


def compare(a, b):
    return (a > b) - (a < b)


def crowded_comparison_operator(x, y):
    if(x.rank == y.rank):
        return compare(x.dist, y.dist)
    return compare(x.rank, y.rank)


def select_parents(problem, fronts, pop_size):
    [calculate_crowding_distance(problem, front) for front in fronts]
    offspring = []
    last_front = 0
    for front in fronts:
        if((len(offspring) + len(front)) > pop_size):
            break
        for point in front:
            offspring.append(point)
        if(fronts.index(front) < len(fronts) - 1):
            last_front += 1
    remaining = pop_size - len(offspring)
    if(remaining > 0):
        fronts[last_front].sort(cmp=crowded_comparison_operator)
        offspring += fronts[last_front][0:remaining]
    return offspring


def nsgaii(pop_size=100, gens=250, dom_func=bdom, problem=DTLZ1):
    population = populate(problem, pop_size)
    [problem.evaluate(point) for point in population]
    initial_population = [point.clone() for point in population]
    fast_non_dominated_sort(problem, population, dom_func)
    children = reproduce(problem, population, pop_size)
    # [problem.evaluate(child) for child in children]
    gen = 0
    while gen < gens:
        say(".")
        union = population + children
        fronts = fast_non_dominated_sort(problem, union, dom_func)
        parents = select_parents(problem, fronts, pop_size)
        population = children
        children = reproduce(problem, parents, pop_size)
        # [problem.evaluate(child) for child in children]
        gen += 1
    union = population + children
    fronts = fast_non_dominated_sort(problem, union, dom_func)
    parents = select_parents(problem, fronts, pop_size)
    print("")
    return initial_population, parents


def write_results(filename, problem, final):
    f = open(filename, 'w')
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

# initial, final = ga(gens=50, problem=DTLZ1())
# write_results('results/GA_DTLZ1.out', DTLZ1(), final)

# initial, final = nsgaii(problem=DTLZ1())
# write_results('results/NSGA_DTLZ1.out', DTLZ1(), final)

# initial, final = ga(gens=50, problem=POM3())
# write_results('results/GA_POM3.out', POM3(), final)

# initial, final = ga(gens=50, problem=DTLZ3())
# write_results('results/GA_DTLZ3.out', DTLZ3(), final)

initial, final = nsgaii(gens=50, problem=DTLZ5())
write_results('results/NSGA_DTLZ5.out', DTLZ5(), final)

# initial, final = nsgaii(gens=50, problem=DTLZ7())
# write_results('results/GA_DTLZ7.out', DTLZ7(), final)

plot_pareto(initial, final)




