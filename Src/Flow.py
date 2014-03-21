__author__ = 'zm'

from Unit import *

# This file describes the class Flow.
# Any specific flow class should inherit from this class

class Flow:
    def __init__(self):
        # Flow Id
        self.flowId = -1

        # Flow size
        self.remainSize = 0.0

        # Obtained bandwidth
        self.bw = 0.0

        # Start&End node id for this flow
        self.startId = -1
        self.endId = -1

        # Path nodes
        self.pathNodeIds = []

        # Path links
        self.pathLinkIds = []

        # Start time
        self.startTime = 0.0

        # Update time
        self.updateTime = 0.0

        # Finish time
        self.finishTime = 0.0

    def BuildPath(self, pathNodeIds):
        # Build path in node ids
        self.pathNodeIds = pathNodeIds[:]
        # Build path in link ids
        for i in range(1, len(pathNodeIds)):
            self.pathLinkIds.append((pathNodeIds[i - 1], pathNodeIds[i]))


