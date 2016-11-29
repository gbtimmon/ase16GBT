from Model import *
from ga import *


def create_decisions():
    decisions = []
    decisions.append(Decision('Mutation', 0.01, 0.1))
    decisions.append(Decision('Crossover', 0.1, 1.0))
    decisions.append(Decision('Population Size', 20, 200))
    decisions.append(Decision('Generations', 10, 250))
    return decisions


class GAProblem(Problem):
    def __init__(self, dtlz_func, num_decisions, num_objectives):
        self.dtlz_func = dtlz_func
        self.num_decisions = num_decisions
        self.num_objectives = num_objectives
        decisions = self.create_decisions()
        objectives = [Objective('Hypervolume')]  # ideally we would probably want spread an other metrics but no time
        Problem.__init__(self, decisions, objectives)

    def simulate(self, decisions):
        problem = self.dtlz_func(self.num_objectives, self.num_decisions)
        inital, final = ga(problem=problem, mutation=decisions[0], crossover_rate=decisions[1],
                           pop_size=decisions[3], gens=decisions[3])
        # we would calculate hypervolume
        hypervolume = 0
        return [hypervolume]  # only need one objective due to no time

    def evaluate(self, point):
        if not point.objectives:
            point.objectives = self.simulate(point.decisions)
        return point.objectives
