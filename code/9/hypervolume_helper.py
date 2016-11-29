import os


def refresh_objectives(problem, population):
    for i, obj in enumerate(problem.objectives):
        scores = [point.objectives[i] for point in population]
        obj.low = min(obj.low, min(scores))
        obj.high = max(obj.high, max(scores))


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
