__author__ = 'zm'
import sys
sys.path.append("..")

from Src.Topology import *
from Src.Node import *
from Src.Link import *


class TestTopology(Topology):
    def CreateTopology(self):
        # Node 0 is useless
        self.nodes.append(None)
        # Build 3 nodes.
        for i in range(1, 4):
            node = Node()
            node.nodeId = i
            self.nodes.append(node)
        self.nodes[1].adjNodeIds.append(2)
        self.nodes[2].adjNodeIds.append(1)
        self.nodes[2].adjNodeIds.append(3)
        self.nodes[3].adjNodeIds.append(2)

        self.links[(1, 2)] = Link((1, 2))
        self.links[(2, 3)] = Link((2, 3))

