__author__ = 'zm'

import sys
sys.path.append("..")

from Src.Simulator import *
from TestFlowScheduler import *
from TestTopo import *
from TestRouting import *

def main():
    sim = Simulator()
    testTopo = TestTopology()
    testTopo.CreateTopology()
    sim.AssignTopology(topo=testTopo, cap=10.0 * Mb)
    sim.AssignRoutingEngine(Routing=TestRouting)
    sim.AssignScheduler(FlowScheduler=TestFlowScheduler)
    sim.Run()

def TestBFS():
    testTopo = TestTopology()
    testTopo.CreateTopology()
    testBFS = Routing()
    testBFS.BFS(testTopo)
    print testBFS.pathList

if __name__ == "__main__":
    #main()
    TestBFS()
