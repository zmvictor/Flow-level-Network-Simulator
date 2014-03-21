=== Simulator Description ===
To use the simulator, user needs to write his/her component classes:
    TestTopology:       a test topology class inherit from base class Topology
    TestRouting:        a test routing class inherit from base class Routing
    TestFlowScheduler:  a test flow scheduler class inherit from base class FlowScheduler

There are other component classes user can customize:
    Node:               the base class of node used in topology
    Link:               the base class of link used in topology
	Flow:				the base class of flow used in flow scheduler

The core component, class Simulator, is running max-min fair methods to iteratively compute
transferring time for each flow. The default BuildPath rule in Routing is shortest path in hops.

=== Component Topology ===
TestTopology:

node_1 ------ node_2 ------ node_3

link capacity are all 10Mbps

=== Component Flow Scheduler ===
TestFlowScheduler:

3 flows, each is in size of 10MB
flow_1 starts at 1.0s, (1 to 2)
flow_2 starts at 4.0s, (1 to 3)
flow_3 starts at 6.0s ,(2 to 3)

=== Component Routing ===
TestRouting:

(src,dst): (path node ids)
(1, 2): (1, 2)
(1, 3): (1, 2, 3)
(2, 3): (2, 3)

