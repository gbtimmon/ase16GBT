from Model import *
from hypervolume_helper import *
from DTLZ import *


def create_decisions():
    return [Decision('Mutation', 0.01, 0.1), Decision('Crossover', 0.1, 1.0),
            Decision('Population Size', 20, 200), Decision('Generations', 10, 250)]


class GAProblem(Problem):
    def __init__(self, dtlz_func, num_objectives, num_decisions):
        self.dtlz_func = dtlz_func
        self.num_decisions = num_decisions
        self.num_objectives = num_objectives
        decisions = create_decisions()
        objectives = [Objective('Hypervolume', do_minimize=False)]  # ideally we would probably want spread and other metrics but no time
        Problem.__init__(self, decisions, objectives)

    def simulate(self, decisions):
        from ga import ga
        problem = self.dtlz_func(self.num_objectives, self.num_decisions)
        inital, final = ga(problem=problem, mutation=decisions[0], crossover_rate=decisions[1],
                           pop_size=int(decisions[2]), gens=int(decisions[3]))
        # we would calculate hypervolume
        write_results('ga_results.txt', problem, final)
        return get_hypervolume_list()  # only need one objective due to no time

    def evaluate(self, point):
        if not point.objectives:
            point.objectives = self.simulate(point.decisions)
        return point.objectives

    def score(self, point):
        return point.objectives[0]

    def ok(self, point):
        return True

    def better(self, p1, p2):
        return self.score(p1) > self.score(p2)

if __name__ == "__main__":
    prob = GAProblem(DTLZ1, 4, 20)
    point = prob.generate_one()
    print(prob.evaluate(point))
    print(point)
