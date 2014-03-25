__author__ = 'zm'

from Unit import *

# This file describes the base class of link
# All the specific link class should inherit this class

class Link:

    def __init__(self, id):
        # link ID is named as tuple of (start node id, destination node id)
        self.linkId = id

        # link capacity
        self.linkCap = 1.0 * Gb

        # Current Flow ids on this link
        self.flowIds = []

    def __del__(self):
        pass