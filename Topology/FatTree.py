__author__ = 'zm'

import sys
sys.path.append("..")

from Src.Topology import *
from Src.Node import *
from Src.Link import *

class FatTree(Topology):
    def __init__(self, K=4):
        # initialize nodes and links
        Topology.__init__(self)
        # default topology size is K=4
        self.K = K
        # calculate servers number
        self.CalServerNums()
        # calculate tor switch number
        self.CalToRNums()
        # calculate aggregate switch number
        self.CalAggrNums()
        # calculate core switch number
        self.CalCoreNums()

    def CreateTopology(self):
        # create nodes
        self.CreateNodes()
        # create links
        self.CreateLinks()

    def CreateLinks(self):
        """
        We build this topology as a directed graph.
        It indicates n1 --- n2 will translate into to edges: (1, 2) and (2, 1)
        """
        for serverId in range(1, self.numOfServers + 1):
            s2torId = (serverId - 1) / (self.K / 2) + 1
            torNodeId = s2torId + self.numOfServers
            self.links[serverId, torNodeId] = Link((serverId, torNodeId))
            self.links[torNodeId, serverId] = Link((torNodeId, serverId))
        for torId in range(1, self.numOfToRs + 1):
            podId = (torId - 1) / (self.K / 2) + 1
            torNodeId = torId + self.numOfServers
            for i in range(0, self.K / 2):
                t2aggrId = (podId - 1) * (self.K / 2) + 1 + i
                aggrNodeId = t2aggrId + self.numOfServers + self.numOfToRs
                self.links[torNodeId, aggrNodeId] = Link((torNodeId, aggrNodeId))
                self.links[aggrNodeId, torNodeId] = Link((aggrNodeId, torNodeId))
        for aggrId in range(1, self.numOfAggrs + 1):
            aggrNodeId = aggrId + self.numOfServers + self.numOfToRs
            for j in range(0, self.K / 2):
                a2coreId = ((aggrId - 1) % (self.K / 2)) * (self.K / 2) + 1 + j
                coreNodeId = a2coreId + self.numOfServers + self.numOfToRs + self.numOfAggrs
                self.links[aggrNodeId, coreNodeId] = Link((aggrNodeId, coreNodeId))
                self.links[coreNodeId, aggrNodeId] = Link((coreNodeId, aggrNodeId))

    def CreateNodes(self):
         # node id is start from 1
        self.nodes.append(None)
        # append server node
        self.AddNodes(self.numOfServers)
        # append tor switch node
        self.AddNodes(self.numOfToRs)
        # append aggregate switch node
        self.AddNodes(self.numOfAggrs)
        # append core switch nodes
        self.AddNodes(self.numOfCores)

    # calculate related metircs
    def CalServerNums(self):
        self.numOfServers = self.K ** 3 / 4
    def CalToRNums(self):
        self.numOfToRs = self.K ** 2 / 2
    def CalAggrNums(self):
        self.numOfAggrs = self.K ** 2 / 2
    def CalCoreNums(self):
        self.numOfCores = self.K ** 2 / 4

    # add n nodes to topology instance
    def AddNodes(self, n):
        for id in range(1, n + 1):
            node = Node()
            node.nodeId = len(self.nodes)
            self.nodes.append(node)

    # return corresponding role
    def GetServerNode(self, serverId):
        return self.nodes[serverId]
    def GetToRNode(self, torId):
        return self.nodes[torId + self.numOfServers]
    def GetAggrNode(self, aggrId):
        return self.nodes[aggrId + self.numOfServers + self.numOfToRs]
    def GetCoreNode(self, coreId):
        return self.nodes[coreId + self.numOfServers + self.numOfToRs + self.numOfAggrs]

    def __del__(self):
        pass