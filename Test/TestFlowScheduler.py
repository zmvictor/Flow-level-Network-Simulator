__author__ = 'zm'
import sys
sys.path.append("..")

from Src.FlowScheduler import *
from Src.Flow import *

class TestFlowScheduler(FlowScheduler):
    def AssignFlows(self):
        flow_1 = Flow()
        flow_1.flowId = 1
        flow_1.remainSize = 10.0 * MB
        flow_1.startTime = 1.0
        flow_1.startId = 1
        flow_1.endId = 2
        flow_2 = Flow()
        flow_2.flowId = 2
        flow_2.remainSize = 10.0 * MB
        flow_2.startTime = 4.0
        flow_2.startId = 1
        flow_2.endId = 3
        flow_3 = Flow()
        flow_3.flowId = 3
        flow_3.remainSize = 10.0 * MB
        flow_3.startTime = 6.0
        flow_3.startId = 2
        flow_3.endId = 3
        self.flows.append(flow_1)
        self.flows.append(flow_2)
        self.flows.append(flow_3)

        self.toStartFlows = self.flows[:]
        self.toStartFlows.sort(key=lambda x: x.startTime)

    def PrintFlows(self):
        for flow in self.finishedFlows:
            print "flow %d start at %f end at %f" % (flow.flowId, flow.startTime, flow.finishTime)
