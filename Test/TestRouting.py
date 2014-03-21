__author__ = 'zm'

import sys
sys.path.append("..")

from Src.Routing import *

class TestRouting(Routing):
    def BuildPath(self):
        self.pathList[(1, 2)] = [1, 2]
        self.pathList[(1, 3)] = [1, 2, 3]
        self.pathList[(2, 3)] = [2, 3]
    def GetPath(self, srcId, dstId):
        return self.pathList[(srcId, dstId)]
