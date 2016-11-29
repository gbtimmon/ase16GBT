#%matplotlib inline
# All the imports
from __future__ import print_function, division
import matplotlib.pyplot as plt
import os.path
from Model import *
from DTLZ import *



def refresh_objectives(problem, population):
    for i, obj in enumerate(problem.objectives):
        scores = [point.objectives[i] for point in population]
        obj.low = min(obj.low, min(scores))
        obj.high = max(obj.high, max(scores))


def reproduce(problem, population, pop_size, mutation, crossover_rate):
    children = []
    for _ in xrange(pop_size):
        mom = random.choice(population)
        dad = random.choice(population)
        while (mom == dad):
            dad = random.choice(population)
        child = mutate(problem, crossover(mom, dad, crossover_rate), mutation)
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
        population.sort(key=lambda point: point.objectives[i])
        rge = population[-1].objectives[i] - population[0].objectives[i]
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
        return compare(y.dist, x.dist)
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


def nsgaii(pop_size=100, gens=250, mutation=0.01, crossover_rate=0.9, dom_func=bdom, problem=DTLZ1):
    population = populate(problem, pop_size)
    [problem.evaluate(point) for point in population]
    if dom_func == cdom:
        refresh_objectives(problem, population)
    initial_population = [point.clone() for point in population]
    fast_non_dominated_sort(problem, population, dom_func)
    children = reproduce(problem, population, pop_size, mutation, crossover_rate)
    if dom_func == cdom:
        [problem.evaluate(child) for child in children]
        refresh_objectives(problem, children)
    gen = 0
    while gen < gens:
        say(".")
        union = population + children
        fronts = fast_non_dominated_sort(problem, union, dom_func)
        parents = select_parents(problem, fronts, pop_size)
        population = children
        children = reproduce(problem, parents, pop_size, mutation, crossover_rate)
        if dom_func == cdom:
            [problem.evaluate(child) for child in children]
            refresh_objectives(problem, children)
        gen += 1
    union = population + children
    fronts = fast_non_dominated_sort(problem, union, dom_func)
    parents = select_parents(problem, fronts, pop_size)
    print("")
    return initial_population, parents


# def write_results(filename, problem, final):
#     f = open(filename, 'w')
#     f.write(problem.name + "\n")
#     for i, point in enumerate(final):
#         total = 0
#         for j in xrange(len(problem.objectives)):
#             total += problem.objectives[j].normalize(point.objectives[j])
#         f.write("{0} ".format(total / len(problem.objectives)))
#     f.write("\n")
#     f.close()


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

try:
    os.mkdir('results')
except Exception:
    pass

# initial, final = ga(gens=50, problem=DTLZ1())
# write_results('results/GA_DTLZ1.out', DTLZ1(), final)

# initial, final = nsgaii(problem=DTLZ1(), crossover_rate=1.0, mutation=(1 / 20.0), dom_func=cdom)
# write_results('results/NSGA_DTLZ1.out', DTLZ1(), final)

# initial, final = ga(gens=50, problem=POM3())
# write_results('results/GA_POM3.out', POM3(), final)

# initial, final = ga(gens=50, problem=DTLZ3())
# write_results('results/GA_DTLZ3.out', DTLZ3(), final)

results_file = open('results/results.txt', 'w')
obj_list = [2, 4, 6]
decisions_list = [10, 20, 40]
dom_func_list = [bdom, cdom]
prob_func_list = [DTLZ1, DTLZ3, DTLZ5, DTLZ7]

for prob in prob_func_list:
    for func in dom_func_list:
        for obj_num in obj_list:
            for dec_num in decisions_list:
                print('NSGA_{3}_{2}({0}, {1})'.format(obj_num, dec_num, func.__name__, prob.__name__))
                for i in xrange(20):
                    say("Run " + str(i + 1).zfill(2) + ": ")
                    problem = prob(obj_num, dec_num)
                    initial, final = nsgaii(gens=50, problem=problem, dom_func=func)
                    # writing results of the frontier for hypervol to calculate
                    write_results('NSGA_{1}_{0}.txt'.format(i, prob.__name__), problem, final)
                results_file.write('NSGA_{3}_{2}_{0}_{1}\n'.format(obj_num, dec_num, func.__name__, prob.__name__))
                h_list = get_hypervolume_list()
                for item in h_list:
                    results_file.write(str(item) + " ")
                    results_file.write("\n")
                results_file.flush()
                say("Hypervolumes: ")
                print(h_list)
                print()

results_file.close()

# initial, final = nsgaii(gens=50, problem=DTLZ7())
# write_results('results/GA_DTLZ7.out', DTLZ7(), final)

# plot_pareto(initial, final)




