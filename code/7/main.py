from DTLZ7 import DTLZ7
from DE import de
from SA import sa
from MWS import mws
from stats import rdivDemo

from helper.sk import *
if __name__ == '__main__':
    repeats = 20
    # repeats = 1
    for model in [DTLZ7]:
        data = []
        baseline = [model() for _ in xrange(repeats)]
        for i,optimizer in enumerate([sa,mws,de]):
        # for i,optimizer in enumerate([sa]):
            opt_rpt = []
            opt_rpt.append(optimizer.func_name)
            for j in range(repeats):
                print "\nStarting Model = %s Optimizer = %s Repeat No = %s \n" % ("DTLZ7",str(optimizer.__name__),str(j+1))
                res = optimizer(model, baseline[j])
                opt_rpt.append(res.score())
            data.append(opt_rpt)
        rdivDemo(data)