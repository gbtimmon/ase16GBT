from Model import *
import math


def create_objectives(num_objectives):
    objs = []
    for i in xrange(num_objectives):
        objs.append(Objective(str(i)))
        objs[-1].high = sys.float_info.min
        objs[-1].low = sys.float_info.max
    return objs


def create_decisions(num_decisions):
    decs = []
    for i in xrange(num_decisions):
        decs.append(Decision(str(i), 0, 1))
    return decs


class DTLZ1(Problem):
    def __init__(self, num_objectives=4, num_decisions=20):
        self.name = "DTLZ1({0}, {1})".format(num_objectives, num_decisions)
        self.num_objectives = num_objectives
        self.num_decisions = num_decisions
        decisions = create_decisions(num_decisions)
        objectives = create_objectives(num_objectives)
        Problem.__init__(self, decisions, objectives)

    def simulate(self, decisions):
        def g():
            total = self.num_decisions - self.num_objectives + 1
            for dec in decisions[self.num_objectives - 1:]:
                total += ((dec - 0.5) ** 2 - math.cos(20 * math.pi * (dec - 0.5)))
            return 100 * total

        objs = []
        for i in xrange(self.num_objectives):

            f1 = float(0.5 * (1 + g()))
            for x in decisions[:self.num_objectives - i + 1]:
                f1 *= float(x)
            if i != 0:
                f1 *= (1 - decisions[self.num_objectives - 1])
            objs.append(f1)
        return objs

    def evaluate(self, point):
        if not point.objectives:
            point.objectives = self.simulate(point.decisions)
        return point.objectives


class DTLZ3(Problem):
    def __init__(self, num_objectives=4, num_decisions=20):
        self.name = "DTLZ3({0}, {1})".format(num_objectives, num_decisions)
        self.num_objectives = num_objectives
        self.num_decisions = num_decisions
        decisions = create_decisions(num_decisions)
        objectives = create_objectives(num_objectives)
        Problem.__init__(self, decisions, objectives)

    def simulate(self, decisions):
        def g():
            total = self.num_decisions - self.num_objectives + 1
            for dec in decisions[self.num_objectives - 1:]:
                total += ((dec - 0.5) ** 2 - math.cos(20 * math.pi * (dec - 0.5)))
            return 100 * total

        objs = []
        for i in xrange(self.num_objectives):

            f1 = (1 + g())
            for x in decisions[:self.num_objectives - 1 - i]:
                f1 *= math.cos(x * math.pi * 1 / 2)
            if i == 0:
                f1 *= math.cos(decisions[self.num_objectives - 2] * math.pi * 1 / 2)
            else:
                f1 *= math.sin(decisions[self.num_objectives - 2 - i + 1] * math.pi * 1 / 2)
            objs.append(f1)
        return objs

    def evaluate(self, point):
        if not point.objectives:
            point.objectives = self.simulate(point.decisions)
        return point.objectives


class DTLZ5(Problem):
    def __init__(self, num_objectives=4, num_decisions=20):
        self.name = "DTLZ5({0}, {1})".format(num_objectives, num_decisions)
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
        self.name = "DTLZ7({0}, {1})".format(num_objectives, num_decisions)
        self.num_objectives = num_objectives
        self.num_decisions = num_decisions
        decisions = create_decisions(num_decisions)
        objectives = create_objectives(num_objectives)
        Problem.__init__(self, decisions, objectives)

    def simulate(self, decisions):
        def g():
            total = 0
            for dec in decisions[self.num_objectives - 1:]:
                total += dec
            return 1 + (9 / (self.num_decisions - self.num_objectives + 1) * total)

        def h(other_objectives):
            total = 0
            for i in xrange(len(other_objectives)):
                total += ((other_objectives[i] / (1 + g())) * (1 + math.sin(3 * math.pi * other_objectives[i])))
            return self.num_objectives - total

        objs = []
        for dec in decisions[:self.num_objectives - 1]:
            objs.append(dec)
        objs.append((1 + g()) * h(objs))
        return objs

    def evaluate(self, point):
        if not point.objectives:
            point.objectives = self.simulate(point.decisions)
        return point.objectives


