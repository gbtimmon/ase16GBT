from Model import *
import math


def create_objectives(num_objectives):
    objs = []
    for i in xrange(num_objectives):
        objs.append(Objective(str(i)))
    return objs


def create_decisions(num_decisions):
    decs = []
    for i in xrange(num_decisions):
        decs.append(Decision(str(i), 0, 1))
    return decs


class DTLZ1(Problem):
    def __init__(self, num_objectives=4, num_decisions=20):
        self.num_objectives = num_objectives
        self.num_decisions = num_decisions
        decisions = create_decisions(num_decisions)
        objectives = create_objectives(num_objectives)
        Problem.__init__(self, decisions, objectives)

    def simulate(self, decisions):
        def g():
            total = 0
            for i in xrange(len(decisions)):
                total += ((decisions[i] - 0.5) ** 2 - math.cos(20 * math.pi * (decisions[i] - 0.5)))
            return 100 * (self.num_decisions + total)

        objs = []
        for i in xrange(self.num_objectives):

            f1 = float(0.5 * (1 + g()))
            for j in xrange(0, self.num_objectives - 1 - i):
                f1 *= float(decisions[j])
            f1 *= float(1 - float(decisions[self.num_objectives - 1 - i]))  # might be j? not sure
            objs.append(f1)
        return objs

    def evaluate(self, point):
        if not point.objectives:
            point.objectives = self.simulate(point.decisions)
        return point.objectives


class DTLZ3(Problem):
    def __init__(self, num_objectives=4, num_decisions=20):
        self.num_objectives = num_objectives
        self.num_decisions = num_decisions
        decisions = create_decisions(num_decisions)
        objectives = create_objectives(num_objectives)
        Problem.__init__(self, decisions, objectives)

    def simulate(self, decisions):
        def g():
            total = 0
            for i in xrange(len(decisions)):
                total = total + (decisions[i] - 0.5) ** 2 - math.cos(20 * math.pi * (decisions[i] - 0.5))
            return 100 * (self.num_decisions + total)

        objs = []
        for i in xrange(self.num_objectives):

            f1 = (1 + g())
            for j in xrange(0, self.num_objectives - 1 - i):
                f1 *= math.cos(decisions[j] * math.pi * 1 / 2)
            if (i == 0):
                f1 *= math.cos(decisions[j] * math.pi * 1 / 2)
            else:
                f1 *= math.sin(decisions[j] * math.pi * 1 / 2)
            objs.append(f1)
        return objs

    def evaluate(self, point):
        if not point.objectives:
            point.objectives = self.simulate(point.decisions)
        return point.objectives


class DTLZ5(Problem):
    def __init__(self, num_objectives=4, num_decisions=20):
        self.num_objectives = num_objectives
        self.num_decisions = num_decisions
        decisions = create_decisions(num_decisions)
        objectives = create_objectives(num_objectives)
        Problem.__init__(self, decisions, objectives)

    def simulate(self, decisions):
        def g():
            total = 0
            for i in xrange(len(decisions)):
                total += (decisions[i] - 0.5) ** 2
            return total

        def theta(val):
            return math.pi * (1 + 2 * g() * val) / (4 * (1 + g()))

        objs = []
        for i in xrange(self.num_objectives):
            f1 = (1 + g())
            for j in xrange(0, self.num_objectives - 1 - i):
                f1 *= math.cos(theta(decisions[j]) * math.pi * 1 / 2)
            if (i == 0):
                f1 *= math.cos(theta(decisions[j]) * math.pi * 1 / 2)
            else:
                f1 *= math.sin(theta(decisions[j]) * math.pi * 1 / 2)
            objs.append(f1)
        return objs

    def evaluate(self, point):
        if not point.objectives:
            point.objectives = self.simulate(point.decisions)
        return point.objectives


class DTLZ7(Problem):
    def __init__(self, num_objectives=4, num_decisions=20):
        self.num_objectives = num_objectives
        self.num_decisions = num_decisions
        decisions = create_decisions(num_decisions)
        objectives = create_objectives(num_objectives)
        Problem.__init__(self, decisions, objectives)

    def simulate(self, decisions):
        def g():
            total = 0
            for i in xrange(len(decisions)):
                total += decisions[i]
            return 1 + 9 / self.num_decisions * total

        def h(other_objectives):
            total = 0
            for i in xrange(len(other_objectives)):
                total += ((other_objectives[i] / (1 + g())) * (1 + math.sin(3 * math.pi * other_objectives[i])))
            return self.num_objectives - total

        objs = []
        for i in xrange(self.num_objectives - 1):
            objs.append(decisions[i])
        objs.append((1 + g()) * h(objs))
        return objs

    def evaluate(self, point):
        if not point.objectives:
            point.objectives = self.simulate(point.decisions)
        return point.objectives


