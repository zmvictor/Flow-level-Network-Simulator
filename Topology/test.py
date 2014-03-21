__author__ = 'zm'

from FatTree import *

topo = FatTree(K=8)
topo.CreateTopology()
for linkId in topo.links:
    print linkId




